from conceptExtractor import ConceptExtractor
import sys
from nltk.tokenize import sent_tokenize

filename = sys.argv[1]

f = open(filename, 'r')

data = f.read()

# Data massaging might need to be moved to the licenseHandler class
sentences = sent_tokenize(data)

doc = open(sys.argv[2], 'r')

docData = doc.read()

docSents = sent_tokenize(docData)
docSents = map(lambda sent: sent.decode('unicode-escape'), docSents)

sentences = list(map(lambda sentence: sentence.replace("\n", " "), sentences))
docSents = list(map(lambda sentence: sentence.replace("\n", " "), docSents))

conceptExtractor = ConceptExtractor()


concepts = []

for definition in sentences:
    concepts.append(conceptExtractor.extractDefinedConcept(definition))

concepts = filter(lambda x: x is not None, concepts)

stemAnalysis = []
lemmaAnalysis = []

for concept in concepts:
    stemAnalysis.append((concept, conceptExtractor.matchConcept(concept, docSents, True)))
    #print stemAnalysis
    lemmaAnalysis.append((concept, conceptExtractor.matchConcept(concept, docSents, False)))

for i in range(len(stemAnalysis)):
    if stemAnalysis[i][1] != lemmaAnalysis[i][1]:
        print "-------------------------------------"
        print "For concept :"
        concept = stemAnalysis[i][0]
        print concept[0]
        print "Stem matching extracted:"
        print len(stemAnalysis[i][1]), " occurences"
        print stemAnalysis[i][1]
        print "Lemma matching extracted:"
        print len(lemmaAnalysis[i][1]), " occurences"
        print lemmaAnalysis[i][1]