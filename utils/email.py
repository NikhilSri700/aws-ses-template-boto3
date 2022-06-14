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
        try:
            Email.ses.verify_email_identity(EmailAddress=email)
        except Exception as error:
            print(f'Exception occurred: {error}')
        else:
            print("Verification email sent, Please Verify")
