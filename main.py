from licenseHandler import LicenseHandler
from conceptExtractor import ConceptExtractor
import sys

handler = LicenseHandler(sys.argv[1])

defParagraphLines = handler.getDefinitionsParagraph()

constructedDefinitions = handler.constructDefinitions(defParagraphLines)

conceptExtractor = ConceptExtractor()

definedConcepts = []

for definition in constructedDefinitions:
    definedConcepts.append(conceptExtractor.extractDefinedConcept(definition))

generalConcepts = []

sentences = handler.getSentences()

print sentences