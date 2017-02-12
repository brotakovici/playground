from licenseHandler import LicenseHandler
from os import listdir
from os.path import isfile, join
import sys

def extractDefinitions(filePath):
    handler = LicenseHandler(filePath)
    definitionsParagraph = handler.getDefinitionsParagraph()
    constructedDefinitions = handler.constructDefinitions(definitionsParagraph)

    return constructedDefinitions

def saveDefinitions(filePath, definitions):
    outputFile = open(filePath, 'w')
    for line in definitions:
        outputFile.write(line)
        outputFile.write('\n')
    outputFile.close()

fileNames = [f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]

for fileName in fileNames:
    print fileName
    filepath = sys.argv[1] + fileName
    definitions = extractDefinitions(filepath)
    saveDefinitions(filepath + '.def', definitions)