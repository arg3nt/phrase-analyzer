from collections import deque
from reader import Reader
from lexeme import Lexeme
from phrase import Phrase

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import graph as gr

lexemes = {}
reader = Reader('input.txt', 1)
startWord = "χριστοῦ"

word = reader.nextWord()

# Process all words into lexemes
while word is not None:
    if not lexemes.get(word):
        lexemes[word] = Lexeme(word)
    
    if len(reader.prevWords) > 1:
        # Add current lexeme to previous lexeme's "next" list
        prevWord = reader.prevWords[-1]
        prevLex = lexemes[prevWord]
        
        prevLex.addNext(word)
        lexemes[word].addPrev(prevWord)

    word = reader.nextWord()

print("Finished processing input:")

G = nx.DiGraph()

gr.compile_from_start(G, lexemes, startWord)

nx.write_graphml(G, 'graph.graphml')

