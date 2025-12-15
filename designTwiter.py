
from collections import defaultdict
from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((-self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        maxheap=[]
        users=set(self.following[userId])
        users.add(userId)

        for userId in users:
            idx=len(self.tweets[userId])
            if self.tweets[userId]:
                time,tweet=self.tweets[userId][-1]
                heapq.heappush(maxheap,(time,tweet,userId,idx-1))

        while maxheap and len(res)<10:
            time,tweet,userId,idx=heapq.heappop(maxheap)
            res.append(tweet)
            if idx-1>=0:
                time,tweet=self.tweets[userId][idx-1]
                heapq.heappush(maxheap,(time,tweet,userId,idx-1))
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

#the intuation is very simple, to design this version of twitter we only needed a hashmap of each user containing their tweets along with the time of tweet
#we store the time as -ve as we need the recent tweets first which we will get by maxheap. 
#we also needed a hashmap of all the users which points which user is following which one, we made it a set to eliminate duplicate following
#in post tweet we simply add a new tweet with time stamp in tweets map
#in follow we simply follow one person to another in set 
#in unfollow we do the same and unfollow a person just remove that person from set
# in get news feed we first get the user's own and all the person he follows the recent tweets and then
#just use heap to only get the most recent tweets untill the list size is 10 or there are no more tweets and we return the list
#time is O(FlogF) where F is no of user a specific user is following and space is O(F) +O(T) where f is total no of user and t is total no of tweets

        
        
