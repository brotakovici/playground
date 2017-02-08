# Code is inspired from this tutorial/article https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-2-word-vectors
from gensim.models import word2vec
import nltk

class WordVector(object):

    # Initializes the object, given a vocab size and a file for the input.
    def __init__(self, filePath, vocabSize):
        self.file = open(filePath, 'r')
        self.vocabSize = vocabSize

    # Reads the file and doesn't do much yet.
    def prepData(self):
        self.data = []
        raw = self.file.read()
        lines = raw.split("\n")

        return lines

    def createModel(self, lines):
        self.model = word2vec.Word2Vec(lines, vocabSize)

    def getModel(self):
        return self.model

    def saveModel(self, filename):
        self.model.save(filename)