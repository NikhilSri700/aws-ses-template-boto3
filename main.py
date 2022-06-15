"""
Main python file for the project.
"""

from utils.email import Email
from utils.template import Template


def mail_body():
    with open("./templates/text-part.txt", "r") as text_file:
        text_data = text_file.read()
    with open("./templates/html-part.html", "r") as html_file:
        html_data = html_file.read()
    return text_data, html_data


# Program execution will start from here
if __name__ == '__main__':
    text, html = mail_body()

    Email.verify_identity('nikhil.srivastav@watchguard.com')

    Template.create('Generic Github MFA', 'Enable MFA', text, html)
    # Template.view('Generic Github MFA')

    # print(Template.list_all())

    # Template.delete('Happy')

    # response = Template.ses.send_templated_email(
    #     Source='nikhil.srivastav@watchguard.com',
    #     Destination={
    #         'ToAddresses': ['nikhil.srivastav@watchguard.com']
    #     },
    #     ReplyToAddresses=['nikhil.srivastav@watchguard.com'],
    #     Template='Test-Template-1',
    #     TemplateData='{"name": "Nikhil", "username": "nsrivastav", "date": "10th July 2022"}'
    # )

    # print(response)
