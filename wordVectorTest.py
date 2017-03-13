from wordVector import WordVector
import sys

wordVector = WordVector(sys.argv[1])

wordVector.createModel()

print wordVector.getMostSimilar('means')
print wordVector.getVocab()
#for item in wordVector.getVocab():
#    print item