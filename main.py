from licenseHandler import LicenseHandler
from conceptExtractor import ConceptExtractor
import sys

documentOne = sys.argv[1]
#documentTwo = sys.argv[2]

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
            print "-----------------------------------------------"
            print concept[0]
            occurences = conceptExtractor.matchConcept(concept, sentences)
            print occurences
            conceptOccurencePair.append((concept, occurences))

    return conceptOccurencePair

print analyseDocument(documentOne)