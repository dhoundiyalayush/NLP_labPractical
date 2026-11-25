# Program 3: Stemming and Lemmatization using NLTK
import nltk
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.stem import PorterStemmer, WordNetLemmatizer

words = ["running", "playing", "cars", "studies"]
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Stemming:", [stemmer.stem(word) for word in words])
print("Lemmatization:", [lemmatizer.lemmatize(word) for word in words])
