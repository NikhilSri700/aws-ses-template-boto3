"""
Module for all the operations related to email.
"""

import boto3
import os
import re
from utils.template import Template
import json


class Email(Template):
    # AWS SES client created using the default credentials configured for AWS CLI
    current_directory = os.getcwd()
    os.chdir('..')
    current_directory = os.path.join(current_directory, 'config')
    user_file = os.path.join(current_directory, 'user_data.json')
    destination_file = os.path.join(current_directory, 'email_destinations.json')
    ses = boto3.client('ses')

    @staticmethod
    def check(email):
        regex = '[a-zA-Z]+[A-Za-z0-9._%+-]+[a-zA-Z0-9]+@[A-Za-z0-9][A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}'
        if re.match(regex, email):
            return True
        else:
            return False

    @staticmethod
    def verify_identity(email):
        """
        Function that will send a verification email to the email addresses provided to register that email as a
        verified identity.
        :param email: str
            E-mail address that needs to be verified
        :return: str
        """
        if Email.check(email):
            try:
                Email.ses.verify_email_identity(EmailAddress=email)
            except Exception as error:
                return f'Exception occurred: {error}'
            else:
                return "Verification email sent, Please Verify"
        else:
            return "Email Address is not Valid"

    @staticmethod
    def delete_identity(identity):
        """
        Function will delete identity.
        :param identity: identity that needs to be deleted
        :return: str
        """
        try:
            Email.ses.delete_identity(Identity=identity)
        except Exception as error:
            return f'Exception occurred: {error}'
        else:
            return "Identity deleted successfully"

    @classmethod
    def send_using_template(cls, source_email, bulk=False):
        """
        Static function that will send templated emails using the already created templates with replacement data.
        :param source_email: str
            Email address using which mails will be sent.
        :param bulk: bool
            Boolean parameter that will be responsible for choice between sending bulk emails or not.
        :return: str
        """

        user_data = Email.load_json(cls.user_file)
        destinations = Email.load_json(cls.destination_file)

        template_list = Template.list_all()
        counter = 1
        destination_list = []
        for destination in destinations:
            destination_list.append({"Destination": destination,
                                     "ReplacementTemplateData": str(json.dumps(user_data[counter - 1]))
                                     })
            counter += 1
        template_choice = int(input("Choose one template: "))

        if bulk:
            try:
                Email.ses.send_bulk_templated_email(
                    Source=source_email,
                    DefaultTemplateData='{"name": "test", "username": "test", "data": "Unknown"}',
                    Destinations=destination_list,
                    Template=template_list[template_choice-1],)
            except Email.ses.exceptions.MessageRejected:
                return "Message Rejected"
            except Email.ses.exceptions.MailFromDomainNotVerifiedException:
                return "Email address is not verified, Verify using option 1 from Menu."
            except Exception as error:
                return f"Exception Occurred: {error}"
            else:
                return "All mails sent successfully"
        else:
            try:
                Email.ses.send_templated_email(
                    Source=source_email,
                    Destination=destinations[0],
                    Template=template_list[template_choice-1],
                    TemplateData=str(json.dumps(user_data[0])))
            except Email.ses.exceptions.MessageRejected:
                return "Message Rejected"
            except Email.ses.exceptions.MailFromDomainNotVerifiedException:
                return "Email address is not verified, Verify using option 1 from Menu."
            except Exception as error:
                return f"Exception Occurred: {error}"
            else:
                return "Mail sent successfully"
