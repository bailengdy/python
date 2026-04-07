import heapq
from collections import defaultdict

# HeapQ
# DefaultDict - Set/List
class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[user_id].append((self.time, tweet_id))
        self.time -= 1

    def get_news_feed(self, user_id: int):
        heap = []
        res = []
        self.following[user_id].add(user_id)
        for followee_id in self.following[user_id]:
            if self.tweets[followee_id]:
                idx = len(self.tweets[followee_id]) - 1
                time, tweet_id = self.tweets[followee_id][idx]
                heapq.heappush(heap, (time, tweet_id, followee_id, idx - 1))
        while heap and len(res) < 10:
            time, tweet_id, followee_id, next_idx = heapq.heappop(heap)
            res.append(tweet_id)
            if next_idx >= 0:
                next_time, next_tweet_id = self.tweets[followee_id][next_idx]
                heapq.heappush(heap, (next_time, next_tweet_id, followee_id, next_idx - 1))
        return res

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id != follower_id:
            self.following[follower_id].discard(followee_id)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)