#coding:UTF-8
#这个文件将样例程序变成依存路径串
#串的头是第一个实体，尾是第二个实体
#串的输出正反：暂不考虑
#格式：句子：| 实体1：类型 | 实体2：类型 | 单词1 单词2 ……\n

# Campbell's technology industry background included running Intuit as well as working as an Apple executive ' \
#         'and serving on the company's board of directors for 17 years after the return of Steve Jobs as chief.
# | (Campbell,BDSPerson,0,8)@#$(Apple,BDSOrganization,91,96)

import script

infile = "allInOne.txt"
outfile = "allInOneFull.txt"

sentList = list(open(infile,'r'))
for sent in sentList:
    text = ''.join([i if ord(i) < 128 else ' ' for i in sent])
    sentClear = ' '.join(text.split())
    rowsClear = list(script.sentToTriples(sentClear))

    print text2