# **** Vector Space Model ****
# ***Directory Tree***
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

# ***Usage***
## (1) Please put corpus file under directory *"dataSets"*
#### For example, put *"ChineseNews"* under "dataSets"

## (2) Go to directory *"codes"*
#### **cd codes**
## (3) Q1 & Q2 : Use python3 to run the program, then insert a query
#### **python3 main_English.py**
#### **Taiwan Youtube COVID-19**
## (4) Q3 : Use python3 to run the program, then insert a query**
#### **python3 main_Chinese.py**
#### **烏克蘭 大選**
## (5) Q4 : Use python3 to run the program, and wait for the result
#### **python3 main_Evaluation.py**

#
# ***Example***
## **(Q1 & Q2)**
### I try datasets (EnglishNews) with only News1.txt ~ News3000.txt due to computer memory limit
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
## **(Q3)**
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
## **(Q4)**
```
yvonne@APNB8IH:/mnt/c/Users/Yvonne/Desktop/WSM_Project1/codes$ python3 main_Evaluation.py
tdidf retrieve ...
--------------------------------------------------
tfidf   MRR@10           0.3275235314642428
tfidf   MAP@10           0.26562813283208014
tfidf   RECALL@10        0.1463903386660504
--------------------------------------------------
```
