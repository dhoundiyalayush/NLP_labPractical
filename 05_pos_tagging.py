# Program 5: POS Tagging using NLTK
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "The boy is playing cricket."
words = word_tokenize(text)
print("POS Tags:", pos_tag(words))
