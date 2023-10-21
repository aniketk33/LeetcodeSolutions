import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.tweet_time = 0
        self.followers_id = defaultdict(set)
        self.post_tweets = defaultdict(list)

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.post_tweets[user_id].append([self.tweet_time, tweet_id])
        self.tweet_time -= 1

    def getNewsFeed(self, user_id: int) -> List[int]:
        result = []
        # store the tweet_time, tweet_id, followee_id and the next index of tweet_id
        min_heap = []
        # add self to the list of followers
        self.followers_id[user_id].add(user_id)
        # get all the followers of the given user
        for followee_id in self.followers_id[user_id]:
            # check if followee_id has posted any tweets
            if followee_id in self.post_tweets:
                tweet_index = len(self.post_tweets[followee_id]) - 1
                # get the particular tweet for the followee_id at the given index
                tweet_time, tweet_id = self.post_tweets[followee_id][tweet_index]
                min_heap.append([tweet_time, tweet_id, followee_id, tweet_index - 1])
        heapq.heapify(min_heap)
        while min_heap and len(result) < 10:
            tweet_time, tweet_id, followee_id, tweet_index = heapq.heappop(min_heap)
            result.append(tweet_id)
            # out of bound case
            if tweet_index >= 0:
                tweet_time, tweet_id = self.post_tweets[followee_id][tweet_index]
                heapq.heappush(min_heap, [tweet_time, tweet_id, followee_id, tweet_index - 1])

        return result

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.followers_id[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.followers_id[follower_id]:
            self.followers_id[follower_id].remove(followee_id)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
