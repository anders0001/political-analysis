from sqlalchemy import create_engine
import pandas as pd 


engine 		= create_engine("postgresql://localhost:5432/political-analysis")


transcript 	= engine.execute(
			'''SELECT transcript FROM video_data
			;''')

print(list(transcript)[0][0])

#for row in transcript:
#	print(row)







'''
USING VADER
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser 	= SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))
'''