from flask import Flask, session, request, redirect, render_template, url_for
from flask_ask import Ask, statement, question
from twitter_client import TwitterClient
import tweepy
import tokens

app = Flask(__name__)
ask = Ask(app, "/twitter_skill")

CALLBACK_URL = 'http://localhost:5000/verify'
db = {}
session = {}

@app.route("/")
def send_token():
	auth = tweepy.OAuthHandler(tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET, CALLBACK_URL)
	redirect_url= auth.get_authorization_url()
	session['request_token']=auth.request_token
	
	return redirect(redirect_url)	

@app.route("/verify")
def get_verification():
	verifier= request.args['oauth_verifier']
	
	auth = tweepy.OAuthHandler(tokens.CONSUMER_KEY, tokens.CONSUMER_SECRET)
	token = session['request_token']
	del session['request_token']
	
	auth.request_token = token
	auth.get_access_token(verifier)
	api = tweepy.API(auth)
	db['api']=api
	db['access_token_key']=auth.access_token
	db['access_token_secret']=auth.access_token_secret
	return redirect(url_for('start'))

@app.route("/start")
def start():
	return("You are all set!")

@ask.launch
def new_ask():
    return statement("Welcome to twitter lex! Please say: How can I use twitter lex, for help.")

@ask.intent('ReadTweets')
def read_post(user_id):
	return statement(TwitterClient(db['access_token_key'],db["access_token_secret"]).get_timeline(user_id, num_of_posts = 20))

@ask.intent('PostTweet')
def post_tweet(tweet):
    return statement(TwitterClient(db['access_token_key'],db["access_token_secret"]).post_status(tweet))

@ask.intent('SearchTweets')
def stream_tweet(hashtag):
	return statement(TwitterClient(db['access_token_key'],db["access_token_secret"]).get_tweets(hashtag, num_of_posts = 20))

@ask.intent('AMAZON.HelpIntent')
def help():
	return question("You can use twitter lex to read top user tweets by saying: Read top tweets from ...; Read newest tweets with some hasthag by saying: Read lattest tweets with hashtag..., or to post new tweet by saying: Tweet for me... What would you like to do?")


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye!")

@ask.intent('AMAZON.CancelIntent')
def cancel():
	return statement("Okay")

if __name__ == '__main__':
	app.secret_key = 'secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.debug = True
	app.run()
