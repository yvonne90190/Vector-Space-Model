# **WSM Project 2: Building IR systems based on the Lemur Project**

In this project I implement several different retrieval methods, (e.g. TF-IDF, BM25, Language Models with different Smoothing).
by use thing toolkits of [Lemur Project](http://www.lemurproject.org/) and [Indri Search Engine](http://sourceforge.net/p/lemur/wiki/Home/)

i.e. algorithms that given a user's request (query) and a corpus of documents assign a score to each document according to its relevance to the query. 

## Document Corpus  
Use WT2g, a 2GB corpus of Web documents to test my algorithms, and run my experiments. ([Here](http://ir.dcs.gla.ac.uk/test_collections/wt10g.html) are details about the corpus (WT10g instead)) 

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
The task is to run the set of queries against the WT2g collection, return a ranked list of documents (the top 1000) in a particular format, and then evaluate the ranked lists.  

1. Vector space model, terms weighted by OKAPI TF x IDF, and inner product similarity between vectors.  
Note I set :
- OKAPI TF = tf / tf + k1((1 - b) + b * doclen / avgdoclen) for documents.
- OKAPI TF = tf / tf + k1((1 - b) + b * doclen / avgdoclen) for queries.
- And set k1 = 2 and b = 0.75, ending up with: tf / (tf + 0.5 + 1.5 * doclen / avgdoclen).  
  
3. Language modeling, maximum likelihood estimates with Laplace smoothing only, query likelihood.  
Note: As I use multinomial model, for every document, only the probabilities associated with terms in the query must be estimated because the others are missing from the query-likelihood formula.  

    Formula (for term i):
    $$p_i = {m_i+1 \over n+k}$$
    where m = term frequency, n=number of terms in document (doc length) , k=number of unique terms in corpus.  

5. Language modeling, Jelinek-Mercer smoothing using the corpus, 0.8 of the weight attached to the background probability, query likelihood.  
  
    Formula:  
    $$p_i = {\lambda P + (1-\lambda) Q}$$
    where P is the estimated probability from document $$(max likelihood = m_i/n)$$ and Q is the estimated probability from corpus (background probability = cf / terms in the corpus).

6. Improve one of the above three IR models. Improve the rank quality of the chosen IR models, and explain and showcase why my modifications can work in my report [ _WSM_Project2.pdf_](https://www.dropbox.com/s/1kscu4zbpo8zp54/WSM_Project2.pdf?dl=0)


## Evaluation
Run all 50 queries and return at top 1,000 documents for each query, except scores that equal to zero. If there are only N<1000 documents with non-zero scores then only return these N documents.

Save the 50 ranked lists of documents in a single file. Each line in the file having the following format:
*query-number Q0 document-id rank score Exp*
where query-number is the number of the query (i.e., 401 to 450), document-id is the _external_ ID for the retrieved document, rank is the rank of the corresponding document in the returned ranked list (1 is the best and 1000 is the worst; break the ties either arbitrarily or lexicographically), and score is the score that my ranking function outputs for the document. Scores should descend while rank increases. "Q0" (Q zero) and "Exp" are constants that are used by some evaluation software. The overall file should be sorted by ascending rank (so descending score) within ascending query-number.  
  
To evaluate a single run (i.e. a single file containing 50,000 lines or less), first download the qrel file ([here](https://wm5.nccu.edu.tw/base/10001/course/10026264/content/proj02/qrels.401-450.txt) is the qrel file for the WT2g corpus. Then, use evaluation tool (ireval.jar) in Lemur Toolkit or download the script of [trec_eval.pl](https://wm5.nccu.edu.tw/base/10001/course/10026264/content/proj02/trec_eval.pl) and run:  
  
*perl trec_eval.pl [-q] qrel_file results_file*  
  
(The -q option outputs evaluation metrics values for each query; the average overall queries will be returned if -q is not used). 

trec_eval provides a number of statistics about how well the retrieval function corresponding to the results_file did on the corresponding queries and includes average precision, precision at various recall cut-offs. I use some of those statistics for this project's report.  
  
## EXAMPLE  
I ran the okapi tf-idf model on query "401. foreign minorities, germany" for the WT2g collection (with stemming), without doing any fancy query processing (just word tokenization).  
  
Below is the statistics I got back by running trec-eval on the results for this query:  
```
Queryid (Num):      401
Total number of documents over all queries
    Retrieved:     1000
    Relevant:        45
    Rel_ret:         42
Interpolated Recall - Precision Averages:
    at 0.00       1.0000
    at 0.10       0.4375
    at 0.20       0.3250
    at 0.30       0.3182
    at 0.40       0.2769
    at 0.50       0.2604
    at 0.60       0.2366
    at 0.70       0.2361
    at 0.80       0.2209
    at 0.90       0.0586
    at 1.00       0.0000
Average precision (non-interpolated) for all rel docs(averaged over queries)
                  0.2605
Precision:
  At    5 docs:   0.4000
  At   10 docs:   0.4000
  At   15 docs:   0.4000
  At   20 docs:   0.3500
  At   30 docs:   0.3000
  At  100 docs:   0.2500
  At  200 docs:   0.1850
  At  500 docs:   0.0800
  At 1000 docs:   0.0420
R-Precision (precision after R (= num_rel for a query) docs retrieved):
    Exact:        0.3111
```
## Paper Report
[ _WSM_Project2.pdf_](https://www.dropbox.com/s/1kscu4zbpo8zp54/WSM_Project2.pdf?dl=0) provide a short description of what I did and some analysis of what you learned. 

Including :  
1. Un-interpolated mean average precision numbers for all 8 runs.
2. Precision at rank 10 documents for all 8 runs.
3. An analysis of the advantages or disadvantages of stemming, IDF, and the different smoothing techniques.
