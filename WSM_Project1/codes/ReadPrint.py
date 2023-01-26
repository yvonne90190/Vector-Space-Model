import os

def ReadFiles(fileList, files, path):
    for file in files:
        if not os.path.isdir(file):
            f = open(path+"/"+file)
            iter_f = iter(f)
            str = ""
            for line in iter_f:
                str = str + line
            str.replace("\n","")
            fileList.append(str)

def ReadRel(relFile, relDict):
    for rel in relFile:
        #print("before", rel)
        for character in['[', ']', ' ', '\n']:
            if character in rel:
                rel = rel.replace(character, "")
        #print("after:", rel)
        rel = rel.split("\t")
        rel[1] = rel[1].split(",")
        relDict[rel[0]] = rel[1]
    #print(rels)

def PrintResult(files, rank, scores):
    print("NewsID\t\tscore")
    for idx in rank[:10]:
        print(files[idx], scores[idx], sep="\t")
        
def PrintEvaluation(MRR, MAP, averageRecall):
    print("tdidf retrieve ...")
    print("-"*50)
    print("tfidf\tMRR@10\t\t", MRR)
    print("tfidf\tMAP@10\t\t", MAP)
    print("tfidf\tRECALL@10\t", averageRecall)
    print("-"*50)
