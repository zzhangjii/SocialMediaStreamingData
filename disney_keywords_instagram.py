
import json

from instagram.client import InstagramAPI
#Variables that contains the user credentials to access Twitter API 
user_id = "0478bb8802a14975af020368bb1f54d2"
access_token = "11870712440.0478bb8.fb7b80abec3240729c92964e78054fbd"
client_secret = "1021a43abc6a424c85e1bad32665887b"


"""
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
access_token = "78270982-oij6sbhNAKpdpxYhn0NCErHmzSz6vOSXUIyzAJrqd"
access_token_secret = "5uj8ZGyaD03vhFfZNKuausKQRi0boTZbAbuZTDkpmxRLd"
consumer_key = "WH52sXkI1v4T2XI0nxs4K9fWs"
consumer_secret = "opkQ2G2YoB1qv7NOGVIUCKHGhelWb3oWsdMuOd7PrXx65n3kOA"

class StreamListener(StreamListener):

	def on_status(self, status):
		temp = dict()
		temp["name"] = status.user.name
		temp["text"] = status.text
		temp["screen_name"] = status.user.screen_name
		temp["followers_count"] = status.user.followers_count
		temp["reply_count"] = status.reply_count
		temp["retweet_count"] = status.retweet_count
		temp["favorite_count"] = status.favorite_count
		temp["user_mentions"] = status.entities["user_mentions"]
		temp["retweet_obj"] = get_Retweet_Info(status)
		temp["quote_obj"] = get_Quote_Info(status)
		temp["in_reply_to_screen_name"] = status.in_reply_to_screen_name
		print (json.dumps(temp))

	def on_error(self, status_code):
		print (status)

		if status_code == 420:
			return False
"""
def main():

	try:
		print("start api: ", access_token)
		api = InstagramAPI(access_token=access_token, client_secret=client_secret)
		print("finish api")
		print(api)
		api.user_incoming_requests()
		print("user_pai")

			
		"""
		recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
		for media in recent_media:
   			print(media.caption.text)
			   """
		"""
		l = StreamListener()
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		stream = Stream(auth, l)
		stream.filter(track=["DisneyPlus", "Disney+", "Disney +", "Disney Plus", "Disney Stream", "Disney Netflix", "Disney Hulu",\
			"Disney streaming service", "Disney Apple", "Disney Roku"])
		"""

	except Exception as e:
		print ("EXCEPTION IN MAIN FUNCTION!!!")
		print (e)
		exit(1)


if __name__ == "__main__":
	main()