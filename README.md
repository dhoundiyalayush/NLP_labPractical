# NLP Practical Programs

This repository contains 10 separate Python files for the Natural Language Processing practicals.

## Programs
1. Tokenization using NLTK, Stanza and spaCy
2. Stopword Removal using NLTK
3. Stemming and Lemmatization using NLTK
4. Comparison of Stemming and Lemmatization
5. POS Tagging using NLTK
6. Chunking and Named Entity Recognition using NLTK
7. TF-IDF Calculation
8. CYK / Chart Parsing
9. Unigram, Bigram and Trigram
10. Sentiment Analysis using NLTK VADER

## Setup
Use Python 3. Install the required libraries:

```bash
pip install -r requirements.txt
```

For spaCy, also download its English model:

```bash
python -m spacy download en_core_web_sm
```

Some scripts download the required NLTK or Stanza language data on first run.

## Run a program
For example:

```bash
python 02_stopword_removal.py
```
