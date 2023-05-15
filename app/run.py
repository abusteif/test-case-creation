from flask import Flask, request
from flask_restful import Resource, Api

from app.gptAPI import GptAPI
from app.utilities import json_to_html_list

app = Flask(__name__)
api = Api(app)


class AppDetails(Resource):
    def post(self):
        data = request.get_json()

        scenario = data.get("firstScenario")
        app_description = data.get("appDescription")

        scenario = 'when user logs in, the first screen they see will depend on the ' \
                   'number of matters they have. if they have only one matter, they will be taken directly ' \
                   'to the matter\'s Timeline view. If the user has multiple matters, ' \
                   'they will see a list of matters grouped by firm name. In addition, ' \
                   'there should be a search function that allows the user to search for ' \
                   'matters. If a matter has a pending to-do items, it should be displayed on ' \
                   'that specific matter\'s item. When user clicks on the matter, they will be ' \
                   'taken to the Timeline viewed associated with this matter. Matters are sorted ' \
                   'chronologically. User can scroll down when the matters can\'t fit all on the screen'

        app_description = 'The app is called LawConnect mobile app. It allows user to view and, depending on the item' \
                          'type, comment on items shared by lawyers. Some examples of items that can be shared are: ' \
                          'documents, invoices, statements.'

        gpt_object = GptAPI()
        return gpt_object.create_session(app_description, scenario)

        # process the data


api.add_resource(AppDetails, '/app-details')

# class EdgeTestCases(Resource):
#     def get(self):
#         # Logic to retrieve user with given ID goes here
#         return {'user_id': user_id, 'name': 'John Doe'}


# @app.route('/')
# def hello_world():
#
#     gpt_object = GptAPI()
#     gpt_object.create_session()
#
#     return gpt_object.add_functionality("when user logs in, the first screen they see will depend on the number of "
#                                         "matters they have. if they have only one matter, they will be taken directly "
#                                         "to the matter's Timeline view. If the user has multiple matters, "
#                                         "they will see a list of matters grouped by firm name. In addition, "
#                                         "there should be a search function that allows the user to search for "
#                                         "matters. If a matter has a pending to-do items, it should be displayed on "
#                                         "that specific matter's item. When user clicks on the matter, they will be "
#                                         "taken to the Timeline viewed associated with this matter. Matters are sorted "
#                                         "chronologically. User can scroll down when the matters can't fit all on the "
#                                         "screen")


if __name__ == "__main__":
    app.run(debug=True)
