"""
355. Design Twitter (Medium)

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

    - Twitter() Initializes your twitter object.

    - postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
        Each call to this function will be made with a unique tweetId.

    - getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user themself.
        Tweets must be ordered from most recent to least recent.

    - follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.

    - unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with
        ID followeeId.
"""

class Twitter:

    def __init__(self):


    def postTweet(self, userId: int, tweetId: int) -> None:


    def getNewsFeed(self, userId: int) -> List[int]:


    def follow(self, followerId: int, followeeId: int) -> None:


    def unfollow(self, followerId: int, followeeId: int) -> None:


if __name__ == "__main__":

    obj = Twitter()
    obj.postTweet(userId,tweetId)
    param_2 = obj.getNewsFeed(userId)
    obj.follow(followerId,followeeId)
    obj.unfollow(followerId,followeeId)
