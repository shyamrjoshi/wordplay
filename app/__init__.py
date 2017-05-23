"""Main app
This flask application provides 4 restful API. These Endpoints can be
used to develop an english learning application.

The API enables users to perform the following actions:
User provides 2 or more words to the server, and the server randomly returns 1 word
User provides 1 English word, and server returns a list of English words that rhyme with that word.
User provides 1 English word, and server returns a detail description of that word including Synonyms,
 Antonyms,pronunciation, frequency and example sentences.

Refer Readme.txt for API Documentation
"""

from flask import Flask
from flask_restful import Api
from resources.randomwords import randomWords
from resources.rhymewords import rhymeWords
from resources.infowords import wordInfo
from resources.rootwords import root
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'relpek'
app.config['BASIC_AUTH_PASSWORD'] = 'puorg'
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

api = Api(app)

# endpoint for the app root
api.add_resource(root, '/', endpoint='rootWords')

# endpoint for getting random word
api.add_resource(randomWords, '/words/1.0/random', endpoint='randomWords')

# endpoint for fetching rhyming words
api.add_resource(rhymeWords, '/words/1.0/rhyme/<string:word>', endpoint='rhymeWords')

# endpoint for getting information about a word
api.add_resource(wordInfo, '/words/1.0/info/<string:word>', endpoint='infoWords')

