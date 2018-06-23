import tweepy
import json

class TwitterListener(tweepy.StreamListener):

	def __init__(self):
		pass

	def on_data(self, data):
		all_data = json.loads(data)
		print((all_data['user']['screen_name'],all_data['text']))
		return True 

	def on_error(self, status_code):
		if status_code == 420:
			return False
