from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class milk(Resource):
    # def get(self):
        # return {"name":"HALLO WARLD"}
    
    def get(self, name):
        return {f"is {name} GAY????":True}



api.add_resource(milk, "/gaychecker/<string:name>/")

if __name__ == "__main__":
    app.run(debug=True)