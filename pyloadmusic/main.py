from __future__ import unicode_literals

import logging
import urllib.parse
from queue import Queue
from threading import Thread

import requests
import youtube_dl

# import custom library
from config import youtube_config

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger('main')


class Worker(Thread):
    """ Thread executing tasks from a given task queue """
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args = self.tasks.get()
            try:
                func(*args)
            except Exception as error:
                # An exception happened while executing
                print(error)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool:
    """ Pool of threads consuming tasks from a queue """

    def __init__(self, num_threads=10):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def map(self, func, arg_list):
        """ Add a list of tasks to the queue """
        for args in arg_list:
            self.tasks.put((func, args))

    def wait_completion(self):
        """ Wait for completion of all tasks in the queue """
        self.tasks.join()


def find_song_url(query):
    """
    Use SearX to search for a song on YouTube
    :param query: The query describing the song to look for (example artist and title)
    :return: The URL of the song on YouTube to be sent to youtube-dl
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "en-US,en;q=0.5",
        "Origin": "null",
        "Connection": "keep-alive",
        "Cookie": "results_on_new_tab=0; safesearch=0; categories='music\054general'; oscar-style=logicodev; language=en-US; image_proxy=1; autocomplete=; theme=some_theme; method=POST; disabled_engines=\"deezer__music\054torrentz__music\054mixcloud__music\054seedpeer__music\054invidious__music\054genius__music\054piratebay__music\054soundcloud__music\054btdigg__music\"; enabled_engines=; disabled_plugins=; enabled_plugins='",
        "Upgrade-Insecure-Requests": "1",
        }

    data = f"category_music=1&{urllib.parse.urlencode({'q': query})}&pageno=1&time_range=None&language=en-US&format=json"

    url = "http://127.0.0.1:7777/"
    response = requests.get(url, data, headers=headers).json()
    for result in response["results"]:
        #title, url, content, host, engine, score, _type = line.split(",")
        if result["engine"] == "youtube":
            return result["url"]
    return None


def get_mp3(query):
    #logger.info(f"Downloading {song[1]} from {song[0]}")
    logger.info(f"Downloading {query}")

    # Find the url to download based on track in query
    song_url = find_song_url(query)

    pos = song_url.find("&list")
    if pos != -1:
        song_url = song_url[:pos]
    try:
        # start download with file config
        ydl_opts = youtube_config.get_youtube_config()
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_url])
    except Exception as e:
        print(e)


if __name__ == "__main__":

    try:
        fileName = input("Supply file name with tracks e.g., my_list.txt OR\n"
                         "Press ENTER to load example_list.txt\n"
                         "Input:"
                        )
        if fileName == "":
            fileName = "./example_list.txt"
    except Exception as e:
        print(e)

    # extract track names from file and load into queries list
    queries = []
    with open(fileName, "r") as f:
        tracks = []
        for line in f.readlines():
            title, artist = line.strip().split("|")
            track = (title, artist)
            queries.append(f"{track[0]} {track[1]}")
    logger.info(f"Downloading {len(tracks)} tracks.")

    # set up threads/workers
    pool = ThreadPool(5)

    # feed queries to thread pool
    pool.map(get_mp3, [(x,) for x in queries])
    pool.wait_completion()