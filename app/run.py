from flask import Flask

from app.gptAPI import GptAPI

app = Flask(__name__)


@app.route('/')
def hello_world():
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
