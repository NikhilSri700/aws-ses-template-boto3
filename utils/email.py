"""
Module for all the operations related to email.
"""

import boto3
import botocore


class Email:
    # AWS SES client created using the default credentials configured for AWS CLI
    ses = boto3.client('ses')

    @staticmethod
    def verify_identity(email):
        """
        Function that will send a verification email to the email addresses provided to register that email as a
        verified identity.
        :param email: str
            E-mail address that needs to be verified
        :return: None
        """
        try:
            Email.ses.verify_email_identity(EmailAddress=email)
        except Exception as error:
            print(f'Exception occurred: {error}')
        else:
            print("Verification email sent, Please Verify")
