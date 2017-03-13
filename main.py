from licenseHandler import LicenseHandler
from conceptExtractor import ConceptExtractor
import sys

documentOne = sys.argv[1]
#documentTwo = sys.argv[2]


# Returns (concept, occurences) pair.
def analyseDocument(documentName):
    documentHandler = LicenseHandler(documentName)

    defParagraphLines = documentHandler.getDefinitionsParagraph()

    constructedDefinitions = documentHandler.constructDefinitions(defParagraphLines)

    conceptExtractor = ConceptExtractor()

    definedConcepts = []

    for definition in constructedDefinitions:
        definedConcepts.append(conceptExtractor.extractDefinedConcept(definition))

    sentences = documentHandlerg.getSentences()

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
        concept = item[0][0]
        for conceptToMatch in documentTwoAnalisis:
            if concept == conceptToMatch[0][0]:

    return None

documentOneAnalisis = analyseDocument(documentOne)
documentTwoAnalisis = analyseDocument(documentTwo)