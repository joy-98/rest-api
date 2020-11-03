from flask import Flask, redirect, url_for, render_template
from flask_restful import Api, Resource
from questions import algebra

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return render_template("index.html")

def A_math_question():
        return {"photo": "44", "topic": 55, "reason":"have fun"}	        

names = {"q1": algebra.find_x_angel_in_qualdrilateral()}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
