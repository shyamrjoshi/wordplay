# wordplay
Wordplay is a Flask Restful API which can be used to learn English words


#Project Goals

Design and implement a restful API that enables users to perform the following actions:
•User provides 2 or more words to the server, and the server randomly returns 1 word
•User provides 1 English word, and server returns a list of English words that rhyme with that word 
•User provides 1 English word, and server returns a detail description of that word including Synonyms,
 Antonyms,pronunciation, frequency and example sentences.

#Project Description

The project is developed with an idea of using this API as an aid to people learning english language.
An english language learning application can be built on using this API.

The application has 3 main functionality.
1. User provides a list of 2 or more words and the API returns a random word from the 
   specified input word list. This functionality can be used to recall tough words and remember them.
2. User provides 1 english word and the API returns words that rhyme with that input word.
   This helps user to learn rhyming words.
3. User provides 1 english word and the API returns detail information about that input word.
   The API returns the definition, Synonyms, Antonyms, Pronunciation, Frequency and Example Sentences for 
   that input word. 
   This help user to learn new words and get information about a word. User can learn the meaning,
   Synonyms, Antonyms and Pronunciation. It also gives the frequency of the word used in english language over the years
   using which user can focus more on words that have high frequency. It also provides 5 example sentences for the input 
   word which gives user a sense of various usage of the word in the english language.

Since the first two goals of the project are related to english words, the third endpoint was selected 
related to words. This decision was made to make a complete linked endpoints. The first two endpoint were 
missing a functionality where user can get detail information about a word. Hence the third endpoint gives 
a detail information about a word. User can use this endpoint to learn words and get information.

 
The project is developed using Flask framework in python 3.0. 
Flask-RESTful library is used to develop resftful api's.
The flask application runs on localhost and is not hosted on a server.
The application has 4 endpoints. These endpoints are as follows
1. http://localhost:5000    
   GET Request
   access the API root

2. http://localhost:5000/words/1.0/random
   POST Request
   randomWords endpoint. Returns a random word from the input word list

3. http://localhost:5000/words/1.0/rhyme/<string:word>
   GET Request
   rhymeWords endpoint. Returns rhyming words for the input word

4. http://localhost:5000/words/1.0/info/<string:word>
   GET Request
   infoWords endpoint. Return detail information about the input word

   
All the endpoints are protected with Basic Authentication.
credentials are relpek:puorg

#API Endpoint details

1. http://localhost:5000    
   GET Request
   access the API root
   argument: None
   Returns a string "Welcome to Word Play"
   
   code file is placed under resources named rootwords.py


2. http://localhost:5000/words/1.0/random
   POST Request
   randomWords endpoint. 
   Only POST request is supported. 
   arguments : "words" Mandatory argument
   Returns a random word from the input word list
   
   Request Content-Type is application/json
	Request body format is
	{
	"words":[list of words]
	}

	Response format is
	{
	"words": "random word"
	}
	   
	code file is placed under resources named randomwords.py
	

3. http://localhost:5000/words/1.0/rhyme/<string:word>
   GET Request
   rhymeWords endpoint. 
   Only GET Request is supported. 
   argument : "word" Mandatory argument
   Returns rhyming words for the input word
   
   Request Content-Type is application/json
   Request Format is
   User passes the word as a part of the GET request URL.
   The word is passed after /rhyme/. The input is stored in
   word variable. There should only be 1 term in the input else 
   server would raise a bad request error (http 400).

	Response Format is
	{
	  "rhyme": [List of rhyming words]
	}

	Error Response format is
	{
	"code": Error Code,
	"message": "Error Message"
	}
	
	The rhyming words are found using the cmu pronouncing dictionary.
	python pronouncing 0.1.5 library is used as an interfacce for the
	cmu pronouncing dictionary. 

	API returns a success response (http 200) if no	rhyming words are
	found for the input word. In this case the response contains empty
	list for the key rhyme.
	
	code file is placed under resources named rhymewords.py
	
4. http://localhost:5000/words/1.0/info/<string:word>
   GET Request
   infoWords endpoint. 
   Only GET Request is supported. 
   argument : "word" Mandatory argument
   Return detail information about the input word
   
   Request Content-Type is application/json
   Request Format is
   User passes the word as a part of the GET request URL.
   The word is passed after /info/. The input is stored in
   word variable. There should only be 1 term in the input else 
   server would raise a bad request error (http 400).
	Response Format is
	{
	  "word": {
		"frequency": "frequency of the word usage over the years",
		"defination": "{"part of speech": definition}",
		"pronounciation": "pronounciation of the word",
		"synonyms": "[list of synonyms]"
		"antonyms": "[list of antonyms]"
		"examples": "{"S.no": 5 example sentences}",
	  }
	}

	Error Response format is
	{
	"code": Error Code,
	"message": "Error Message"
	}
	
	Python PyDictionary is used for fetching the meaning, synonyms 
	and antonyms of the input word.
	CMU pronouncing dictionary is used to get the pronounciation of
	the input word.
	http://api.wordnik.com:80/v4/word.json/{word}/frequency wordnik API
	is used to fetch the frequency of the input word.
	http://api.wordnik.com:80/v4/word.json/{word}/examples wordnik API
	is used to fetch the examples for the input word.
	
	The response fields are None/Empty, if API is unable to find the 
	respective fields for the input word. In this case the response is 
	success(http 200) and would contain None/Empty fields.
	
	code file is placed under resources named infowords.py
	
	
