import tweepy
import authenticator
import twitter_client
import tokens

if __name__ == "__main__":
	client = twitter_client.TwitterClient(authenticator.Authenticator(
		tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET, 
		tokens.ACCESS_TOKEN, tokens.ACCESS_TOKEN_SECRET).authenticate())

	print(client.get_timeline())
