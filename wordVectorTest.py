from wordVector import WordVector
import sys

print sys.argv[1]
print sys.argv[2]

wordVector = WordVector(sys.argv[1], 200)

data = wordVector.prepData()
#wordVector.createModel(data)
#wordVector.saveModel(sys.argv[2])

lines = []

for line in open(sys.argv[1], 'r')
    lines.append(line)

wordVector.createModel(lines)