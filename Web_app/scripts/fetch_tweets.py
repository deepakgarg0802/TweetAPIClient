import tweepy
from twitter_connection import *
import warnings

class TweetList:
    
    def __init__(self):

        myconn= Create_conn()
        self.myApi= myconn.authorize()

    def filterTweet(self,query):
        
        #query = '%23custserve'
        max_tweets = 1000
        searched_tweets = []
        last_id = -1

        while len(searched_tweets) < max_tweets:
            count = max_tweets - len(searched_tweets)
            try:
                new_tweets = self.myApi.search(q=query, count=count, max_id=str(last_id - 1))
                if not new_tweets:
                    break
                searched_tweets.extend(new_tweets)
                last_id = new_tweets[-1].id
                #print searched_tweets
            except tweepy.TweepError as e:
                # depending on TweepError.code, one may want to retry or wait
                # to keep things simple, we will give up on an error
                break

        mytweets={}
        for tweet in searched_tweets:
            if(tweet.retweet_count >0):
                mytweets[tweet.user.screen_name]=tweet.text
                #print tweet.user.screen_name+ " : "+ tweet.id_str
                
        return json.dumps(mytweets)

#-----ignore warning of ssl
warnings.filterwarnings("ignore")

myList= TweetList()
print myList.filterTweet(query = '%23custserve')
