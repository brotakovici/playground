import nltk
from nltk.parse.stanford import StanfordParser
import re
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize
from nltk import ngrams

path_to_jar = "/Users/DMNDPL1/Projects/Code/3rd Year/playground/lib/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar"
path_to_models_jar = "/Users/DMNDPL1/Projects/Code/3rd Year/playground/lib/stanford-english-corenlp-2016-10-31-models.jar"

words_to_split_on = ['means', 'mean', 'shall mean']

class ConceptExtractor(object):

    # Not being used at the moment

    def __init__(self):
        self.dependency_parser = StanfordParser(path_to_jar = path_to_jar, path_to_models_jar = path_to_models_jar, encoding='utf-8')
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
            conceptWords = self.splitConcept(conceptRawForm)
            # Get the base form/lemma
            lemma = self.lemmatizeConceptWords(conceptWords)
            # Also gets the stem, to recognize as many forms of the word
            stem = self.stemConceptWords(conceptWords)
            return (conceptRawForm, lemma, stem, definition.strip())
        else:
            return None

    # This handles multiword and hyphenated concepts, returns a list of words that together make up the concept
    def splitConcept(self, concept):
        conceptWords = concept.split(' ')
        return conceptWords

    def lemmatizeConceptWords(self, conceptWords):
        lemmatizedConceptWords = []

        for word in conceptWords:
            lemmatizedConceptWords.append(self.lemmatizer.lemmatize(word))

        return lemmatizedConceptWords

    def stemConceptWords(self, conceptWords):
        stemmedConceptWords = []

        for word in conceptWords:
            stemmedConceptWords.append(self.stemmer.stem(word))

        return stemmedConceptWords

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

        return result.strip().replace("\"", "").replace("\'", "").replace("(", "").replace(")", "").replace(".", "").replace("/", "")

    # Will extract all concepts (NP) in a sentence.
    # Need to play around with the depth, at the moment it's favoring super concepts (very specific concepts made from many words).
    def extractGeneralConcepts(self, sentence):
        tree = self.dependency_parser.raw_parse(sentence)
        tree = tree.next()
        concepts = []
        for subtree in tree.subtrees():
            if subtree.label() == 'NP':
                concepts.append(subtree.leaves())

        print concepts
        return (sentence, concepts)

    # Given a concept and a list of sentences, will return the sentences in which the concept appears
    def matchConcept(self, concept, sentences):
        extractedConceptForm = concept[0]
        lemmas = concept[1]
        stems = concept[2]
        definition = concept[3]
        conceptSize = len(stems)

        for sentence in sentences:
            kgrams = ngrams(sentence.split(), conceptSize)
            for kgram in kgrams:
                print kgram

    def compareLemmas(self):
        return "bazaconii"

    def compareStems(self):
        return "bazaconii"