# Program 1: Tokenization using NLTK, Stanza and spaCy

# A. NLTK
# Install if needed: pip install nltk
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
from nltk.tokenize import sent_tokenize, word_tokenize

text = "The iPhone is popular. It has a powerful camera."
print("NLTK:")
for sentence in sent_tokenize(text):
    print("Sentence:", sentence)
    print("Words:", word_tokenize(sentence))

# B. Stanza
# Install if needed: pip install stanza
import stanza
stanza.download("en")
nlp_stanza = stanza.Pipeline(lang="en", processors="tokenize")
doc = nlp_stanza(text)
print("\nStanza:")
for sentence in doc.sentences:
    print("Sentence:", sentence.text)
    print("Words:", [word.text for word in sentence.words])

# C. spaCy
# Install if needed: pip install spacy
# Also run: python -m spacy download en_core_web_sm
import spacy
nlp_spacy = spacy.load("en_core_web_sm")
doc = nlp_spacy(text)
print("\nspaCy:")
for sentence in doc.sents:
    print("Sentence:", sentence.text)
    print("Words:", [token.text for token in sentence])
