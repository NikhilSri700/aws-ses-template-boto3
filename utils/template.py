"""
Module for AWS SES templating.
"""

import boto3
import botocore
from utils.config import Config


class Template(Config):
    # AWS SES client created using the default credentials configured for AWS CLI
    ses = boto3.client('ses')

    @staticmethod
    def create_or_update(template_json='config/config_template.json'):
        """
        Static function that is used to create or update all the templates stored in 'config_template.json'.
        It will iterate through all the templates one by one, and if that template is new then it will create that
        template, and if it already exists then it will update that template.
        :return: str
        """
        all_templates = Template.load_json(template_json)

        for templateId, template in all_templates.items():
            try:
                Template.ses.create_template(Template=template)
                return f"Template \'{template['TemplateName']}\' Created Successfully"
            except Template.ses.exceptions.AlreadyExistsException:
                Template.ses.update_template(Template=template)
                return f"Template \'{template['TemplateName']}\' already exist, updated successfully"
            except Template.ses.exceptions.InvalidTemplateException:
                return f"Invalid Template: {templateId}"
            except botocore.exceptions.ParamValidationError:
                return f"Invalid Parameters passed for {templateId}"

    @staticmethod
    def delete(template_name):
        """
        Static function that will delete a template.
        :param template_name: str
            Name of the template that will be deleted.
        :return: str
        """
        try:
            Template.ses.delete_template(TemplateName=template_name)
        except Exception as error:
            return f'Exception occurred: {error}'
        else:
            return 'Template deleted successfully'

    @staticmethod
    def view(template_name):
        """
        Static function that will give details about a template.
        :param template_name: str
            Name of the template that will be described.
        :return: str
        """
        try:
            return Template.ses.get_template(TemplateName=template_name)
        except Template.ses.exceptions.TemplateDoesNotExistException:
            return 'Template does not exist'

    @staticmethod
    def list_all():
        """
        Static function that will list all the email templates stored in AWS SES.
        :return: List of all templates
        """
        template_dict = Template.ses.list_templates()
        template_list = []
        for template in template_dict['TemplatesMetadata']:
            template_list.append(template['Name'])

        for counter in range(len(template_list)):
            print(f'{counter+1}. {template_list[counter]}')
        return template_list
