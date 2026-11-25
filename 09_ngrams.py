# Program 9: Unigram, Bigram and Trigram using NLTK
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")

from nltk.tokenize import word_tokenize
from nltk.util import ngrams

text = "A waterfall is a river or body of water."
tokens = word_tokenize(text)

print("Unigrams:", list(ngrams(tokens, 1)))
print("Bigrams:", list(ngrams(tokens, 2)))
print("Trigrams:", list(ngrams(tokens, 3)))
