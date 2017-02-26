import ConfigParser		#to get API keys from another configuration file
import json

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

class Create_conn:
	"""docstring for Create_conn"""
	def __init__(self):
		
		config = ConfigParser.ConfigParser()
		config.read('.twitter')

		self.consumer_key = config.get('apikey', 'key')
		self.consumer_secret = config.get('apikey', 'secret')
		self.access_token = config.get('token', 'token')
		self.access_token_secret = config.get('token', 'secret')
		self.stream_rule = config.get('app', 'rule')
		self.account_screen_name = config.get('app', 'account_screen_name').lower() 
		self.account_user_id = config.get('app', 'account_user_id')

	def authorize(self):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		self.tweetApi = API(auth)
		return self.tweetApi
		
if __name__ == '__main__':
	myconn= Create_conn()
	twitterApi= myconn.authorize()