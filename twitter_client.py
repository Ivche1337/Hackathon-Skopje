import tweepy
import tokens
import authenticator
import re

class TwitterClient():

	def __init__(self):
		self.auth = authenticator.Authenticator(tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET, 
							tokens.ACCESS_TOKEN, tokens.ACCESS_TOKEN_SECRET).authenticate()
		self.api = tweepy.API(self.auth)

	def get_timeline(self, user_id=None, num_of_posts=1):
		posts = []
		posts_string = ""
		for status in tweepy.Cursor(self.api.user_timeline, id=user_id).items(num_of_posts):
			post = status._json["text"]
			post = re.sub(r"http\S+", "", post)
			posts.append(post)
		no = 1
		for post in posts:
			if len(post) >= 10:
				posts_string += "Tweet " + str(no) + ": " + post + "..." 
				no += 1

		return posts_string


	def post_status(self, post):
		try:
			if self.api.update_status(status = post):
				return "Post Successful"
		except tweepy.error.TweepError as e:
			return "Post not successful"
