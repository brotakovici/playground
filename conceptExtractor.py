import nltk
from nltk.parse.stanford import StanfordParser
import re
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

path_to_jar = "/Users/DMNDPL1/Projects/Code/3rd Year/playground/lib/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar"
path_to_models_jar = "/Users/DMNDPL1/Projects/Code/3rd Year/playground/lib/stanford-english-corenlp-2016-10-31-models.jar"

words_to_split_on = ['means', 'mean', 'shall mean']

class ConceptExtractor(object):

    # Not being used at the moment

    def __init__(self):
        #self.dependency_parser = StanfordParser(path_to_jar = path_to_jar, path_to_models_jar = path_to_models_jar)
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()


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

        # If one of the common definition words is found, split on it and extract what is on the left of it,
        # as that's where usually the concept being defined is placed.
        if wordToSplitOn  != '':
            newLine = definition.split(wordToSplitOn)
            # Strip definition numbers and other punctuation marks.
            conceptRawForm =  self.prettifyConcept(newLine[0])
            # Get the base form/lemma
            lemma = self.lemmatizer.lemmatize(conceptRawForm)
            # Also gets the stem, to recognize as many forms of the word
            stem = self.stemmer.stem(conceptRawForm)
            return (conceptRawForm, lemma, stem)
        else:
            return None

    # Strips definition number, removes quotes and other random punctuation marks.
    def prettifyConcept(self, concept):
        pattern = re.compile(r"([0-9]+[.]?)+")
        explodedConcept = concept.split(' ')
        result = ''
        #print explodedConcept
        explodedConcept = list(filter(lambda x: not pattern.match(x), explodedConcept))
        #print explodedConcept
        for item in explodedConcept:
            result += " " + item

        return result.strip().replace("\"", "").replace("\'", "")