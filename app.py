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
#    welcome = render_template('welcome')
#    reprompt = render_template('reprompt')
#    return question(welcome) \
#        .reprompt(reprompt)

@ask.intent('ReadTweets')
def read_post():
	return statement(TwitterClient().get_timeline(num_of_posts = 3))

#@ask.intent('QPostTweet')
#def post_tweet():
#	return question("Do you want me to post something on your twitter feed")
	

if __name__ == '__main__':
	app.run(debug=True)
