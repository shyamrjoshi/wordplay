from flask import Flask
from flask_restful import Api
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



if __name__ == '__main__':
    app.run()
