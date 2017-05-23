"""
This file contains the code for the rhymeWords endpoint.
User provides 1 English word, and server returns a list of
English words that rhyme with that word.

Endpoint : http://hostname/words/rhyme/<string:word>
This endpoint only supports GET Request.
Request Content-Type is application/json
Request Format is
User passes the word as a part of the GET request URL.

Response Format is
{
  "rhyme": [List of rhyming words]
}

Error Response format is
{
"code": Error Code,
"message": "Error Message"
}

"""

import pronouncing
from flask_restful import Resource, reqparse, marshal, fields

response_rhyme_fields = {
    'rhyme': fields.String
}


class rhymeWords(Resource):
    def __init__(self):
        """
        Initialize the arguments. The Request must contains the
        'word' argument.
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('word', type=str, required=True,
                                   help='No word provided',
                                   location='json')
        super(rhymeWords, self).__init__()

    def check_input_no_of_words(self, word):
        """
        Check for no of words in the input string.
        Return True if no of words equal to 1. else return False
        :param word: String
        :return: Boolean
        """
        if len(word.split()) == 1:
            return True
        else:
            return False

    def get(self, word):
        """
        Function to handle get request to rhymeWords endpoint.
        returns a reponse containing the rhyming words for
        the input word.
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
                # find rhyming words using the pronouncing library
                word = word.lower()
                rhyme_list = pronouncing.rhymes(word)

                response = {
                    'rhyme': rhyme_list
                }

                return marshal(response, response_rhyme_fields), 200

            except Exception as e:  # Error occurred while finding rhyme words
                response = {"code": 500,
                            "message": e.value}
                return response, 500
        else:  # Empty string passed as input
            response = {"code": 400,
                        "message": "Empty Word list"
                        }
            return response, 400
