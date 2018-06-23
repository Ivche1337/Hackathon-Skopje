import tweepy
import authenticator
import twitter_client
import tokens

if __name__ == "__main__":
	client = twitter_client.TwitterClient()

	print(client.get_timeline("pycon", 5))
