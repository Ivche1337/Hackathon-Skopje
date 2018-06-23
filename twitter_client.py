import tweepy
import tokens
import authenticator
import re

class TwitterClient():

	def __init__(self, access_token, access_token_secret):
		self.auth = authenticator.Authenticator(tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET, 
							access_token, access_token_secret).authenticate()
		self.api = tweepy.API(self.auth)

	def get_timeline(self, user_id=None, num_of_posts=1):
		posts = []
		posts_string = ""
		users = self.api.search_users(user_id)
		for status in tweepy.Cursor(self.api.user_timeline, tweet_mode="extended", id=users[0].id).items(num_of_posts):
			post = status.full_text
			post = re.sub(r"http\S+", "", post)
			posts.append(post)
		no = 1
		for post in posts:
			if len(post) >= 10 and 'RT @' not in post:
				posts_string += "Tweet " + str(no) + ": " + post + "..." 
				no += 1

		return posts_string

	def get_tweets(self, hashtag, num_of_posts=1):
		posts = []
		posts_string = ""
		for status in tweepy.Cursor(self.api.search, q=("#" + hashtag), tweet_mode="extended").items(num_of_posts):
			post = [status.user.name, status.full_text]
			post[1] = re.sub(r"http\S+", "", post[1])
			posts.append(post)
		for post in posts:
			if 'RT @' not in post[1]:
				posts_string += "Tweet from " + post[0] + ": " + post[1] + "..."
		return posts_string

	def post_status(self, post):
		try:
			if self.api.update_status(status = post):
				return "Post Successful"
		except tweepy.error.TweepError as e:
			return "Post not successful"