import tweepy
import tokens
import authenticator
import twitter_listener


class TwitterStreamer():

	def __init__(self):
		self.auth = authenticator.Authenticator(tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET, 
												tokens.ACCESS_TOKEN, tokens.ACCESS_TOKEN_SECRET).authenticate()
		self.listener = twitter_listener.TwitterListener()

	def streaming(self, hashtags):
		stream = tweepy.Stream(self.auth, self.listener)
		stream.filter(track = hashtags)