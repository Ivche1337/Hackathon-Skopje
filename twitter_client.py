import tweepy
import tokens
import authenticator

class TwitterClient():

	def __init__(self):
		self.auth = authenticator.Authenticator(tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET, 
												tokens.ACCESS_TOKEN, tokens.ACCESS_TOKEN_SECRET).authenticate()
		self.api = tweepy.API(self.auth)

	def get_timeline(self, user_id=None, num_of_posts=5):
		self.user_id = user_id
		self.num_of_posts = num_of_posts
		self.posts = dict()
		for status in tweepy.Cursor(self.api.user_timeline, id=user_id).items(num_of_posts):
			self.posts[status._json["user"]["name"]] = status._json["text"]

		return self.posts

