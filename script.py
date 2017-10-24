#coding:utf8

from nltk.parse.stanford import StanfordDependencyParser
import copy

def sentToTriples(sent):
    #returns a list of triples
    eng_parser = StanfordDependencyParser(r"/home/losphoenix/StanfordNLP/stanford-parser/stanford-parser.jar",
                            r"/home/losphoenix/StanfordNLP/stanford-parser/stanford-parser-3.6.0-models.jar",
                            r"/home/losphoenix/StanfordNLP/stanford-parser/englishPCFG.ser.gz")

    parsed = eng_parser.parse(sent.split())
    result = list(parsed)
#print parsed;

 #   for row in result[0].triples():
 #       print(row[0]);
    return result[0].triples()

#row = list(sentToTriples("i shot an elephant in my pajamas"))[0]
#print(row);

def triplesToPathWord(triples, v0, v1):
    #this converts triples to an Array of Path from v0 to v1 or vise
    verge = [[v0],[v1]]
    newVerge = [];
    for i in range(1, 100):
        print i
        newVerge = [];
        for triple in triples:
            hWord = triple[0][0];
            tWord = triple[2][0];

            for vv in verge:

                v = copy.deepcopy(vv);
                # print "v"
                # print verge
                if v[len(v) - 1] == hWord :
                    v.insert(len(v), tWord);
                    q = v;
                    newVerge.insert(len(newVerge), q);
                    # print newVerge;
                elif v[len(v) - 1] == tWord :
                    v.insert(len(v), hWord);
                    q = v;
                    newVerge.insert(len(newVerge), q);
                    # print v;
                    # print newVerge;

        verge = copy.deepcopy(newVerge)
        #print verge
        for v in verge:
            #print v
            if v0.find(v[0]) != -1:
                if v1.find(v[len(v)-1]) != -1:
                    v.pop(0);
                    v.pop(len(v) - 1);
                    print v
                    return v
            if v0.find(v[0]) != -1:
                if v1.find(v[len(v) - 1]) != -1:
                    v.pop(0);
                    v.pop(len(v)-1);
                    print v
                    return v





        #print(list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split())))

text = "“All good things take patience,” Intel’s GM of data centers Diane Bryant said"
text2 = ''.join([i if ord(i) < 128 else ' ' for i in text])
print text2

row = list(sentToTriples(text2))

triplesToPathWord(row, "All", "Diane")
