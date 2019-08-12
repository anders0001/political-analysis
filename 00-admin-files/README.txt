-------------------------- IDEA -------------------------------------
CURRENT POLITICAL DISCUSSION
- Rezo Video: How relevant is this?
- How many people use Youtube as source of information?
- How powerful are Youtubers (i.e. Rezo) today?

PROBLEM
- Lack of transparency in the political realm
- Lots of "fake news" flying through the internet
- No real website exists that is the "standard" of internet sentiment

RESULT
- Number of Youtube videos watched in Germany in last 30 days by political sentiment
	- Rank videos according to political sentiment
	- Check and/or rank by comments & views


------------------- DATA EXTRACTION -------------------------
Youtube-API Key (pass it with key=API_KEY parameter)
AIzaSyCH-RbXxD4FCvj7PIclUqKErL0EkxzBmwk


#START: Extract youtube-page
	#Extract information
		#Number of views
		#Number of comments
	#Save information to postgreSQL
	#Extract links
	#Filter links according to relevancy

FEATURES: 
YT-Video-ID / Title / # View / # Likes / # Comments / Tags / Transcript

    title = []
    videoId = []
    viewCount = []
    likeCount = []
    commentCount = []
    tags = []

#SCRAPE LOOP:
	#Repeat process until limit is reached

#TASKS
	#Get transcripts of videos (via subtitles?!)
	#Check API call limit without API key
	#Find language recognition library

- Named Entity Recognition 
	- Tags > 
	- Implementation:
		- Spacy Tokenizer > Named Entities (understand sentence structure)
		-  
- Sentiment Analysis 
	- positive or negative
	- Vader ()

-------------- TOOLS USED --------------------------------------------------
Google's Developer Console 			For access to Youtube to get song data
Youtube-Transcript-API				https://pypi.org/project/youtube-transcript-api/ > to get transcripts
PSQL (postgres)
Metabase
5