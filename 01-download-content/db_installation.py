from sqlalchemy import create_engine
import json

con = create_engine("postgresql://localhost:5432/political-analysis")
	
con.execute('''DROP TABLE IF EXISTS video_data''')
con.execute('''CREATE TABLE video_data (
				INDEX INT,
				TITLE VARCHAR(255),
				VIDEO_ID TEXT, 
				VIEWCOUNT INT,
				COMMENTCOUNT INT,
				LIKECOUNT INT,
				TAGS TEXT,
				TRANSCRIPT TEXT);
			''')

print("Table successfully created.")