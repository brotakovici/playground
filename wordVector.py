# Code is inspired from this tutorial/article https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-2-word-vectors
from gensim.models import word2vec
from nltk import word_tokenize

class WordVector(object):

    # Initializes the object, given a vocab size and a file for the input.
    def __init__(self, filePath, vocabSize):
        self.file = open(filePath, 'r')
        self.vocabSize = vocabSize

    # Reads the file and doesn't do much yet.
    def prepData(self):
        self.data = []
        for line in self.file:
            tokens = word_tokenize(line)
            self.data.append(tokens)
        #print reduce(lambda x, y: x + " " + y, tokens)

        print self.data
        return self.data

    def createModel(self, lines):

        self.model = word2vec.Word2Vec(lines, min_count=3)

        #print self.model.vocab

        if 'means' in self.model.vocab:
            print self.model.most_similar(['means'])

    def getModel(self):
        return self.model

    def saveModel(self, filename):
        self.model.save(filename)