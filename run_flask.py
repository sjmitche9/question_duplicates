# import Flask and jsonify
from flask import Flask, jsonify, request

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

import os
# import functions

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
	def post(self):
		question1 = json_retrieved['q1']
		question2 = json_retrieved['q2']
		label = int(json_retrieved['label'])
		result = check_similarity(question1, question2, label)
		message = f"Probability of duplicate: {round(result[1] * 100, 2)}%"
		lst = [result, message]
		return jsonify(lst)

api.add_resource(Predict, '/predict', methods=['POST'])

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=5555)