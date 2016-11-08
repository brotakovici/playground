from licenseHandler import LicenseHandler
import sys

handler = LicenseHandler(sys.argv[1])

print handler.getDefinitions()