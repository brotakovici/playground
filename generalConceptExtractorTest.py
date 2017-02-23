from conceptExtractor import ConceptExtractor
import sys
from nltk.tokenize import sent_tokenize

filename = sys.argv[1]

f = open(filename, 'r')

data = f.read()

# Data massaging might need to be moved to the licenseHandler class
sentences = sent_tokenize(data)

sentences = list(map(lambda sentence: sentence.replace("\n", " "), sentences))

conceptExtractor = ConceptExtractor()

for sentence in sentences:
    for concepts in conceptExtractor.extractGeneralConcepts(sentence):
        print concepts
        print '------------------------------------------------------'