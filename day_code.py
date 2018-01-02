# pip install python-twitter
import twitter

# connection à twitter
api = twitter.Api(consumer_key="kHSFnkhDL7koDMg5ws85BnFzJ",
                  consumer_secret="wwZdpqibtzt8p1puFRmMq37iNfWqLf3wFzw2e01LzM4n0b1yDu",
                  access_token_key="702409853667508224-aPVOmtrWNEa05x2p9ifzxHcoM1uhi7K",
                  access_token_secret="DjcVavUBuirMMUo9iDgOWh4VLZiDFKsz74Qmqs8nlyI50")

# Qui sont mes amis ?
my_friends = api.GetFriends()
print([my_friend.name for my_friend in my_friends])

# Qui sont tes amis ?
my_friends = api.GetFriends(screen_name="@IamBaloGouN")
print([my_friend.name for my_friend in my_friends])

# Quelles sont les tendances du moment
top_trends = api.GetTrendsCurrent()
print(top_trends)

# Quels sont les tweets contenant le mot "love"
search_love_tweets = api.GetSearch(term="love")
print(search_love_tweets)
