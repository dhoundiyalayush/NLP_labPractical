# Program 4: Comparison of Stemming and Lemmatization
import nltk
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.stem import PorterStemmer, WordNetLemmatizer

words = ["playing", "running", "cars", "studies"]
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

for word in words:
    print(f"{word}: Stem = {stemmer.stem(word)}, Lemma = {lemmatizer.lemmatize(word)}")
