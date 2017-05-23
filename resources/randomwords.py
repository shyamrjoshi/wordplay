"""
This file contains the code for the randomWords endpoint.
User provides 2 or more words to the server, and the server
randomly returns 1 word

Endpoint : http://hostname/words/random
This endpoint only supports POST Requests.
Request Content-Type is application/json
Request format is
{
"words":[list of words]
}

Response format is
{
"words": "random word"
}

"""

from flask_restful import Resource, reqparse, marshal, fields
import random

response_fields = {
    'words': fields.String
}


class randomWords(Resource):
    def __init__(self):
        """
        Initialize the arguments. The Request must contains the
        'words' argument.
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('words', type=list, required=True,
                                   help='No words provided',
                                   location='json')
        super(randomWords, self).__init__()

    def post(self):
        """
        Function to handle the post request to randomWords endpoint.
        function reads the 'words' argument from the request
        and returns a response which contains a randomly selected word
        from the list of input words.

        :return: dict
        """
        args = self.reqparse.parse_args()
        # choose a random word from the input word list
        random_word = random.choice(args['words'])
        response = {
            "words": random_word
        }
        return marshal(response, response_fields), 200
