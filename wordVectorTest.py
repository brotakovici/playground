from wordVector import WordVector
import sys

wordVector = WordVector(sys.argv[1], 200)

data = wordVector.prepData()
#wordVector.createModel(data)
#wordVector.saveModel(sys.argv[2])

wordVector.createModel(data)