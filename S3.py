from nltk.parse.stanford import StanfordDependencyParser
from nltk.tokenize.stanford_segmenter import StanfordSegmenter

eng_parser = StanfordDependencyParser(path_to_jar=r"D:\StanfordNLP\stanford-parser\stanford-parser.jar",
                                      path_to_models_jar=r"D:\StanfordNLP\stanford-parser\stanford-parser-3.6.0-models.jar",
                                      model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')

outputs = ' '.join(tokenizer.tokenize(sentence))

print(outputs)

result = list(eng_parser.parse(outputs.split()))

for row in result[0].triples():
    print(row);