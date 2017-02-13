import nltk
from nltk.parse.stanford import StanfordParser

path_to_jar = "PLACEHOLDER"
path_to_models_jar = "PLACEHOLDER"

dependency_parser = StanfordParser(path_to_jar = path_to_jar, path_to_models_jar = path_to_models_jar)

result = dependency_parser.raw_parse('I shot an elephant in my sleep')
dep = result.next()
list(dep.triples())