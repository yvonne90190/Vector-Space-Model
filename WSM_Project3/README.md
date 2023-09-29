# WSM Final Project: OTTO – Multi-Objective Recommender System 2022
## Introduction
I team up with my WSM classmates and participate in a e-commerce recommendation competition hosted by OTTO on the OTTO Kaggle Challenge website.  
The goal of this competition is to predict e-commerce clicks, cart additions, and orders. We build three multi-objective recommender system based on previous events in a user session.  

## Dataset
OTTO releases a public dataset of 12M real-world anonymized user sessions, and the primitive dataset is available at [OTTO Kaggle Challenge homepage](https://www.kaggle.com/competitions/otto-recommender-system).  

## Implementation
Our team implement following retrieval models: 
1) Vector Space Model (VSM)
2) Word2Vec Model
3) XGBranker
We also ensemble the models to get a higher score.

I also try to implement Language Modeling(LM), BM25, JM-smoothing, and  adopt some Machine Learning toolkits to learn the judgement during the process using scikit-learn. 

## Report
The report provide the descriptions of what we did and some analysis of what we learned including:
- The scores for our selected runs.
- The analysis of our proposed solutions.
- How we organize our team work? (up to 10 points).
- What advanced Machine Learning techniques we use from Natural Language Processing research fields such as Word Embedding.
- Data Visualizations for data analysis or performance results.
