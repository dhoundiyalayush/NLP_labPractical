# Program 6: Chunking and Named Entity Recognition using NLTK
# The supplied practical's code performs Named Entity Recognition (NER).
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("maxent_ne_chunker_tab")
nltk.download("words")

from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

text = "Apple is located in California."
tagged_words = pos_tag(word_tokenize(text))
named_entities = ne_chunk(tagged_words)
print(named_entities)
