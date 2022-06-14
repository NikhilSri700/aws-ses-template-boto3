"""
Module for AWS SES templating.
"""

import boto3
import botocore


class Template:
    # AWS SES client created using the default credentials configured for AWS CLI
    ses = boto3.client('ses')

    # Create Email Template
    @staticmethod
    def create(template_name, subject, text, html):
        try:
            Template.ses.create_template(
                Template={
                    'TemplateName': template_name,
                    'SubjectPart': subject,
                    'TextPart': text,
                    'HtmlPart': html
                }
            )
        except Template.ses.exceptions.AlreadyExistsException:
            print('Template Already exist')
        except Template.ses.exceptions.InvalidTemplateException:
            print("Invalid Template")
        except botocore.exceptions.ParamValidationError:
            print("Invalid Parameters passed")
        else:
            print("Template Created Successfully")

    # Update Email Template
    @staticmethod
    def update(template_name, subject, text, html):
        try:
            Template.ses.update_template(
                Template={
                    'TemplateName': template_name,
                    'SubjectPart': subject,
                    'TextPart': text,
                    'HtmlPart': html
                }
            )
        except Template.ses.exceptions.TemplateDoesNotExistException:
            print('Template does not exist')
        except Template.ses.exceptions.InvalidTemplateException:
            print("Invalid Template")
        except botocore.exceptions.ParamValidationError:
            print("Invalid Parameters passed")
        else:
            print("Template Updated Successfully")

    @staticmethod
    def delete(template_name):
        try:
            Template.ses.delete_template(TemplateName=template_name)
        except Exception as error:
            print(f'Exception occurred: {error}')
        else:
            print('Template deleted successfully')

    @staticmethod
    def view(template_name):
        try:
            print(Template.ses.get_template(TemplateName=template_name))
        except Template.ses.exceptions.TemplateDoesNotExistException:
            print('Template does not exist')

    @staticmethod
    def list_all():
        print(Template.ses.list_templates())
