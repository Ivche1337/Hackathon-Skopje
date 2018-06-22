import tweepy

class Authenticator():

	def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
		self.consumer_secret = CONSUMER_SECRET
		self.consumer_key = CONSUMER_KEY
		self.access_token = ACCESS_TOKEN
		self.access_token_secret = ACCESS_TOKEN_SECRET

		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)

	def authenticate(self):
		return self.auth

