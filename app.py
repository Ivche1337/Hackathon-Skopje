from flask import Flask, request, render_template
from flask_ask import Ask, statement, question, session
from twitter_client import TwitterClient

app = Flask(__name__)
ask = Ask(app, "/twitter_skill")

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@ask.launch
def new_ask():
        return statement("Hi!")

@ask.intent('ReadTweets')
def read_post(user_id):
	return statement(TwitterClient().get_timeline(user_id, num_of_posts = 10))

@ask.intent('PostTweet')
def post_tweet(tweet):
        print(tweet)
        return statement(TwitterClient().post_status(tweet))


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye!")


@ask.intent('AMAZON.CancelIntent')
def cancel():
	return statement("Okay")


if __name__ == '__main__':
	app.run(debug=True)
