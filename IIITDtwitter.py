# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
CONSUMER_KEY = "Vu1DzQPAHCzmYBP4ssDOVjigl"
CONSUMER_SECRET = "qMnuOYbMu1JeW0QoW2pXi3kVhg6NhOS0wBvHrVhzsfJpFZbGKK"
ACCESS_TOKEN = "986631352869994496Yb1hYsx7455M4A0VaMr28tRCrR76Wmm"
ACCESS_TOKEN_SECRET = "MFhLjSC55Cz8lm46C2EBY4bUwDtrvh2uyhajA4QlkL5YP"

HOST = "127.0.0.1"
USER = "root"
PASSWD = "N0man$hahid"
DATABASE = "iiitd"

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 10000 tweets. 
tweet_count = 10000
for tweet in iterator:
    tweet_count -= 1
	listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
	streamer = tweepy.Stream(auth=auth, listener=listener)
    # We convert to the JSON format to print.
    print json.dumps(tweet)
       
    if tweet_count <= 0:
        break 

		
		
class StreamListener(tweepy.StreamListener):
	def on_data(self, data):
			try:
			   # Decode the JSON from Twitter
				datajson = json.loads(data)
				
				#grab the wanted data from the Tweet
				text = datajson['text']
				screen_name = datajson['user']['screen_name']
				tweet_id = datajson['id']
				created_at = parser.parse(datajson['created_at']) 
				
				#insert the data into the MySQL database
				store_data(created_at, text, screen_name, tweet_id)
			
			except Exception as e:
			   print(e)

		   
# This function takes the 'created_at', 'text', 'screen_name' and 'tweet_id' and stores it
# into a MySQL database
def store_data(created_at, text, screen_name, tweet_id):
    db=MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DATABASE, charset="utf8")
    cursor = db.cursor()
    insert_query = "INSERT INTO twitter (tweet_id, screen_name, created_at, text) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (tweet_id, screen_name, created_at, text))
    db.commit()
    cursor.close()
    db.close()
    return
	
