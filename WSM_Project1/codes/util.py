import math
import sys

#http://www.scipy.org/
try:
	import numpy as np
	from numpy import dot
	from numpy.linalg import norm
except:
	print("Error: Requires numpy from http://www.scipy.org/. Have you installed scipy?")
	sys.exit() 

def removeDuplicates(list):
	""" remove duplicates from a list """
	return set((item for item in list))

def consineSimilarity(vector1, vector2):
	cos_vec = np.dot(vector1,vector2)/(norm(vector1, axis=1)*norm(vector2))
	return cos_vec

def EuclideanDistance(vector1, vector2):
    return float(math.dist(vector1, vector2))

