import nltk

grammar = "NP: {<DT>?<JJ>*<NN>}"

sentence = "A vehicle is a human made machine that provides transport."
tokens = nltk.word_tokenize(sentence)
print tokens
tagged = nltk.pos_tag(tokens)
print tagged
parser = nltk.RegexpParser(grammar)
tree = parser.parse(tagged)
print tagged
tree.draw()