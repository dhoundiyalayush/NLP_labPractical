# Program 2: Stopword Removal using NLTK
import nltk
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a simple natural language processing program."
stop_words = set(stopwords.words("english"))
words = word_tokenize(text)
filtered = [word for word in words if word.lower() not in stop_words]

print("After stopword removal:", filtered)
