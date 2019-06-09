from textblob import TextBlob
text = "Python is worst"
obj = TextBlob(text)
sentiment = obj.sentiment.polarity
print(sentiment)
