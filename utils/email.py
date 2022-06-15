"""
Module for all the operations related to email.
"""

import boto3
import botocore
import re


class Email:
    # AWS SES client created using the default credentials configured for AWS CLI
    ses = boto3.client('ses')

    @staticmethod
    def check(email):
        regex = '^[a-z0-9A-Z]+[\\._]?[A-Za-z0-9]+[@]\\w+[.]\\w{2,3}$'
        if re.search(regex, email):
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
