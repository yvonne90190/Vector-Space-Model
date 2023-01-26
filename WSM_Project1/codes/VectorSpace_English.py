from __future__ import division, unicode_literals
from Parser import Parser
import math
import util
import sys

try:
	import numpy as np
except:
	print("Error: Requires numpy from https://numpy.org/install/. Have you installed ?")
	sys.exit() 

class VectorSpace:
    #Collection of document term vectors
    tfVectors = []
    #idf Vector
    idfVector = []
    #Mapping of vector index to keyword
    vectorKeywordIndex=[]
    #Tidies terms
    parser=None

    def __init__(self, documents=[]):
        #self.bloblist = documents
        self.tfVectors=[]
        self.parser = Parser()
        if(len(documents)>0):
            self.build(documents)
            

    def build(self, documents):
        """ Create the vector space for the passed document strings """
        self.vectorKeywordIndex = self.getVectorKeywordIndex(documents)
        self.tfVectors = [self.makeVector(document) for document in documents]
        self.idfVector = self.makeidfVector(documents)
        self.tfVectors = self.makeTfidfVectors(self.tfVectors)


    def getVectorKeywordIndex(self, documentList):
        """ create the keyword associated to the position of the elements within the document vectors """
        #Mapped documents into a single word string	
        vocabularyString = " ".join(documentList)
        vocabularyList = self.parser.tokenise(vocabularyString)
        #Remove common words which have no search value
        vocabularyList = self.parser.removeStopWords(vocabularyList)
        uniqueVocabularyList = util.removeDuplicates(vocabularyList)
        vectorIndex={}
        offset=0
        #Associate a position with the keywords which maps to the dimension on the vector used to represent this word
        for word in uniqueVocabularyList:
            vectorIndex[word]=offset
            offset+=1
        return vectorIndex  #(keyword:position)

    def makeVector(self, wordString):
        """ @pre: unique(vectorIndex) """
        #Initialise vector with 0's
        vector = [0] * len(self.vectorKeywordIndex)
        wordList = self.parser.tokenise(wordString)
        wordList = self.parser.removeStopWords(wordList)
        for word in wordList:
            try:
                vector[self.vectorKeywordIndex[word]] += 1; #Use simple Term Count Model
            except:
                continue
        return vector

    def makeidfVector(self, documents):
        vector = [0] * len(self.vectorKeywordIndex)
        for document in documents:
            wordList = self.parser.tokenise(document)
            wordList = self.parser.removeStopWords(wordList)
            wordList = util.removeDuplicates(wordList)
            for word in wordList:
                vector[self.vectorKeywordIndex[word]] += 1; #Use simple Term Count Model
        for idx in range(len(self.vectorKeywordIndex)):
            vector[idx] = math.log(len(documents) / (vector[idx]))
        return vector

    def makeTfidfVectors(self, tfVectors):
        tfidfVectors = np.multiply(tfVectors,self.idfVector)
        return tfidfVectors

    def buildQuerytfidfVector(self, termList):
        """ convert query string into a term vector """
        query = self.makeVector(" ".join(termList))
        queryTfidf = self.makeTfidfVectors(query)
        return queryTfidf

    def search(self, searchList, flag):
        queryVector = self.buildQuerytfidfVector(searchList)
        reverse_or_not = True
        
        if flag == "Cosine":
            ratings = util.consineSimilarity(self.tfVectors, queryVector)
            
        elif flag == "Euclidean":
            ratings = [util.EuclideanDistance(queryVector, tfidfVector) for tfidfVector in self.tfVectors]
            reverse_or_not = False
            
        if flag == "Relevance":
            ratings = util.consineSimilarity(self.tfVectors, queryVector)
            """new query"""
            feedBackQuery = np.argpartition(ratings, -1)[-1:]
            for i, idx in enumerate(feedBackQuery):
                new_query = self.tfVectors[idx] * 0.5 + queryVector
            ratings = util.consineSimilarity(self.tfVectors, new_query)
            
        doc_rank = sorted(range(len(ratings)), key=lambda k: ratings[k], reverse=reverse_or_not)
        return ratings, doc_rank
