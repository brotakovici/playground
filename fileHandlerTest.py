from licenseHandler import LicenseHandler
import sys

handler = LicenseHandler(sys.argv[1])

defParagraphLines = handler.getDefinitionsParagraph()

for line in handler.constructDefinitions(defParagraphLines):
    print line