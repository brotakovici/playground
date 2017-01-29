from licenseHandler import LicenseHandler
import sys

handler = LicenseHandler(sys.argv[1])

for line in handler.getDefinitionsParagraph():
    print line