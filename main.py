"""
Main python file for the project.
"""

from utils.email import Email
from utils.template import Template

# Program execution will start from here
if __name__ == '__main__':
    Template.create_or_update()
    # Template.view('Generic Github MFA')

    print(Template.list_all())

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
