# Code is inspired from this tutorial/article https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-2-word-vectors
from gensim.models import word2vec
from nltk import word_tokenize
import nltk
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

class WordVector(object):

    # Initializes the object, given a vocab size and a file for the input.
    def __init__(self, filePath, vocabSize):
        self.file = open(filePath, 'r')
        self.vocabSize = vocabSize

    # Reads the file and doesn't do much yet.
    # Assumes it gets sentences, tokenizes and returns a list of lists of words, as that's what the word2vec module takes.
    # Assumes each line is a sentence.
    def prepData(self):
        self.data = []
        for line in self.file:
            tokens = word_tokenize(line)
            self.data.append(tokens)
        #print reduce(lambda x, y: x + " " + y, tokens)

        return self.data

    # Works pretty well, tested on SPL-1.0, might need a bit better mapping to remove random stuff depending on license
    def getSentences(self):
        data = self.file.read()
        sentences = tokenizer.tokenize(data)

        sentences = list(map(lambda x: x.replace('\n', '').replace('   ', ''), sentences))

        return sentences

    def createModel(self, lines):

        self.model = word2vec.Word2Vec(lines, min_count=3)

        #print self.model.vocab

        if 'means' in self.model.vocab:
            print self.model.most_similar(['means'])

    def getMostSimilar(self, word):
        if word in self.model.vocab:
            return self.model.most_similar([word])
        else:
            return []

    def getModel(self):
        return self.model

    def saveModel(self, filename):
        self.model.save(filename)