import os
from VectorSpace_English import VectorSpace
from ReadPrint import *

if __name__ == '__main__':
    path = '../dataSets/smaller_dataset/collections'
    collectionFiles= os.listdir(path)
    collections = []
    ReadFiles(collections, collectionFiles, path)

################################################################
    path = '../dataSets/smaller_dataset/queries'
    queryFiles= os.listdir(path)
    queries = []
    ReadFiles(queries, queryFiles, path)

    for index, queryFile in enumerate(queryFiles):
        #print("before:", queryFiles[index])
        queryFiles[index] = queryFile.replace(".txt", "")
        #print("after:", queryFiles[index])

################################################################
    relevanceDict = {}
    relevancePath = '../dataSets/smaller_dataset/rel.tsv'
    relevances = open(relevancePath, 'r').readlines()
    ReadRel(relevances, relevanceDict)

################################################################

    APS = []
    RRS = []
    recalls = []
    vectorSpace = VectorSpace(collections)
    for query, q in zip(queries,queryFiles):
        AP = []
        RR = []
        r = 0
        queryString = query.split(" ")
        scores = vectorSpace.search(queryString, "Cosine")[0]
        rank = vectorSpace.search(queryString, "Cosine")[1]
        for index,i in zip(rank[:10],range(10)):
            doc = collectionFiles[index]
            for character in["d", ".txt"]:
                if character in doc:
                    doc = doc.replace(character, "")
            if doc in relevanceDict[q]:
                r += 1
                AP.append(r/(i+1))
                RR.append(1/(i+1))
        if len(RR) != 0:
            rr = sum(RR)/len(RR)
        recall = r/len(relevanceDict[q])
        ap = sum(AP)/10
        recalls.append(recall)
        APS.append(ap)
        RRS.append(rr)
    averageRecall = sum(recalls)/len(recalls)
    MRR = sum(RRS)/len(RRS)
    MAP = sum(APS)/len(APS)
    
################################################################

    PrintEvaluation(MRR, MAP, averageRecall)
