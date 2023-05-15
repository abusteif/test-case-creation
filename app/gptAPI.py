import json

import openai

from app.configs import json_marker
from app.local_configs import gpt_api_key
from app.utilities import json_to_html_list


class GptAPI:

    def __init__(self, model="gpt-3.5-turbo"):
        openai.api_key = gpt_api_key
        self.model = model
        self.session = None
        self.conversation = None

    def create_user_prompt(self, message):
        prompt = {
            "role": "user",
            "content": message
        }
        self.conversation.append(prompt)
        return prompt

    def generate_response(self, return_text=True):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.conversation
        )
        self.conversation.append(
            {
                "role": "assistant",
                "content": response.choices[0].message.content
            }
        )
        print(response)
        return response.choices[0].message.content if return_text else response

    def create_session(self, app_description, scenario):
        first_message = 'You will be my assistant. I want you to write test cases for an application I am testing. ' \
                        'Here is a quick description of what the app does: ' + app_description + \
                        'I will be describing the functionality of each page of the app in my subsequent requests, ' \
                        'and you will create test cases. ' \
                        'Return the test steps in the a JSON format. For example:' \
                        '{"testCases": [{"number":"<test case number>", "name":"<testCaseName>", "objective":"Test ' \
                        'case objective", "priority": "<priority>", "steps":[{"step": "Enter text into the Username field", ' \
                        '"expectedBehaviour": "Text entered successfully"}]}]}. Use the keyword ' + json_marker + \
                        ' to mark the start of the JSON data. Generate multiple test cases.' \
                        'Here is the first scenario:' + scenario

        self.conversation = [
            {
                "role": "user",
                "content": first_message
            }
        ]

        return json.loads(self.generate_response().split(json_marker)[1].replace("\n", ""))


    def add_functionality(self, description):
        # self.create_user_prompt(description)
        # response = self.generate_response(True)
        # return response
        # response = response.split(json_marker)[1]
        # print(response)
        # self.create_user_prompt("Create edge test cases. Append them to the existing list. Follow the same format outlined in the initial message. "
        #                         "That is, the usage of !!*!! to mark the start of the JSON data as well as"
        #                         "the JSON format agreed upon")
        # response = self.create_edge_cases()
        # return json_to_html_list(response)

        # return response
        return

    def create_edge_cases(self):
        self.create_user_prompt("Create edge test cases. Follow the same format outlined in the initial message. "
                                "That is, the usage of  to mark the start of the JSON data as well as"
                                "the JSON format agreed upon. For test case number, start from where you left"
                                "off in the previous set of test cases")
        return self.generate_response(True).split(json_marker)[1]

