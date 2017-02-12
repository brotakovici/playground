from wordVector import WordVector
import sys

wordVector = WordVector(sys.argv[1], 200)

sentences = wordVector.getSentences()
for sentence in sentences:
    print "----\n"
    print sentence

#data = wordVector.prepData()

#wordVector.createModel(data)