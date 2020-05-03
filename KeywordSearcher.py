import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


class KeywordSearcher():
    def __init__(self):
        # read json into a dataframe. Training data for other recipes
        self.df_idf=pd.read_json("data/recipes.json",lines=False)
        self.df_idf['text'] = self.df_idf['title'] + self.df_idf['body']
        self.df_idf['text'] = self.df_idf['text'].apply(lambda x: self.pre_process(x))

        #load a set of stop words
        self.stopwords=self.get_stop_words("resources/stopwords.txt")

        #get the text column    
        self.docs=self.df_idf['text'].tolist()

        #create a vocabulary of words, 
        #ignore words that appear in 85% of documents, 
        #eliminate stop words
        self.cv=CountVectorizer(max_df=0.85,stop_words=self.stopwords, max_features=100000)
        self.word_count_vector=self.cv.fit_transform(self.docs)

        # you only needs to do this once
        self.feature_names=self.cv.get_feature_names()

   
    def pre_process(self,text):
        # lowercase
        text=text.lower()
        #remove tags
        text=re.sub("</?.*?>"," <> ",text)
        # remove special characters and digits
        text=re.sub("(\\d|\\W)+"," ",text)
        return text
        
    def get_stop_words(self,stop_file_path):
        #load stop words 
        with open(stop_file_path, 'r', encoding="utf-8") as f:
            stopwords = f.readlines()
            stop_set = set(m.strip() for m in stopwords)
            return frozenset(stop_set)

    def sort_coo(self,coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

    def extract_topn_from_vector(self,feature_names, sorted_items, topn=10):
        """get the feature names and tf-idf score of top n items"""
        
        #use only topn items from vector
        sorted_items = sorted_items[:topn]

        score_vals = []
        feature_vals = []

        for idx, score in sorted_items:
            fname = feature_names[idx]
            
            #keep track of feature name and its corresponding score
            score_vals.append(round(score, 3))
            feature_vals.append(feature_names[idx])

        #create a tuples of feature,score
        #results = zip(feature_vals,score_vals)
        results= {}
        for idx in range(len(feature_vals)):
            results[feature_vals[idx]]=score_vals[idx]
        
        return results

        

    def getKeywords(self, title, body, keywordCount = 10):
        tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
        tfidf_transformer.fit(self.word_count_vector)
        
        # read test docs into a dataframe and concatenate title and body
        df_test=pd.DataFrame([{ "title": title, "body": body }])
        df_test['text'] = df_test['title'] + df_test['body']
        df_test['text'] = df_test['text'].apply(lambda x:self.pre_process(x))

        # get test docs into a list
        docs_test=df_test['text'].tolist()
        docs_title=df_test['title'].tolist()
        docs_body=df_test['body'].tolist()

        #generate tf-idf for the given document. 0 is because we only want one.
        tf_idf_vector=tfidf_transformer.transform(self.cv.transform([docs_test[0]]))

        #sort the tf-idf vectors by descending order of scores
        sorted_items=self.sort_coo(tf_idf_vector.tocoo())

        #extract only the top n; n here is 10
        keywords=self.extract_topn_from_vector(self.feature_names,sorted_items,keywordCount)
    
        return keywords.keys()

        


