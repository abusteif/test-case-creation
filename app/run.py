from flask import Flask, request
from flask_restful import Resource, Api

from app.gptAPI import GptAPI
from app.utilities import json_to_html_list

app = Flask(__name__)
api = Api(app)


class InitialQuery(Resource):
    def post(self):
        data = request.get_json()

        scenario = data.get("firstScenario")
        app_description = data.get("appDescription")

        gpt_object = GptAPI()
        gpt_object.create_session()

        return gpt_object.add_functionality("when user logs in, the first screen they see will depend on the number of "
                                            "matters they have. if they have only one matter, they will be taken directly "
                                            "to the matter's Timeline view. If the user has multiple matters, "
                                            "they will see a list of matters grouped by firm name. In addition, "
                                            "there should be a search function that allows the user to search for "
                                            "matters. If a matter has a pending to-do items, it should be displayed on "
                                            "that specific matter's item. When user clicks on the matter, they will be "
                                            "taken to the Timeline viewed associated with this matter. Matters are sorted "
                                            "chronologically. User can scroll down when the matters can't fit all on the "
                                            "screen")

        # process the data
        return {'message': 'Data received', 'data': data}, 200


class EdgeTestCases(Resource):
    def get(self):
        # Logic to retrieve user with given ID goes here
        return {'user_id': user_id, 'name': 'John Doe'}

@app.route('/')
def hello_world():
    # content = "!!*!!\n{\n \"number\": \"TC001\",\n \"name\":\"Login and view matters\",\n \"objective\":\"Ensure user can login and view matters correctly\",\n \"steps\":[\n    {\n        \"step\":\"Enter valid credentials and click on login button\",\n        \"expectedBehaviour\":\"User should be logged in successfully\"\n    },\n    {\n        \"step\":\"Identify the number of matters available for user\",\n        \"expectedBehaviour\":\"If only one matter available, user should be redirected to that matter's Timeline view, otherwise user should see a list of matters grouped by firm name\"\n    },\n    {\n        \"step\":\"Click on search bar and enter search keyword\",\n        \"expectedBehaviour\":\"Matters should be filtered according to the search keyword\"\n    },\n    {\n        \"step\":\"Identify matters with pending to-do items\",\n        \"expectedBehaviour\":\"The specific matter with the pending to-do items should display it on the matter's item\"\n    },\n    {\n        \"step\":\"Scroll through the list of matters\",\n        \"expectedBehaviour\":\"User should be able to scroll down freely to view all available matters\"\n    },\n    {\n        \"step\":\"Click on a matter\",\n        \"expectedBehaviour\":\"User should be taken to the Timeline view associated with that matter\"\n    },\n    {\n        \"step\":\"Verify the chronological sorting of matters\",\n        \"expectedBehaviour\":\"Matters should be sorted chronologically and displayed in the correct order\"\n    }\n ]\n},\n{\n \"number\": \"TC002\",\n \"name\":\"Login with invalid credentials\",\n \"objective\":\"Ensure user can't login with invalid credentials\",\n \"steps\":[\n    {\n        \"step\":\"Enter invalid credentials and click on login button\",\n        \"expectedBehaviour\":\"User should not be logged in and should receive an appropriate error message\"\n    }\n ]\n},\n{\n \"number\": \"TC003\",\n \"name\":\"View matters with no to-do items\",\n \"objective\":\"Ensure user can view matters with no to-do items correctly\",\n \"steps\":[\n    {\n        \"step\":\"Enter valid credentials and click on login button\",\n        \"expectedBehaviour\":\"User should be logged in successfully\"\n    },\n    {\n        \"step\":\"Identify the number of matters available for user\",\n        \"expectedBehaviour\":\"If only one matter available, user should be redirected to that matter's Timeline view, otherwise user should see a list of matters grouped by firm name\"\n    },\n    {\n        \"step\":\"Verify all matters have no to-do items\",\n        \"expectedBehaviour\":\"No indication of pending to-do items should be displayed for any matter\"\n    },\n    {\n        \"step\":\"Scroll through the list of matters\",\n        \"expectedBehaviour\":\"User should be able to scroll down freely to view all available matters\"\n    },\n    {\n        \"step\":\"Click on a matter\",\n        \"expectedBehaviour\":\"User should be taken to the Timeline view associated with that matter\"\n    },\n    {\n        \"step\":\"Verify the Timeline view\",\n        \"expectedBehaviour\":\"The Timeline view should be displayed correctly without any to-do items\"\n    }\n ]\n},\n{\n \"number\": \"TC004\",\n \"name\":\"View matters offline\",\n \"objective\":\"Ensure user can view matters when offline\",\n \"steps\":[\n    {\n        \"step\":\"Go offline\",\n        \"expectedBehaviour\":\"User should not be able to access the app\"\n    },\n    {\n        \"step\":\"Launch app\",\n        \"expectedBehaviour\":\"App should display an appropriate error message indicating it requires internet connection to function properly\"\n    },\n    {\n        \"step\":\"Go back online\",\n        \"expectedBehaviour\":\"User should be able to access the app\"\n    }\n ]\n}\n!!*!!"
    # content = content.split("!!*!!")[1]
    # content = '{"testCases":[' + content + ']}'
    # return json_to_html_list(content)
    # return "ok"
    gpt_object = GptAPI()
    gpt_object.create_session()

    return gpt_object.add_functionality("when user logs in, the first screen they see will depend on the number of "
                                        "matters they have. if they have only one matter, they will be taken directly "
                                        "to the matter's Timeline view. If the user has multiple matters, "
                                        "they will see a list of matters grouped by firm name. In addition, "
                                        "there should be a search function that allows the user to search for "
                                        "matters. If a matter has a pending to-do items, it should be displayed on "
                                        "that specific matter's item. When user clicks on the matter, they will be "
                                        "taken to the Timeline viewed associated with this matter. Matters are sorted "
                                        "chronologically. User can scroll down when the matters can't fit all on the "
                                        "screen")


if __name__ == "__main__":
    app.run(debug=True)
