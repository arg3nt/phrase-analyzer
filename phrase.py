from functools import reduce

class Phrase:
    def __init__(self, lexemes):
        self.lexemes = lexemes
    
    def __str__(self):
        return reduce(lambda x, y: x + " " + y, [lex.value for lex in self.lexemes])
