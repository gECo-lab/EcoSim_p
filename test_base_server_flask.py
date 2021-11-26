from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import pdb


########
# Data #
########

simulation_status = {'iteration': '1', 'end': '0'}

#######
# APP #
#######

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET', 'POST'])
def home():

	global simulation_status

	if request.method == 'POST':

		# pdb.set_trace()

		simulation_status = {**request.get_json()}		

	return simulation_status


#############
# Resources #
#############


class StatusItem(Resource):

	parser = reqparse.RequestParser()

	parser.add_argument('iteration', type=str, location='json')

	parser.add_argument('end', type=str, location='json')

	def get(self):

		global simulation_status

		return simulation_status, 200

	def post(self):

		global simulation_status

		# args = StatusItem.parser.parse_args()

		# pdb.set_trace()

		# simulation_status['iteration'] = args['iteration']

		# simulation_status['end'] = args['end']

		simulation_status = {**request.get_json()}

		return simulation_status, 200


api.add_resource(StatusItem, '/status')

if __name__ == '__main__':
	app.run('127.0.0.1', '5000', debug=True)
