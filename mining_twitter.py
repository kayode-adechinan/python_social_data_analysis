# create twitter app -> https://apps.twitter.com/

import twitter
api = twitter.Api(consumer_key="kHSFnkhDL7koDMg5ws85BnFzJ",
                  consumer_secret="wwZdpqibtzt8p1puFRmMq37iNfWqLf3wFzw2e01LzM4n0b1yDu",
                  access_token_key="702409853667508224-aPVOmtrWNEa05x2p9ifzxHcoM1uhi7K",
                  access_token_secret="DjcVavUBuirMMUo9iDgOWh4VLZiDFKsz74Qmqs8nlyI50")

# check if everything work as expected
print(api)

# get info about current user

my_friends = api.GetFriends()
print([my_friend.name for my_friend in my_friends])


# your_friends = api.GetFriends(screen_name="@IamBaloGouN")
# print([your_friend.name for your_friend in your_friends])

# get top trends
top_trends = api.GetTrendsCurrent()
print(top_trends)

# get top trends from us
top_us_trends = api.GetTrendsWoeid("23424977")
print(top_us_trends)
print(top_us_trends[0].name)

# simple search

search_love_tweets = api.GetSearch(term="love")
print(search_love_tweets)