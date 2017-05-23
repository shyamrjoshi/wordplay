"""
This file contains the code for the wordInfo endpoint.
User provides 1 English word, and server returns a detail
description of that word including Synonyms, Antonyms,
Pronunciation, Frequency and Example Sentences.

Endpoint : http://hostname/words/info/<string:word>
This endpoint only supports GET Request.
Request Content-Type is application/json
Request Format is
User passes the word as a part of the GET request URL.

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

"""

from PyDictionary import PyDictionary
import pronouncing
import requests
from flask_restful import Resource, reqparse, marshal, fields

response_rhyme_fields = {
    "defination": fields.String,
    "synonyms": fields.String,
    "antonyms": fields.String,
    "pronounciation": fields.String,
    "frequency": fields.String,
    "examples": fields.String
}


class wordInfo(Resource):
    def __init__(self):
        """
        Initialize the arguments. The Request must contains the
        'word' argument.
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('word', type=str, required=True,
                                   help='No word provided',
                                   location='json')
        super(wordInfo, self).__init__()

    def check_input_no_of_words(self, word):
        """
        Check for no of words in the input string.
        Return True if no of words equal to 1. else return False
        :param word: String
        :return: Boolean
        """
        if len(word.split()) > 1:
            return False
        else:
            return True

    def get_word_frequency(self, word):
        """
        Get the frequency of the given word.
        Frequency is fetched from https://www.wordnik.com/
        GET http://api.wordnik.com:80/v4/word.json/{word}/frequency
        Returns word usage over time from 1800 to present
        wordnik public api key, found on their website, is used to
        access their API
        :param word: String
        :return: String
        """

        # sending a get request to wordnik frequency endpoint and
        # returning the frequency of the input word
        try:
            header = {"Content-Type": "application/json; charset=utf-8"}
            req = requests.get(
                "http://api.wordnik.com:80/v4/word.json/" + word + "/frequency?useCanonical=false&startYear=1800&endYear=2012&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5",
                headers=header)
            if req.status_code == 200:
                response_data = req.json()
                return response_data["totalCount"]
        except Exception as e:
            return

    def get_word_example(self, word):
        """
        Get 5 example sentences for the input word.
        Examples are fetched from https://www.wordnik.com/
        GET http://api.wordnik.com:80/v4/word.json/{word}/examples
        Returns examples for a word
        wordnik public api key, found on their website, is used to
        access their API
        :param word: String
        :return: dict
        """

        # sending a get request to wordnik example endpoint and
        # returning the 5 examples of the input word
        try:
            header = {"Content-Type": "application/json; charset=utf-8"}
            req = requests.get(
                "http://api.wordnik.com:80/v4/word.json/" + word + "/examples?includeDuplicates=false&useCanonical=false&skip=0&limit=5&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5",
                headers=header)

            if req.status_code == 200:
                response_data = req.json()
                example = {}
                i = 0
                for element in response_data["examples"]:
                    i = i + 1
                    example[i] = element["text"]

                return example
        except Exception as e:
            return

    def get(self, word):
        """
        Function to handle get request to wordInfo endpoint.
        returns a response containing the detail information about
        the input word. Response contains definition, pronunciation,
        synonyms, antonyms, frequency and examples.
        :param word: String
        :return: dict
        """

        # check if word exists.
        if word:
            # check if more than 1 word is provided as input.
            # return error if more than 1 word
            word = word.strip()
            word_check = self.check_input_no_of_words(word)
            if not word_check:
                response = {"code": 400,
                            "message": "A Term must be only a single word"
                            }
                return response, 400
            try:
                # convert the input to lower case and
                # get the word from the PyDictionary
                word = word.lower()
                word_dict = PyDictionary(word)

            # raise error is PyDictionary failed to find the word
            except Exception as e:
                response = {
                    "code": 400,
                    "error": e.val
                }
                return response, 400

            # fetching the word meaning
            try:
                if word_dict.meaning(word):
                    defination = word_dict.getMeanings()[word]
                else:
                    defination = None
            except Exception as e:
                defination = None

            # fetching the Synonyms for input word
            if word_dict.getSynonyms()[0]:
                synonyms = word_dict.getSynonyms()[0][word]
            else:
                synonyms = None

            # fetching the antonyms for input word
            if word_dict.getAntonyms()[0]:
                antonyms = word_dict.getAntonyms()[0][word]
            else:
                antonyms = None

            # fetching the pronunciation for input word
            if pronouncing.phones_for_word(word):
                pronounciation = pronouncing.phones_for_word(word)[0]
            else:
                pronounciation = None

            # fetching the frequency for the input word
            frequency = self.get_word_frequency(word)

            # fetching examples for the input word
            examples = self.get_word_example(word)

            # create and return the response
            word_r = {
                "defination": defination,
                "synonyms": synonyms,
                "antonyms": antonyms,
                "pronounciation": pronounciation,
                "frequency": frequency,
                "examples": examples
            }
            return {word: marshal(word_r, response_rhyme_fields)}, 200
        else:  # raise error if empty string pass as input
            response = {"code": 400,
                        "message": "Empty Word list"
                        }
            return response, 400
