import tweepy
import tokens
import authenticator

class TwitterClient():

	def __init__(self):
		self.auth = authenticator.Authenticator(tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET, 
												tokens.ACCESS_TOKEN, tokens.ACCESS_TOKEN_SECRET).authenticate()
		self.api = tweepy.API(self.auth)

	def get_timeline(self, user_id=None, num_of_posts=1):
		posts = []
		for status in tweepy.Cursor(self.api.user_timeline, id=user_id).items(num_of_posts):
			posts.append(status._json["text"])
		posts_string = "...".join([i for i in posts])
		if user_id != None:
			post_string = "Reading " + str(num_of_posts) + " tweets " + self.api.get_user(user_id).screen_name + " made ..." + posts_string
		else:
			post_string = "Reading " + str(num_of_posts) + " tweets you made..." + posts_string
		return post_string


	def post_status(self, post):
		try:
			if self.api.update_status(status = post):
				return "Post Successful"
		except tweepy.error.TweepError as e:
			return "Post not successful"