# Code is inspired from this tutorial/article https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-2-word-vectors
from gensim.models import word2vec
from nltk import word_tokenize
from nltk import sent_tokenize
import nltk
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

class WordVector(object):

    # Initializes the object, reads the data from the file.
    def __init__(self, filePath):
        self.data = open(filePath, 'r').read()

    # Reads the file and doesn't do much yet.
    # Assumes it gets sentences, tokenizes and returns a list of lists of words, as that's what the word2vec module takes.
    # Assumes each line is a sentence.
    def prepData(self):
        sentences = sent_tokenize(self.data)

        #print reduce(lambda x, y: x + " " + y, tokens)

        return sentences

    def createModel(self):
        lines = self.prepData()
        tokens = []
        for line in lines:
            tokens.append(word_tokenize(line))

        self.model = word2vec.Word2Vec(tokens, min_count=3)

        #print self.model.vocab

        if 'means' in self.model.vocab:
            print self.model.most_similar(['means'])

    def getMostSimilar(self, word):
        if word in self.model.vocab:
            return self.model.most_similar([word])
        else:
            return []

    def getVocab(self):
        return self.model.vocab


    def getModel(self):
        return self.model

    def saveModel(self, filename):
        self.model.save(filename)