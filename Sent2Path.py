#coding:UTF-8
#这个文件将样例程序变成依存路径串
#串的头是第一个实体，尾是第二个实体
#串的输出正反：暂不考虑
#格式：原句子（已经检查过）@q# 单词1 单词2 ……\n

# Campbell's technology industry background included running Intuit as well as working as an Apple executive ' \
#         'and serving on the company's board of directors for 17 years after the return of Steve Jobs as chief.
# | (Campbell,BDSPerson,0,8)@#$(Apple,BDSOrganization,91,96)

import script

infile = "allInOne.txt"
outfile = "allInOneFull.txt"

sentList = list(open(infile,'r'))
outPtr = open(outfile, 'w')

cnt = 0
for sent in sentList:
    cnt += 1
    print cnt
    text = ''.join([i if ord(i) < 128 else ' ' for i in sent])
    sentClear = ' '.join(text.split())
    # print sentClear
    #rowsClear = list(script.sentToTriples(sentClear)) # this line is too haste, sentClear is like:
    #Kris Osborn is editor-in-chief of Defense Systems. | (Kris Osborn,BDSPerson,0,11)@#$(Defense Systems,BDSOrganization,34,49)
    sent, remaining = sentClear.split('|')
    # print remaining
    headRaw, tailRaw = remaining.split('@#$')
    headStr =headRaw.split(',')[0].split('(')[1]
    tailStr = tailRaw.split(',')[0].split('(')[1]
    # print headStr
    # print tailStr
    # print sent
    rowsClear = list(script.sentToTriples(sent))#似乎总是连通的
    # print rowsClear
    dependList = script.triplesToPathPhrase(rowsClear, headStr, tailStr)
    rst = ""
    rst += sent
    rst += ' @q# '
    for dependWord in dependList:
        rst += dependWord
        rst += " "
    rst += "\n"
    outPtr.write(rst)
outPtr.close()

