setwd('C:/DragonBallZ/Spring2018/DIC_CSE587/Lab1')
install.packages("twitteR")
library(twitteR)

# Change the next four lines based on your own consumer_key, consume_secret, access_token, and access_secret. 
consumer_key <- "hqgRb0SNmm7TG0tAMXuF4RkHA"
consumer_secret <- "Di7vtfQNTwxZEFykQPZYHZXRyJFsjQBlfcxcN3hZYtKFLot7zM"
access_token <- "4338966852-lBmLvEg9mADHIdjK2hT4W5mtHmI9jRKxcV4PTrB"
access_secret <- "AwKRZw9AvTMvMrb2jouX5JHTjDASI3zeceVsemgQa1SSq"

setup_twitter_oauth(consumer_key, consumer_secret, access_token, access_secret)
tw = twitteR::searchTwitter('#realDonaldTrump + #HillaryClinton', n = 1e4, since = '2016-11-08', retryOnRateLimit = 1e3)
d = twitteR::twListToDF(tw)
