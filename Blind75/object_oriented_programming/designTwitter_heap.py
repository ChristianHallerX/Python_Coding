"""
355. Design Twitter (Medium), similar to "23 Merge K Lists, HARD"

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

    1  Twitter()
        Initializes your twitter object.
    2 postTweet(int userId, int tweetId)
        Composes a new tweet with ID tweetId by the user userId.
        Each call to this function will be made with a unique tweetId.
    3 getNewsFeed(int userId)
        Retrieves the 10 most recent tweet IDs in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user themselves.
        Tweets must be ordered from most recent to least recent.
    4 follow(int followerId, int followeeId)
        The user with ID followerId started following the user with ID followeeId.
    5 unfollow(int followerId, int followeeId)
        The user with ID followerId started unfollowing the user with ID followeeId.
"""

# every value added to the dict is already wrapped in a default data structure
from collections import defaultdict
import heapq


class Twitter:
    """
    followMap: data structure to associate followerId with followeeId map with set. e.g., a hashSet
    tweetMap: data structure hash map for userId -> list (negative count (timestamp), tweetId)
    Feed like "merge k sorted lists" -> get list of followIds, merge lists (list of lists) use pointers
        to choose on counter

    Time complexity: O(10 * k) -> O(k) naive list implementation with k followers.
                     O(10 * logk) minHeap optimized, but heapify O(k) -> Still O(k), optimizing not required lol
    """

    def __init__(self):
        self.count = 0  # used as timestamp, counting negative for minHeap
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # add count (timestamp) and tweetId to tweet map
        self.tweetMap[userId].append([self.count, tweetId])
        # decrement for next tweet
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # grab last tweet from each followee, heapify to minHeap (based on count), pop 10 last elements to result list
        result = []  # sorted starting from recent
        minHeap = []

        # add user themself to followMap (specified in task) so they follow themselves/see their own tweets, too
        self.followMap[userId].add(userId)

        # go through all followeeIds and get their tweets
        for followeeId in self.followMap[userId]:

            # we don't know if this followee has tweeted at all, check if there is anything in the tweetMap
            if followeeId in self.tweetMap:
                # index is last element of the list of lists
                index = len(self.tweetMap[followeeId]) - 1
                # Get the last list and unpack count and tweetId
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append(
                    [count, tweetId, followeeId, index - 1]
                )  # index-1 is the next position to look at in list

        heapq.heapify(minHeap)
        # pop from minHeap, extract values, and append to result list
        while minHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)

            # if this followeeId had more tweets
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add to hash set
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove value if value in hash set
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
    print(twitter.getNewsFeed(1), "expected [5]")
    twitter.follow(1, 2)  # User 1 follows user 2.
    twitter.postTweet(2, 6)  # User 2 posts a new tweet (id = 6).
    print(twitter.getNewsFeed(1), "expected [6, 5]")
    twitter.unfollow(1, 2)  # User 1 unfollows user 2.
    print(twitter.getNewsFeed(1), "expected [5]")
