from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import routes
from routes import initialize_routes
from resources.db import initialize_db

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'e9b36f610670449c7eb8180eea083588'

CORS(app)

initialize_db(app)
initialize_routes(api)

@app.route('/')
def show_app():
    return routes.initialize_routes()

# app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)