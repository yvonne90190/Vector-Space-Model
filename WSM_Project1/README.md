# WSM Project 1: Ranking by Vector Space Models

## Directory Tree
```
── WSM_Project1 
    ├── README.md
    ├── codes
    │   ├── Parser.py
    │   ├── PorterStemmer.py
    │   ├── ReadPrint.py
    │   ├── VectorSpace_Chinese.py
    │   ├── VectorSpace_English.py
    │   ├── dict.txt.big
    │   ├── main_Chinese.py
    │   ├── main_English.py
    │   ├── main_Evaluation.py
    │   ├── util.py
    |   └── __pycache__
    ├── dataSets
    │   ├── ChineseNews
    │   ├── EnglishNews
    │   └── smaller_dataset
    │       ├── collections
    │       ├── queries
    │       └── rel.tsv
    └── stopwords
        ├── EnglishStopwords.txt
        └── cn_stopwords.txt
```

## Usage
1. Please put corpus file under directory *"dataSets"*. For example, put *"ChineseNews"* under "dataSets"
2. Go to directory *"codes"*
```
cd codes
```
3. Q1 & Q2 : Use python3 to run the program, then insert a query
```
python3 main_English.py  
Taiwan Youtube COVID-19
```
4. Q3 : Use python3 to run the program, then insert a query
```
python3 main_Chinese.py
烏克蘭 大選
```
5. Q4 : Use python3 to run the program, and wait for the result
```
python3 main_Evaluation.py
```


## Description
### Q1 : Vector Space Model with Different Weighting Schemes & Similarity Metrics (Please DON'T use any off-the-shelf packages or functions)
Rank the Documents according to the Similarity scores.  

I develop a retrieval program that is able to retrieve the relevant news to the given query from a set of 8,000 English News collected from reuters.com according to different weighting schemes and similarity metrics. In the given dataset, each file is named by its News ID and contains the corresponding news title and content, as shown in below:  

Below are some steps in the codes:  
1. Stemming & Removing Stop Words (English Stop Words); & Indexing
2. Transfer Queries into a Vector
3. Transfer Documents into Vectors
4. Calculate the Similarity between the Query Vector and the Document Vectors  

### Q2 : Relevance Feedback
Relevance Feedback is an IR technique for improving retrieved results. The simplest approach is Pseudo Feedback, the idea of which is to feed the results retrieved by the given query, and then to use the content of the fed results as supplement queries to re-score the documents.

In this work, I use the Nouns and the Verbs within the first document of the above **Method 1** (e.g. TF-IDF Weighting + Cosine Similarity ) for Pseudo Feedback. The new query term weighting scheme is **[1 * original query + 0.5 * feedback query]**. Please try to use the new query to re-rank the documents.

For instance, suppose the index vector is ["network", "computer", "share", "ask", "soccer", "song"], the query is "network", and the content of the feedback document is:

**Jimmy shares songs via the computer network.**
Then it result in a new query vector like this:

**1 * [1, 0, 0, 0, 0, 0] + 0.5 * [1, 1, 1, 0, 0, 1] = [1.5, 0.5, 0.5, 0, 0, 0.5]**

Here is an example result for the query "Youtube Taiwan COVID-19" in Q1 and Q2:
```
yvonne@APNB8IH:/mnt/c/Users/Yvonne/Desktop/WSM_Project1/codes$ python3 main_English.py
Query: Taiwan Youtube COVID-19
TF-IDF Weighting + Cosine Similarity:
NewsID          score
News1240.txt    0.401259616112328
News2230.txt    0.31250740180281755
News1679.txt    0.30185530550918077
News668.txt     0.2941385404635579
News2401.txt    0.23880906231175728
News623.txt     0.2361227203051997
News796.txt     0.21449136009881573
News820.txt     0.2115604421553403
News447.txt     0.19738758807912685
News2050.txt    0.18560401923813633
==================================================
TF-IDF Weighting + Euclidean Distance:
NewsID          score
News2925.txt    14.134438165044562
News1830.txt    14.380952644111517
News2424.txt    14.621545959844639
News68.txt      15.127943862524896
News2401.txt    15.194231513664816
News1516.txt    15.262773103523134
News100.txt     15.31720589300909
News1061.txt    15.431442391195404
News1497.txt    15.43915216923247
News1592.txt    15.568640088712291
==================================================
TF-IDF Weighting + Relevance Feedback:
NewsID          score
News1240.txt    0.9352865361242683
News2230.txt    0.38034021327702816
News1679.txt    0.35563753095212064
News668.txt     0.34867072291267726
News623.txt     0.30806547716690663
News2401.txt    0.2767983138882255
News820.txt     0.26861481050246283
News796.txt     0.2548435823460667
News447.txt     0.2356408013065766
News2050.txt    0.22390969982680858
```
### Q3 : Vector Space Model with Different Scheme & Similarity Metrics in Chinese and English
In this part, I retrieve the relevant news to the query from a set of 2,000 Chinese News collected from chinatimes.com and setn.com according to different weighting schemes (TF and TF-IDF) and cosine similarity metric.
I use Jieba or to split the Chinese word segments.

Here is the example result of the query "烏克蘭 大選":
```
yvonne@APNB8IH:/mnt/c/Users/Yvonne/Desktop/WSM_Project1/codes$ python3 main_Chinese.py
Query: 烏克蘭 大選
Building prefix dict from /mnt/c/Users/Yvonne/Desktop/WSM_Project1/codes/dict.txt.big ...
Loading model from cache /tmp/jieba.u4ad1628c067c24c20ac8d281daedc1a7.cache
Loading model cost 1.205 seconds.
Prefix dict has been built successfully.
TF-IDF Weighting + Cosine Similarity:
NewsID          score
News200049.txt  0.1612062668849048
News200892.txt  0.15234352869124823
News200053.txt  0.13843129794029096
News200847.txt  0.13321720718128047
News200135.txt  0.1279983036523605
News200137.txt  0.12790430924329405
News200007.txt  0.1250505372166102
News200056.txt  0.12475501236352618
News200081.txt  0.12214259781822105
News200071.txt  0.12099087277644432 
```
### Q4 : Evaluation IR system
In this part, I focus another [smaller dataset](https://wm5.nccu.edu.tw/base/10001/course/10026264/content/proj01/smaller_dataset.zip), which have 1460 documents, 76 queries and their labelled relevant documents.  
I implement the following metrics on this dataset: Recall@10, MAP@10, MRR@10, by using vector space model and trying some NLP technique e.g. stemming, remove stop word.  
  
Here is the example result :
```
yvonne@APNB8IH:/mnt/c/Users/Yvonne/Desktop/WSM_Project1/codes$ python3 main_Evaluation.py
tdidf retrieve ...
--------------------------------------------------
tfidf   MRR@10           0.3275235314642428
tfidf   MAP@10           0.26562813283208014
tfidf   RECALL@10        0.1463903386660504
--------------------------------------------------
```
