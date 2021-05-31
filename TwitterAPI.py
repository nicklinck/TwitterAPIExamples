import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


# The TwitterAPI Class allows you to pull tweets from a specific user and
# to see the replies to the tweets from that user
class TwitterAPI():
    
    def __init__(self):
        self.bearer_token = self.auth()
        
        
    ############################################
    ### Twitter API Request Helper Functions ###
    ############################################
    def auth(self):
        return os.environ.get("BEARER_TOKEN")
    
    def create_headers(self):
        headers = {"Authorization": "Bearer {}".format(self.bearer_token)}
        logging_debug(headers)
        # if you did not set "BEARER_TOKEN" as environment variable, 
        # type in you bearer token manually here in place of '{}'
        #headers = {"Authorization": "{}"}
        #logging_debug(headers)
        return headers


    def create_url(self, query):    
        # Tweet fields are adjustable.
        # Options include:
        # attachments, author_id, context_annotations,
        # conversation_id, created_at, entities, geo, id,
        # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
        # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
        # source, text, and withheld
        tweet_fields = "tweet.fields=author_id"
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
            query, tweet_fields
        )
        return url


    def connect_to_endpoint(self, url, headers):
        response = requests.request("GET", url, headers=headers)
        logging_debug(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()



    ##########################################
    ### Functions to Get Data from Twitter ###
    ##########################################
    def get_tweets(self, user):
        # '-is:retweet' means that retweets from this conversation will not be included
        # change 'lexfridman' to any use you would like to get tweets from
        url = self.create_url(query="from:" + user + " -is:retweet")
        headers = self.create_headers()
        json_response = self.connect_to_endpoint(url, headers)
        logging_info("get_tweets returned: " + print_json(json_response))
        return json_response


    # TODO: if the original tweet is a reply to someone else. this does not work.  
    def get_replies(self, id):
        url = self.create_url(query="conversation_id:" + id + " -is:retweet")
        headers = self.create_headers()
        json_response = self.connect_to_endpoint(url, headers)
        return json_response


    ##########################################
    ### Functions to Process Returned Data ###
    ##########################################
    def process_tweets(self):
        # get all of the tweets from a specific user
        json_response = self.get_tweets("lexfridman")

        count = 0
        for tweet in json_response["data"]:            
            logging_info(("tweet ", count, ": ", tweet["text"]))

            # get all of the replies from the initial tweet (using conversation id)
            replies = self.get_replies(tweet["id"])
            logging_info("replies: " + print_json(replies))
            count += 1


########################
### Helper Functions ###
########################
def print_json(json_response):
    return json.dumps(json_response, indent=4, sort_keys=True)

def logging_debug(message):
    if DEBUG == True:
        print(message)
        
def logging_info(message):
    if INFO == True:
        print(message)

        
#####################
### Main Function ###
#####################
if __name__ == "__main__":
    DEBUG = False # set to True in order to contain more information
    INFO = True

    twitter_api = TwitterAPI()
    twitter_api.process_tweets()




