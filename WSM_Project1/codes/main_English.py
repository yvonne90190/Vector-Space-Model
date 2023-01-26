import os
from VectorSpace_English import VectorSpace
from ReadPrint import *

if __name__ == '__main__':

    queryString = input("Query: ").split(" ")

    path = '../dataSets/EnglishNews'
    files= os.listdir(path)
    doclist = []
    ReadFiles(doclist, files, path)
    
    vectorSpace = VectorSpace(doclist)
    ################################################################
    print("TF-IDF Weighting + Cosine Similarity:")
    scores = vectorSpace.search(queryString, "Cosine")[0]
    rank = vectorSpace.search(queryString, "Cosine")[1]
    PrintResult(files, rank, scores)

    print("="*50)
    ################################################################
    
    print("TF-IDF Weighting + Euclidean Distance:")
    scores = vectorSpace.search(queryString, "Euclidean")[0]
    rank = vectorSpace.search(queryString, "Euclidean")[1]
    PrintResult(files, rank, scores)    
    
    print("="*50)
    ################################################################
    
    print("TF-IDF Weighting + Relevance Feedback:")
    scores = vectorSpace.search(queryString, "Relevance")[0]
    rank = vectorSpace.search(queryString, "Relevance")[1]
    PrintResult(files, rank, scores)