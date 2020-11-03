from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def A_math_question():
        return {"photo": "44", "topic": 55, "reason":"have fun"}	        

names = {"tim": {"age": 22, "gender": "male"},	
         "bill": {"age": 20, "gender": "male"},	       
         "question": A_math_question()}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
