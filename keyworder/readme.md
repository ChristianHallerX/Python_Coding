
~~~shell
k                              d         
k k                            d         
kk   eee y  y w   w ooo rrr  ddd eee rrr 
k k  e e y  y w w w o o r   d  d e e r   
k  k ee   yyy  w w  ooo r    ddd ee  r   
            y                            
         yyy                             
~~~

## Description

Keyworder identifies words frequencies in job descriptions (JD) and helps identifying important keywords.
The more often a word appears in a JD, the more important it will likely be.
Make sure to integrate these high-frequency to your résumé.
However, do not omit critically evaluating lower frequency words.

NLTK is used to remove common stopwords, which are unlikely to be common keywords.


### Installation

Python 3.5+ must be installed


### Create a virtualenv 

~~~shell
python -m venv venv
~~~shell

### Source env

~~~shell
source venv/bin/activate
~~~

### Download requirements 

Run in your console:
~~~shell
pip install -r requirements.txt
~~~


## Usage 
1. Fill the example_song_list.txt file with your track list (use the same format aka =song|artist=, one per line)
2. run 'python keyworder.py', it will use searx to to find the URL of the song on YouTube Music and then download the mp3 using =youtube-dl=.


** Disclaimer
Downloading copyrighted songs may be illegal in your country. This tool is for educational purposes bla bla bla... Please support the artists by buying their music.
