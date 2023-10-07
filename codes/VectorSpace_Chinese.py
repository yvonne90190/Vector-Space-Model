import sys
import math
import util

try:
    import numpy as np
    import jieba
except:
    print("Error: Requires numpy from https://numpy.org/install/. Have you installed?")
    print("Error: Requires jieba from https://github.com/fxsjy/jieba/. Have you installed?")
    sys.exit() 

jieba.set_dictionary('dict.txt.big')

class VectorSpace:
    #Collection of document term vectors (tf vector -> tfidf vector)
    tfVectors = []
    #idf Vector
    idfVector = []
    #tfidf Vector
    tfidfVector = []
    #Mapping of vector index to keyword
    vectorKeywordIndex=[]
    #stopwords
    stopwords = []

    def __init__(self, documents=[]):
        self.tfVectors=[]
        if(len(documents)>0):
            self.build(documents)

    def build(self, documents):
        """ Create the vector space for the passed document strings """      
        self.stopwords = open('../stopwords/cn_stopwords.txt', 'r')
        self.stopwords = self.stopwords.read().split()
        self.vectorKeywordIndex = self.getVectorKeywordIndex(documents)
        self.tfVectors = [self.makeVector(document) for document in documents]
        self.idfVector = self.makeIdfVector(documents)
        self.tfidfVectors = self.makeTfidfVectors(self.tfVectors)  # convert tfVectors (tf vector) into tfidf vector
    
    def tokenise(self, string):
        string = [v for v in jieba.cut(string, cut_all=False)]
        return string
        
    def removeStopWords(self, List):
        List = [word for word in List if word not in self.stopwords]
        return List
    
    def getVectorKeywordIndex(self, documentList):
        """ create the keyword associated to the position of the elements within the document vectors """
        #Mapped documents into a single word string	
        vocabularyString = "".join(documentList)
        vocabularyString = self.tokenise(vocabularyString)
        vocabularyString = self.removeStopWords(vocabularyString)
        uniqueVocabularyList = util.removeDuplicates(vocabularyString)
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
        wordList = self.tokenise(wordString)
        wordList = self.removeStopWords(wordList)
        for word in wordList:
            try:
                vector[self.vectorKeywordIndex[word]] += 1; #Use simple Term Count Model
            except:
                continue
        return vector

    def makeIdfVector(self, documents):
        vector = [0] * len(self.vectorKeywordIndex)
        for document in documents:
            wordList = self.tokenise(document)
            wordList = self.removeStopWords(wordList)
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
        """ convert query string into a tidf vector """
        query = self.makeVector(" ".join(termList))
        query_tfidf = self.makeTfidfVectors(query)
        return query_tfidf

    def cosineSimilarity(self,searchList):
        """ search for documents that match based on a list of terms """
        queryVector = self.buildQuerytfidfVector(searchList)
        ratings = [0] * len(self.vectorKeywordIndex)
        ratings = util.consineSimilarity(self.tfidfVectors, queryVector)
        doc_rank = sorted(range(len(ratings)), key=lambda k: ratings[k], reverse=True)
        return ratings, doc_rank