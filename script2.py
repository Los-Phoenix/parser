#coding:UTF-8
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
segmenter = StanfordSegmenter(
    path_to_jar=r"D:\StanfordNLP\stanford-segmenter\stanford-segmenter-3.6.0.jar",
    path_to_slf4j=r"D:\StanfordNLP\stanford-segmenter\slf4j-api.jar",
    path_to_sihan_corpora_dict=r"D:\StanfordNLP\stanford-segmenter\data",
    path_to_model=r"D:\StanfordNLP\stanford-segmenter\data\pku.gz",
    path_to_dict=r"D:\StanfordNLP\stanford-segmenter\data\dict-chris6.ser.gz"
)
str=u"我在博客园开了一个博客，我的博客名叫伏草惟存，写了一些自然语言处理的文章。"
result = segmenter.segment(str)
print result