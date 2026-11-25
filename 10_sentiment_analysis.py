# Program 10: Sentiment Analysis using NLTK VADER
import nltk
nltk.download("vader_lexicon")

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
text = "This product is very good and amazing."
scores = sia.polarity_scores(text)

print("Scores:", scores)
compound = scores["compound"]

if compound >= 0.05:
    print("Sentiment: Positive")
elif compound <= -0.05:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
