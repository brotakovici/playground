from licenseHandler import LicenseHandler
import sys

handler = LicenseHandler(sys.argv[1])

defParagraphLines = handler.getDefinitionsParagraph()

print list(filter(lambda x: x.replace("\n", "") is not "", defParagraphLines))