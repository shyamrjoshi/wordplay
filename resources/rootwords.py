"""
This file contains the code for the root resource.
Use Get method to call this endpoint. GET http://hostname
returns a string "Welcome to Word Play"
"""

from flask_restful import Resource


class root(Resource):
    def get(self):
        """
        Get method for resource root. Accessed by
        http://hostname
        :return: String
        """
        return "Welcome to Word Play"
