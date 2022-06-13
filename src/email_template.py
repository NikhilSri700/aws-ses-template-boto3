'''
Module for AWS SES templating. 
'''

import boto3
import botocore

#AWS SES client created using the default credentials configured for AWS CLI 
ses = boto3.client('ses')

#Create Email Template
def create(templateName, subject, text, html):
    try:
        ses.create_template(
            Template = {
                'TemplateName': templateName,
                'SubjectPart': subject,
                'TextPart': text,
                'HtmlPart': html
            }
        )
    except ses.exceptions.AlreadyExistsException:
        print('Template Already exist')
    except ses.exceptions.InvalidTemplateException:
        print("Invalid Template")
    except botocore.exceptions.ParamValidationError:
        print("Invalid Parameters passed")
    else:
        print("Template Created Successfully")
