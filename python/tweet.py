import tweepy
consumer_key = "MadjiVMpJRpk7rQUrMJ2ycx6c"
consumer_secret = "GtCRStS5jBQOP1NBZp8yXMYMgOCsg3AaLnk7qdYFk1p07BkR3J"
access_token = "17453539-My3NaJUlL0l47tQ93Sqj8dL7TnRtEGvTOAYJY6BMe"
access_token_secret = "5X8fb8o6um5tB0VIAbep9wuM1yBliSASBijgbkqGAIPkq"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets

print(api.show_friendship)
# foreach through all tweets pulled

def print_timeline():
    public_tweets = api.home_timeline()
    for tweet in  public_tweets:
     #Printing the text stored inside the tweet object
     print(tweet.text)
def get_user_timeline():
    usertimeline = api.user_timeline("@swamy39")
    print(usertimeline)

def getUser():
    user = api.get_user('twitter')
    print(user.screen_name)
    print(user.followers_count)
    for friend in user.friends():
        print(friend.screen_name)
#print_timeline()
#get_user_timeline()
getUser()


