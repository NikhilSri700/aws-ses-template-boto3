"""
Module for all the operations related to email.
"""

import boto3
import botocore
import re
from utils.template import Template
import json


class Email(Template):
    # AWS SES client created using the default credentials configured for AWS CLI
    ses = boto3.client('ses')

    @staticmethod
    def check(email):
        regex = '[a-zA-Z]+[A-Za-z0-9._%+-]+[a-zA-Z0-9]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}'
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
        :return: None
        """
        if Email.check(email):
            try:
                Email.ses.verify_email_identity(EmailAddress=email)
            except Exception as error:
                print(f'Exception occurred: {error}')
            else:
                print("Verification email sent, Please Verify")
        else:
            print("Email Address is not Valid")

    @staticmethod
    def send_using_template(source_email, bulk=False):
        """
        Static function that will send templated emails using the already created templates with replacement data.
        :param source_email: str
            Email address using which mails will be sent.
        :param bulk: bool
            Boolean parameter that will be responsible for choice between sending bulk emails or not.
        :return: None
        """

        Email.load_jsons()
        template_list = Template.list_all()
        counter = 1
        destination_list = []
        for destination in Email.destinations:
            destination_list.append({"Destination": destination,
                                     "ReplacementTemplateData": str(json.dumps(Email.user_data[counter - 1]))
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
                print("Message Rejected")
            except Email.ses.exceptions.MailFromDomainNotVerifiedException:
                print("Email address is not verified, Verify using option 1 from Menu.")
            except Exception as error:
                print(f"Exception Occurred: {error}")
            else:
                print("All mails sent successfully")
        else:
            try:
                Email.ses.send_templated_email(
                    Source=source_email,
                    Destination=Email.destinations[0],
                    Template=template_list[template_choice-1],
                    TemplateData=str(json.dumps(Email.user_data[0])))
            except Email.ses.exceptions.MessageRejected:
                print("Message Rejected")
            except Email.ses.exceptions.MailFromDomainNotVerifiedException:
                print("Email address is not verified, Verify using option 1 from Menu.")
            except Exception as error:
                print(f"Exception Occurred: {error}")
            else:
                print("Mail sent successfully")
