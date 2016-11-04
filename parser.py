import nltk
from textblob.classifiers import NaiveBayesClassifier
#import spacy

#en_nlp = spacy.load('en')

lines = open('data.txt', 'r').readlines()


### Only handles really basic definitions, doesn't take into accound colons if
### the definition uses the form NP: definition. Needs to be expanded, maybe have
### multiple patterns depending on the definitions. Need legal documents to see how
### definitions are usually done in legal language.

grammar = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
      {<NNP>+},                # chunk sequences of proper nouns
  VP: {<V.*><NP>},
  DEF: {<VBZ><NP>}
"""

train = [("A vehicle is a human-made machine that provides transport.", True),
        ("I like pie.", False),
        ("The cube is a shape.", True),
        ("An apple is ugly.", False),
        ("John is tired.", False),
        ("The apple is in the cupboard.", False)]


model = NaiveBayesClassifier(train)
definition = "DEF: {<>}"

def filt(n):
    return n.label()=='NP'

def getConcepts(tree):
    concepts = []
    for subtree in tree.subtrees(filter = filt):
        print subtree


#for line in lines:
#    tokens = nltk.word_tokenize(line)
#    tagged = nltk.pos_tag(tokens)
#    #print line
#    #print tagged
#    parser = nltk.RegexpParser(grammar)
#    tree = parser.parse(tagged)
#    getConcepts(tree)
#    #tree.draw() #Draws the tree

print model.classify("The car is a vehicle.")
print model.classify("I don't like pie.")
print model.classify("The bed is a piece of furniture.")