import openai

from app.utilities import json_to_html_list


class GptAPI:

    def __init__(self, model="gpt-3.5-turbo"):
        openai.api_key = "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"
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

    def generate_response(self):
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
        return response

    def create_session(self):
        first_message = 'You will be my assistant. I want you to write test cases for an application. '\
                        'I will be describing the functionality of each page of the app, and you will create test '\
                        'cases. Return the test steps in the a JSON format. For example:'\
                        '{"number":"<test case number>", "name":"<testCaseName>", "objective":"Test case objective",'\
                        ' "steps":[{"step": "Enter text into the Username field", '\
                        '"expectedBehaviour": "Text entered successfully"}]}. Use the keyword !!*!! to mark'\
                        'the start of the JSON data'\
                        'of the json format. Generate multiple test cases'\
                        'Here is the first scenario: when user logs in, the first screen they see will depend on the number of '\
                        'matters they have. if they have only one matter, they will be taken directly '\
                        'to the matter\'s Timeline view. If the user has multiple matters, '\
                        'they will see a list of matters grouped by firm name. In addition, '\
                        'there should be a search function that allows the user to search for '\
                        'matters. If a matter has a pending to-do items, it should be displayed on '\
                        'that specific matter\'s item. When user clicks on the matter, they will be '\
                        'taken to the Timeline viewed associated with this matter. Matters are sorted '\
                        'chronologically. User can scroll down when the matters can\'t fit all on the screen'
        self.conversation = [
            {
                "role": "user",
                "content": first_message
            }
        ]

        self.generate_response()


    def add_functionality(self, description):
        self.create_user_prompt(description)
        response = self.generate_response().choices[0].message.content
        # return response
        response = response.split("!!*!!")[1]
        return json_to_html_list(response)


        # return response
