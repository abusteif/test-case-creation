import json

def json_to_html_list(data):
    # Convert JSON data to a Python object
    test_cases_dict = json.loads(data)
    html_list = "<ul>"
    print(test_cases_dict)

    # Create an HTML unordered list
    for test_case in test_cases_dict['testCases']:
        html_list += f"<li><b>Test Case Number:</b> {test_case['number']}<br>"
        html_list += f"<b>Test Case Name:</b> {test_case['name']}<br>"
        html_list += f"<b>Objective:</b> {test_case['objective']}<br>"
        html_list += "<b>Steps:</b><ol>"
        for step in test_case['steps']:
            html_list += f"<li>{step['step']}<br><i>Expected Behaviour:</i> {step['expectedBehaviour']}</li>"
        html_list += "</ol></li>"
    html_list += "</ul>"
    return html_list