#Testing

Python unittest library is used to do unit testing of the API.
All test files are places inside the tests folder
The file apitestwords.py contains the code for unit testing this API.
it has 11 test cases. execute this file to run unittesting.
 

#Sample Example Requests

1. GET Request to rootWords endpoint
   curl -i --user relpek:puorg -H "Content-Type: application/json" -X GET http://localhost:5000
   
   Response
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
		100    23  100    23    0     0    105      0 --:--:-- --:--:-- --:--:--   113HTTP/1.0 200 OK
		Content-Type: application/json
		Content-Length: 23
		Server: Werkzeug/0.12.2 Python/3.5.1
		

		"Welcome to Word Play"


2. POST Request to randomWords endpoint
   curl -i --user relpek:puorg -H "Content-Type: application/json" -X POST -d '{"words":["abject","conduit", "exigent", "modicum","portent"]}' http://localhost:5000/words/1.0/random
	
   Response
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
		100    83  100    21  100    62     89    263 --:--:-- --:--:-- --:--:--   283HTTP/1.0 200 OK
		Content-Type: application/json
		Content-Length: 21
		Server: Werkzeug/0.12.2 Python/3.5.1
		

		{"words": "exigent"}
		
3. GET Request to rhymeWords endpoint
   curl -i --user relpek:puorg -H "Content-Type: application/json" -X GET http://localhost:5000/words/1.0/rhyme/climbing
	
   Response
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
		100    66  100    66    0     0    301      0 --:--:-- --:--:-- --:--:--   301HTTP/1.0 200 OK
		Content-Type: application/json
		Content-Length: 66
		Server: Werkzeug/0.12.2 Python/3.5.1
		

		{"rhyme": "['diming', 'liming', 'priming', 'rhyming', 'timing']"}
		
4. GET Request to infoWords endpoint
   curl -i --user relpek:puorg -H "Content-Type: application/json" -X GET http://localhost:5000/words/1.0/info/abject
   
   Response
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
		100  1266  100  1266    0     0    658      0  0:00:01  0:00:01 --:--:--   664HTTP/1.0 200 OK
		Content-Type: application/json
		Content-Length: 1266
		Server: Werkzeug/0.12.2 Python/3.5.1
		

		{"abject": {"frequency": "629", "defination": "{'Adjective': ['of the most contemptible kind', 'most unfortunate or miserable', 'showing utter resignation or hopelessness', 'showing humiliation or submissiveness']}", "antonyms": "['commendable', 'exalted', 'excellent', 'magnificent', 'worthy']", "examples": "{1: 'Segregation still exists in the media, in the movies and the TV shows, where the abject is absented, where there is the default and the deviant, the \"normal\" and the \"abnormal\".', 2: 'And the last thing they want is someone to get injured by what he referred to as abject stupidity, anybody coming out.', 3: 'A true scientist should aim to finish life in abject loneliness and poverty.', 4: 'But, even before Christmas, the lack of fresh vegetables caused scurvy to break out, and disappointed adventurer after disappointed adventurer took to his bunk in abject surrender to this culminating misfortune.', 5: 'The dogs sat on their chairs in abject silence with Davis and his wife menacing them to remain silent, while, in front of the curtain, Dick and Daisy Bell delighted the matinee audience with their singing and dancing.'}", "pronounciation": "AE1 B JH EH0 K T", "synonyms": "['wretched', 'base', 'contemptible', 'degraded', 'dejected']"}}


#Setup

1. clone files from https://github.com/shyamrjoshi/wordplay

2. install python 3.5.2
3. install pip
4. install requirements from requirements.txt
5. run the application, python run.py


To execute test cases. run python apitestwords.py 


#Files

The project structure is as follows

app 								#flask app
	__init__.py 					#code File which contains the flask app
	
resources 							#contains code for endpoints
	infowords.py 					#code file for infoWords endpoint
	randomwords.py 					#code file for randomWords endpoint
	rhymewords.py 					#code file for rhymeWords endpoint
	rootwords.py 					#code file for rootWords endpoint
	
tests 								#files required for testing
	longest_english_word.txt 		#longest english word

apitestwords.py						#Code file containing unittests
config.py							#configuration file
requirements.txt					#crequirements.txt file
run.py								#Code file to execute the application


#Things to do

1. Improve authentication by adding oAuth 2.0 authentication.
2. Add Pagination and Filters to the endpoints.
3. Improve accuracy of identifying the word.
4. Identify language specific words.
5. Include support for multiple word search.


#Assumptions

1. The words entered by user are consider English words. For the words that
   do not exists in the python dictionary empty response is returned. Endpoint 
   currently does not identify language of the input words.
2. randomWords endpoint retuns a random word for the input word list. It simply
   returns the word and does not check for valid words. Hence it will return any 
   random input string words
3. For large requests the server will reply with HTTP 413 if the payload is 
   to large for the server to handle. Similarily server will reply with HTTP 429
   if too many requests are send that cannot be handled by the server.


#References

1. https://flask-restful.readthedocs.io/en/0.3.5/
2. http://developer.wordnik.com/docs.html
3. https://docs.python.org/2/library/unittest.html

