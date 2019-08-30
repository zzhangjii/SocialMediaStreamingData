from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json


def get_Retweet_Info(status):
	
	if status.retweeted == False:
		return ""

	else:
		return status.retweeted_status

def get_Quote_Info(status):

	if status.is_quote_status == False:
		return ""

	else:
		return status.quoted_status


#Variables that contains the user credentials to access Twitter API 
access_token = "486124046-06lYhLwzeNxLbHrOsdBo9FuTGvlK5Y2K9pmCb9z2"
access_token_secret = "iA35fHbcD1qngG0tKCvcB1k99EMAttptNfjMr8I0VMjKW"
consumer_key = "2O6Tz8pugHDdDofeIWvq6u3zt"
consumer_secret = "J9KhVPRHqDDdDCvT4HkG3vafdPBf4fqEOaCZgOPzo5eI6OVuoc"

class StreamListener(StreamListener):

	def on_status(self, status):
		temp = dict()
		temp["name"] = status.user.name
		temp["text"] = status.text
		temp["screen_name"] = status.user.screen_name
		temp["time"] = status.created_at
		temp["followers_count"] = status.user.followers_count
		temp["reply_count"] = status.reply_count
		temp["retweet_count"] = status.retweet_count
		temp["favorite_count"] = status.favorite_count
		temp["user_mentions"] = status.entities["user_mentions"]
		temp["retweet_obj"] = get_Retweet_Info(status)
		temp["quote_obj"] = get_Quote_Info(status)
		temp["in_reply_to_screen_name"] = status.in_reply_to_screen_name
		if temp["followers_count"] >= 0:
			print (temp["name"])
			print (temp["screen_name"])
			print (temp["time"])
			print (temp["text"]+"\n")
			print("***********************************************************************")

			
		


	def on_error(self, status_code):
		print (status)
		if status_code == 420:
			return False

def main():

	try:
		l = StreamListener()
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth)
		stream = Stream(auth, l)
		stream.filter(track=['#Disney'])


	except Exception as e:
		print ("EXCEPTION IN MAIN FUNCTION!!!")
		print (e)
		print (type(e))
		print (e.__dict__)
		exit(1)


if __name__ == "__main__":
	main()