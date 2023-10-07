import os
from VectorSpace_Chinese import VectorSpace
from ReadPrint import *

if __name__ == '__main__':

    queryString = input("Query: ").split(" ")

    path = '../dataSets/ChineseNews'
    files= os.listdir(path)
    bloblist = []
    ReadFiles(bloblist, files, path)

    vectorSpace = VectorSpace(bloblist)

################################################################

    print("TF-IDF Weighting + Cosine Similarity:")
    score = vectorSpace.cosineSimilarity(queryString)[0]
    rank = vectorSpace.cosineSimilarity(queryString)[1]
    PrintResult(files, rank, score)