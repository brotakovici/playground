import nltk
from nltk.parse.stanford import StanfordParser
import re

path_to_jar = "/Users/DMNDPL1/Projects/Code/3rd Year/playground/lib/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar"
path_to_models_jar = "/Users/DMNDPL1/Projects/Code/3rd Year/playground/lib/stanford-english-corenlp-2016-10-31-models.jar"

words_to_split_on = ['means', 'mean', 'shall mean']

class ConceptExtractor(object):

    def __init__(self):
        self.dependency_parser = StanfordParser(path_to_jar = path_to_jar, path_to_models_jar = path_to_models_jar)


    def extractDefinedConcept(self, definition):
        #tree = self.dependency_parser.raw_parse(definition)
        #tree = tree.next()
        ##concepts = []
        ##for subtree in tree.subtrees():
            ##if subtree.label() == 'NP':
                ##concepts.append(subtree.leaves())

        #print definitiong
        wordToSplitOn = ''
        for word in words_to_split_on:
            if word in definition:
                wordToSplitOn = word
                break

        if wordToSplitOn  != '':
            newLine = definition.split(wordToSplitOn)



            print self.removeDefinitionNumber(newLine[0])

        #print concepts

    def removeDefinitionNumber(self, concept):
        pattern = re.compile(r"([0-9]+[.]?)+")
        explodedConcept = concept.split(' ')
        result = ''
        print explodedConcept
        explodedConcept = list(filter(lambda x: not pattern.match(x), explodedConcept))
        print explodedConcept
        for item in explodedConcept:
            result += " " + item

        return result.strip()