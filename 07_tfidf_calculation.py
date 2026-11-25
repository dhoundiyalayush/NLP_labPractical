# Program 7: TF-IDF Calculation
# Install if needed: pip install scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "NLP processes human language",
    "Language processing is interesting",
    "NLP is useful"
]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(documents)

print("TF-IDF Matrix:")
print(matrix.toarray())
print("Feature Names:")
print(vectorizer.get_feature_names_out())
