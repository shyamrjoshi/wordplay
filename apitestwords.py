"""
This file contains Unittest cases for the words API.

"""
from base64 import b64encode

from app import app
import unittest
import ast
import json


class wordsapitest(unittest.TestCase):
    """
    This class contains the methods for unit testing the
    words API

    """

    def setUp(self):
        """
        function for setup instructions
        reference the words api client
        :return: None
        """
        self.app = app.test_client()
        self.headers = {
            'Content-Type':'application/json',
            'Authorization': 'Basic %s' % b64encode(b"relpek:puorg").decode("ascii")
        }
    def root(self):
        """
        function to get response from root
        :return: String
        """
        return self.app.get('/',headers=self.headers)

    def randomWords(self, input_word):
        """
        Function to get response from randomWords endpoint
        :param input_word: dict
        :return: dict
        """
        input_word = json.dumps(input_word)
        return self.app.post('/words/1.0/random', data=input_word, follow_redirects=True,headers=self.headers)

    def rhymeWords(self, input_word):
        """
        Function to get response from rhymeWords endpoint
        :param input_word: String
        :return: dict
        """
        return self.app.get('/words/1.0/rhyme/' + input_word, follow_redirects=True, headers=self.headers)

    def wordInfo(self, input_word):
        """
        Function to get response from wordsInfo endpoint
        :param input_word: String
        :return: dict
        """
        return self.app.get('/words/1.0/info/' + input_word, follow_redirects=True, headers=self.headers)

    def test_root(self):
        """
         function to test response for root
        :return: None
        """
        rv = self.root()
        self.assertEquals(rv.status_code, 200)
        self.assertIn('Welcome to Word Play', rv.get_data(as_text=True))

    def test_random_words(self):
        """
        function to test randomWords endpoint for list of words
        :return: None
        """
        input_word_list = {"words": ["word1", "word2", "word3"]}
        rv = self.randomWords(input_word=input_word_list)
        response_data = json.loads(rv.get_data(as_text=True))
        self.assertEquals(rv.status_code, 200)
        self.assertIn(response_data["words"], input_word_list["words"])

    def test_rhyme_words(self):
        """
        function to test rhymeWords endpoint for 1 word
        :return: None
        """
        input_word_list = "climbing"
        expected_output_list = {"rhyme": ["diming", "liming", "priming", "rhyming", "timing"]}
        rv = self.rhymeWords(input_word=input_word_list)
        response_data = json.loads(rv.get_data(as_text=True))
        self.assertEquals(rv.status_code, 200)
        self.assertEquals(set(ast.literal_eval(response_data["rhyme"])), set(expected_output_list["rhyme"]))

    def test_empty(self):
        """
        function to test randomWords endpoint for empty request.
        :return: None
        """
        input_word_list = []
        expected_output_list = []
        rv = self.randomWords(input_word=input_word_list)
        # self.assertEquals(set(response_data),set(expected_output_list) )
        self.assertEquals(rv.status_code, 400)

    def test_long_list_words(self):
        """
        function to test randomWords endpoint for a long list of words
        :return: None
        """
        input_word_list = {
            "words": ["word1", "word2", "word3", "diming", "liming", "priming", "rhyming", "timing", "absurd", "alward",
                      "bird", "blurred", "all", "antol", "appall", "aul", "aull", "bacall", "ball", "baseball", "bawl",
                      "befall", "brawl", "caul", "crall", "crawl", "dall", "daul", "depaul", "drawl", "edsall",
                      "engwall", "enthral", "fairall", "fall", "faul", "faull", "forestall", "gall", "gaul", "gaulle",
                      "grall", "graul", "hall", "haul", "install", "kall", "kaul", "krall", "krol", "kroll", "lall",
                      "lol", "luminol", "mall", "maul", "maule", "maull", "mccall", "mccaul", "mcfall", "mcfaul",
                      "mcnall", "mcphaul", "mehall", "metall", "mol", "montreal", "nall", "nepal", "pall", "paul",
                      "paule", "paull", "peterpaul", "pol", "prall", "rall", "raul", "rawl", "recall", "sabol", "sall",
                      "saul", "babar", "bahr", "bahre", "balakumar", "baldemar", "baltazar", "bar", "bargar", "barr",
                      "barre", "bashar", "bazaar", "bazar", "bejar", "belvoir", "bizarre", "bizarre", "bodnar", "bogar",
                      "bognar", "bomar", "bondar", "bonior", "boyar", "car", "carr", "carre", "ceasar", "cigar",
                      "cisar", "claar", "clar", "cotnoir", "cousar", "csar", "csaszar", "czar", "d'ivoire", "dakar",
                      "dar", "dardar", "darr", "delamar", "delebarre", "demar", "detar", "dinar", "disbar", "dzhokhar",
                      "dzokhar", "emdr", "fahr", "far", "farquar", "farr", "farrar", "ferrar", "flohr", "foobar",
                      "gaar", "gahr", "gar", "ghafar", "giroir", "giscard", "godar", "gohr", "gombar", "gregoire",
                      "guitar", "guizar", "haar", "hajjar", "hamar", "har", "hekmatyar", "hocevar", "hribar", "hribar",
                      "huizar", "jabar", "jabbar", "jaffar", "jahr", "jamar", "jar", "jiar", "kadar", "kahr", "kahre",
                      "karr", "kjar", "kjar", "klar", "kumar", "labar", "lahr", "lamar", "lamarr", "lamarre", "lar",
                      "lebar", "lemar", "lemarr", "maher", "mahr", "mar",
                      "marr", "mawr", "mcgarr", "meagher", "melgar", "menjivar", "minnaar", "myanmar", "najar",
                      "najjar", "navar", "navarre", "nazar", "npr", "o'barr", "obar", "obarr", "our", "paar", "paccar",
                      "par", "parr", "pfarr", "phar", "pharr", "pickar", "pintar", "preslar", "qasr", "qatar", "quarre",
                      "r", "r.", "rajkumar", "renoir", "revoir", "ribar", "robar", "saar", "sagar", "saldivar",
                      "saldovar", "sar", "scar", "schaar", "schar", "scharr", "shahar",
                      "sharar", "sharrar", "sitar", "skaar", "sklar", "soutar", "spahr", "spar", "sphar", "spohr",
                      "staar", "star", "starr", "subpar", "superstar", "tabar", "tar", "tarr", "tatar", "tesar", "thar",
                      "tokar", "tovar", "transtar", "tsar", "tsar", "ulaanbaatar", "valdemar", "victoire", "voir",
                      "wor", "wor", "yahr", "zachar", "zadar", "zagar", "zalar", "zaldivar", "zarre", "zulfikar",
                      "stall", "tall", "taul", "thall", "thrall", "tol", "vandall", "vanhall", "vantol", "wahle", "wal",
                      "wall", "walle", "burd", "byrd", "chauffeured", "concurred", "conferred", "curd", "deferred",
                      "demurred", "deterred", "ferd", "gerd", "gird", "gjerde", "heard", "herd", "hird", "hurd",
                      "incurred", "inferred", "interred", "jerde", "kurd", "leard", "misheard", "nerd", "occurred",
                      "one-third", "overheard", "prefered", "preferred", "preferred", "preferred", "recurred",
                      "referred", "referred", "reword", "slurred", "spurred", "stirred", "third", "transfered",
                      "transferred", "uncured", "undeterred", "unheard"]}
        rv = self.randomWords(input_word=input_word_list)
        response_data = json.loads(rv.get_data(as_text=True))
        self.assertEquals(rv.status_code, 200)
        self.assertIn(response_data["words"], input_word_list["words"])

    def test_word_info(self):
        """
        function to test wordInfo endpoint for 1 word
        :return: None
        """
        word = "vitality"
        rv = self.wordInfo(input_word=word)
        expected_output = {
            word: {
                "frequency": "975",
                "defination": "{'Noun': ['an energetic style', 'a healthy capacity for vigorous activity', '(biology', 'not physical or chemical', 'the property of being able to survive and grow']}",
                "antonyms": "['enervation', 'inactivity', 'lethargy', 'weakness', 'lack']",
                "examples": "{1: 'And finally, both Lord Robertson and Secretary of State Powell pointed to what they called the vitality and the relevance of NATO, and said any damage done to the reputation of NATO over the last couple weeks can quite, in their words, be easily overcome.', 2: \"Professor Huxley himself has told us that he lived in 'the hope and the faith that in course of time we shall see our way from the constituents of the protoplasm to its properties,' _i. e._ from carbonic acid, water, and ammonia to that mysterious thing which we call vitality or life -- from the molecular motion of the brain to Socratic wisdom,\", 3: 'The strongest, the most amply endowed with what we call vitality or power to live, win.', 4: 'But the thought that it is mechanics and chemistry applied by something of which they as such, form no part, some agent or principle which we call vitality, is welcome to us.', 5: '\"The Indian savages,\" said Margrave, sullenly, \"have not a health as perfect as mine, and in what you call vitality -- the blissful consciousness of life -- they are as sticks and stones compared to me.\"'}",
                "pronounciation": "V AY0 T AE1 L AH0 T IY0",
                "synonyms": "['vigor', 'continuity', 'spunk', 'strength', 'verve']"
            }
        }
        response_data = json.loads(rv.get_data(as_text=True))

        self.assertEquals(rv.status_code, 200)
        self.assertEquals(response_data[word]["defination"], expected_output[word]["defination"])
        self.assertEquals(response_data[word]["antonyms"], expected_output[word]["antonyms"])
        self.assertEquals(response_data[word]["examples"], expected_output[word]["examples"])
        self.assertEquals(response_data[word]["frequency"], expected_output[word]["frequency"])
        self.assertEquals(response_data[word]["pronounciation"], expected_output[word]["pronounciation"])
        self.assertEquals(response_data[word]["synonyms"], expected_output[word]["synonyms"])

    def test_word_info_bad_request(self):
        """
        function to test wordInfo endpoint for a bad request.
        input more than 1 word
        :return: None
        """
        word = "defination of vitality "
        rv = self.wordInfo(input_word=word)
        expected_output = {
            "code": 400,
            "message": "A Term must be only a single word"
        }
        response_data = json.loads(rv.get_data(as_text=True))

        self.assertEquals(rv.status_code, 400)
        self.assertEquals(response_data["code"], expected_output["code"])
        self.assertEquals(response_data["message"], expected_output["message"])

    def test_word_rhyme_bad_request(self):
        """
        function to test wordRhyme endpoint for a bad request.
        input more than 1 word
        :return: None
        """
        word = "Not a single Term "
        rv = self.rhymeWords(input_word=word)
        expected_output = {
            "code": 400,
            "message": "A Term must be only a single word"
        }
        response_data = json.loads(rv.get_data(as_text=True))

        self.assertEquals(rv.status_code, 400)
        self.assertEquals(response_data["code"], expected_output["code"])
        self.assertEquals(response_data["message"], expected_output["message"])

    def test_word_info_bad_word(self):
        """
        function to test wordInfo endpoint for a
        garbage input word
        :return: None
        """
        word = "hdiasudhisuahdiasushdiaushdiaushdiasuhdisauh"
        rv = self.wordInfo(input_word=word)
        expected_output = {
            word: {
                "frequency": None,
                "defination": None,
                "antonyms": None,
                "examples": None,
                "pronounciation": None,
                "synonyms": None
            }
        }
        response_data = json.loads(rv.get_data(as_text=True))

        self.assertEquals(rv.status_code, 200)
        self.assertEquals(response_data[word]["defination"], expected_output[word]["defination"])
        self.assertEquals(response_data[word]["antonyms"], expected_output[word]["antonyms"])
        self.assertEquals(response_data[word]["examples"], expected_output[word]["examples"])
        self.assertEquals(response_data[word]["frequency"], expected_output[word]["frequency"])
        self.assertEquals(response_data[word]["pronounciation"], expected_output[word]["pronounciation"])
        self.assertEquals(response_data[word]["synonyms"], expected_output[word]["synonyms"])

    def test_word_info_longest_word(self):
        """
        function to test wordInfo endpoint with the longest english
        word pass as input
        :return: None
        """
        file = open("tests/longest_english_word.txt")
        if file:
            word = file.readline()
            rv = self.wordInfo(input_word=word)
            expected_output = {
                word: {
                    "frequency": None,
                    "defination": None,
                    "antonyms": None,
                    "examples": None,
                    "pronounciation": None,
                    "synonyms": None
                }
            }
            response_data = json.loads(rv.get_data(as_text=True))
            self.assertEquals(rv.status_code, 200)
            for key, value in response_data.items():
                self.assertEquals(response_data[key]["defination"], expected_output[word]["defination"])
                self.assertEquals(response_data[key]["antonyms"], expected_output[word]["antonyms"])
                self.assertEquals(response_data[key]["examples"], expected_output[word]["examples"])
                self.assertEquals(response_data[key]["frequency"], expected_output[word]["frequency"])
                self.assertEquals(response_data[key]["pronounciation"], expected_output[word]["pronounciation"])
                self.assertEquals(response_data[key]["synonyms"], expected_output[word]["synonyms"])

    def test_word_rhyme_longest_word(self):
        """
        function to test wordRhyme endpoint with the longest
        english word pass as input
        :return: None
        """
        file = open("tests/longest_english_word.txt")
        if file:
            word = file.readline()
            rv = self.rhymeWords(input_word=word)
            expected_output = {
                "rhyme": "[]"
            }
            response_data = json.loads(rv.get_data(as_text=True))
            self.assertEquals(rv.status_code, 200)
            self.assertEquals(response_data["rhyme"], expected_output["rhyme"])


if __name__ == '__main__':
    unittest.main()
