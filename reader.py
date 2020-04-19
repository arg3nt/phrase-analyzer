from string import punctuation
from collections import deque
import re

rm_punctuation = str.maketrans('', '', punctuation)

class Reader:
    def __init__(self, filename, depth):
        self.fp = open(filename)
        self.depth = depth + 1 # prevWords will include the current word
        self.prevWords = deque([])

        self._processNewline()
    
    def nextWord(self):
        """Returns the next word in the file, keeping the list of previous words current"""
        if not self._curIndex < len(self._curLine):
            self._processNewline()
            if not self._curLine:
                return None

            while len(self._curLine) == 0:
                self._processNewline()
                if not self._curLine:
                    return None

        word = self._curLine[self._curIndex].lower()

        # skip words that are made completely empty by stripping punctuation and numbers
        while not word:
            word = self._curLine[self._curIndex].lower()


        # Update the previous words set
        self.prevWords.appendleft(word)
        while len(self.prevWords) > self.depth:
            self.prevWords.pop()
        
        self._curIndex += 1
        return word
    
    def _processNewline(self):
        self._curLine = self.fp.readline().translate(rm_punctuation)
        self._curLine = re.sub(r'\d+', '', self._curLine)
        self._curLine = self._curLine.split()

        self._curIndex = 0

    def close(self):
        self.fp.close()