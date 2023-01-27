# **WSM Project 2: Building IR systems based on the Lemur Project**

In this project I implement several different retrieval methods, i.e. algorithms that given a user's request (query) and a corpus of documents assign a score to each document according to its relevance to the query. Some of these retrieval methods will be the implementation of the basic retrieval models studied in the class (e.g. TF-IDF, BM25, Language Models with different Smoothing). I use the toolkits of Lemur Project, which includes search engines, browser toolbars, text analysis tools, and data resources that support research and development of information retrieval and text mining. I heavily read its wiki, [Lemur Project](http://www.lemurproject.org/) and [Indri Search Engine Wiki](http://sourceforge.net/p/lemur/wiki/Home/), in order to understand how to use the toolkits.  

## Document Corpus  
Use WT2g, a 2GB corpus of Web documents to test my algorithms, and run my experiments. ([Here](http://ir.dcs.gla.ac.uk/test_collections/wt10g.html) are details about the corpus (WT10g instead), in case you are interested.) 

For the corpus, I construct two indexes, (a) with stemming, and (b) without stemming. Both indexes contain stopwords. For stemming, I can use the porter (Porter) stemmer. Below is an example of index information:
<table>
  <tr>
    <td>IndexID</td>
    <td>Index Description</td>
    <td>Statistics</td>
  </tr>
  <tr>
    <td>0</td>
    <td>WT2G with stemming</td>
    <td>terms=   261,742,791 unique_terms=   1,391,908 docs=   247,491</td>
  </tr>
  <tr>
    <td>1</td>
    <td>WT2G without stemming</td>
    <td>terms=   261,742,791 unique_terms=   1,526,004 docs=   247,491</td>
  </tr>
</table>
  
## Queries  
[Here](https://wm5.nccu.edu.tw/base/10001/course/10026264/content/proj02/topics.401-450.txt) is a set of 50 TREC queries for the corpus, with the standard TREC format having topic title, description and narrative. Documents from the corpus have been judged with respect to their relevance to these queries by NIST assessors.

## Ranking Functions
The task is to run the set of queries against the WT2g collection, return a ranked list of documents (the top 1000) in a particular format, and the evaluate the ranked lists.  
  
Implement the following variations of a retrieval system:  

1. Vector space model, terms weighted by Okapi TF (see note) times an IDF value, and inner product similarity between vectors.  
Note: I use for the weights OKAPI TF x IDF where OKAPI TF = tf/(tf + 0.5 + 1.5 * doclen / avgdoclen). For queries, Okapi TF can also be computed in the same way, just use the length of the query to replace doclen.  
  
     Also note that the definition of OKAPI TF is tf / tf + k1((1 - b) + b * doclen / avgdoclen). In the above formula, I set k1 = 2 and b = 0.75, to end up with: tf / (tf + 0.5 + 1.5 * doclen / avgdoclen).  
  
2. Language modeling, maximum likelihood estimates with Laplace smoothing only, query likelihood.  
Note: If you use multinomial model, for every document, only the probabilities associated with terms in the query must be estimated because the others are missing from the query-likelihood formula (please refer to our slides).  

    For model estimation use maximum-likelihood and Laplace smoothing. Use formula (for term i)  
    $$p_i = {m_i+1 \over n+k}$$
  
    where m = term frequency, n=number of terms in document (doc length) , k=number of unique terms in corpus.  

3. Language modeling, Jelinek-Mercer smoothing using the corpus, 0.8 of the weight attached to the background probability, query likelihood.  
  
    The formula for Jelinek-Mercer smoothing is,  
 
    $$p_i = {\lambda P + (1-\lambda) Q}$$

    where P is the estimated probability from document $$(max likelihood = m_i/n)$$ and Q is the estimated probability from corpus (background probability = cf / terms in the corpus).

4. Improve one of the above three IR models. Improve the rank quality of the chosen IR models, and explain and showcase why my modifications can work in my report [ _WSM_Project2.pdf_](https://www.dropbox.com/s/1kscu4zbpo8zp54/WSM_Project2.pdf?dl=0)
