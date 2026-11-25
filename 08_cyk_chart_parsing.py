# Program 8: CYK / Chart Parsing using NLTK
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det JJ JJ N | Det JJ N
VP -> V PP
PP -> P NP
Det -> 'The' | 'the'
JJ -> 'quick' | 'brown' | 'lazy'
N -> 'fox' | 'dog'
V -> 'jumps'
P -> 'over'
""")

parser = ChartParser(grammar)
sentence = "The quick brown fox jumps over the lazy dog".split()

print("CYK / Chart Parsing Trees:")
for tree in parser.parse(sentence):
    print(tree)
