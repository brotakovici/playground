from licenseHandler import LicenseHandler
from conceptExtractor import ConceptExtractor
from wordVector import WordVector
import sys

documentOne = sys.argv[1]
documentTwo = sys.argv[2]

model = WordVector(documentOne)
model.createModel()

# Returns (concept, occurences) pair.
def analyseDocument(documentName):
    documentHandler = LicenseHandler(documentName)

    defParagraphLines = documentHandler.getDefinitionsParagraph()

    constructedDefinitions = documentHandler.constructDefinitions(defParagraphLines)

    conceptExtractor = ConceptExtractor()

    definedConcepts = []

    for definition in constructedDefinitions:
        definedConcepts.append(conceptExtractor.extractDefinedConcept(definition))

    sentences = documentHandler.getSentences()

    conceptOccurencePair = []

    for concept in definedConcepts:
        if concept is not None:
            #print "-----------------------------------------------"
            #print concept[0]
            occurences = conceptExtractor.matchConcept(concept, sentences, True)
            #print occurences
            conceptOccurencePair.append((concept, occurences))

    return conceptOccurencePair

def compareDocuments(documentOneAnalisis, documentTwoAnalisis):
    differences = []

    for item in documentOneAnalisis:
        for conceptToMatch in documentTwoAnalisis:
            if item[0][0] == conceptToMatch[0][0]:
                #print conceptToMatch
                #print "\n"
                if item[0][3] != conceptToMatch[0][3]:
                    #print 'Definition changed for concept:'
                    #print item[0][0]
                    #print item
                    #print item
                    differences.append((item[0][0], item[1]))


    return differences

documentOneAnalisis = analyseDocument(documentOne)
documentTwoAnalisis = analyseDocument(documentTwo)

#for item in documentTwoAnalisis:
#    print '------------------------------------------'
#    print item

for item in compareDocuments(documentOneAnalisis, documentTwoAnalisis):

    print item[0]
    print item[1]
    print 'Similar concepts:'

    similar = model.getMostSimilar(item[0])
    if similar != []:
        print similar