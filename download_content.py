from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd 
import json
from sqlalchemy import create_engine


#Setup Environment & Variables
API_KEY				= "AIzaSyAhYyZhCyQ2jAuu_0f8YmgC2-SLf-6gvy0"
youtube				= build('youtube', 'v3', developerKey=API_KEY)
video_ids 			= []
title 				= []
viewCount 			= []
likeCount 			= []
commentCount 		= []
tags 				= []
transcript 			= []

#Run Query on YouTube and extract Top 10 results of videos sorted by Views and save them as 'video_ids'
search_results = youtube.search().list(	part='id', 
										q='Politik Deutschland', 
										maxResults= 10, 
										type='video',
										order='viewCount').execute()
print("Search completed.")

for i in range(10):
	video_ids.append(str(search_results['items'][i]['id']['videoId']))

print(video_ids)


#Loop through video ids and download relevant video data
for i in range(10):

	try:
		#Download video_id data
		results_song_data = youtube.videos().list(id=i, part='id,snippet,statistics').execute()
		results_transcript = YouTubeTranscriptApi.get_transcript(i)

		#Extract data from JSON to strings:
		title.append(results_song_data['items'][0]['snippet']['title'])
		viewCount.append(results_song_data['items'][0]['statistics']['viewCount'])
		likeCount.append(results_song_data['items'][0]['statistics']['likeCount'])
		commentCount.append(results_song_data['items'][0]['statistics']['commentCount'])
		tags.append(results_song_data['items'][0]['snippet']['tags'])

		for text_part in results_transcript:
			transcript.append(text_part['text'])

		transcript_filtered = ' '.join(transcript)

		json_data 	= {	'video_id': i, 
						'title': title[0], 
						'viewcount': int(viewCount[0]),
						'commentcount': int(likeCount[0]),
						'likecount': int(commentCount[0]),
						'tags': ','.join(tags[0]),
						'transcript': ' '.join(transcript)
						}

		#Create JSON file from dictionary
		#with open('downloaded_content/data_download_1.json', 'w') as json_file:
		#	json.dump(json_dictionary, json_file)


		#Convert data to DF and then insert into SQL
		df = pd.DataFrame.from_dict(json_data,orient='index').transpose()
		engine = create_engine("postgresql://localhost:5432/political-analysis")
		df.to_sql('video_data', con=engine, if_exists='append')

	except:
		print('Data from one video could not be retrieved.')