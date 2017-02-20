from conceptExtractor import ConceptExtractor
import sys

filename = sys.argv[1]

f = open(filename, 'r')

conceptExtractor = ConceptExtractor()

for line in f:
    conceptExtractor.extractDefinedConcept(line)