from licenseHandler import LicenseHandler
from conceptExtractor import ConceptExtractor
import sys

documentOne = sys.argv[1]
documentTwo = sys.argv[2]


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
            occurences = conceptExtractor.matchConcept(concept, sentences)
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
                    differences.append((item[0][0], item[1]))


    return differences

documentOneAnalisis = analyseDocument(documentOne)
documentTwoAnalisis = analyseDocument(documentTwo)

#for item in documentTwoAnalisis:
#    print '------------------------------------------'
#    print item

print compareDocuments(documentOneAnalisis, documentTwoAnalisis)