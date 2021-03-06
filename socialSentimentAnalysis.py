!pip install vaderSentiment

import pandas as pd
import numpy as np
import io 
import requests
import re

#import libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Upload and read file
uploaded = files.upload()

#Take tweet text and put into list
tweet_list = df.text

#Import top ten Tech Stocks
topTenTech = ["AAPL", "GOOG", "MSFT", "FB", "ibm", "AMZN", "ATT", "CSCO", "intel", "vz"]

#vader object
sid_obj = SentimentIntensityAnalyzer()

#for each tech company name, find which tweets have their names and append into local list, 
#then run sentiment analysis and print out sentiment score for each list
for i in range(len(topTenTech)):
  tempEval = []
  total_neg =0
  total_compound=0
  total_sentences =0
  total_positive =0
  total_neutral = 0
  for z in range(len(tweet_list)):
    if(topTenTech[i].lower() in tweet_list[z]):
      tempEval.append(tweet_list[z])
  for item in tempEval:
    sentiment_dict = sid_obj.polarity_scores(item)
    total_compound = total_compound + sentiment_dict['compound']
    total_neg = total_neg + sentiment_dict['neg']
    total_positive = total_positive + sentiment_dict[ 'pos']
    total_neutral = total_neutral + sentiment_dict['neu']
    total_sentences = len(tempEval)
  if total_sentences == 0:
    total_sentences = 1
  print("Sentiment Analysis for " + topTenTech[i] + ": ")
  print("total_compound ", total_compound)
  print("total_neg ", total_neg/ total_sentences)
  print("total_positive ", total_positive/ total_sentences)
  print("total_neutral ", total_neutral/ total_sentences)
  print("Final Sentiment Score ", total_compound / total_sentences)
  print("------------------------------------------")


#data set citation
#Bruno Taborda, Ana de Almeida, José Carlos Dias, Fernando Batista, Ricardo Ribeiro. (2021). "Stock Market Tweets Data." Web.
