import nltk
from nltk.parse.stanford import StanfordParser

path_to_jar = "/Users/DMNDPL1/Projects/Code/3rd Year/playground/lib/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar"
path_to_models_jar = "/Users/DMNDPL1/Projects/Code/3rd Year/playground/lib/stanford-english-corenlp-2016-10-31-models.jar"

dependency_parser = StanfordParser(path_to_jar = path_to_jar, path_to_models_jar = path_to_models_jar)

result = dependency_parser.raw_parse('I shot an elephant in my sleep')
dep = result.next()
list(dep.triples())