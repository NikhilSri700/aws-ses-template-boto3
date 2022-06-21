# AWS SES Templating using Python and Boto3
## Introduction
Python utility made using classes and modules to send personalized e-mails using Amazon SES API and AWS e-mail Template.

## How to use
* Configure `AWS CLI` in your local system with your AWS credentials for `Boto3`.
* Install pipenv using pip:
```commandline
    pip install pipenv
```
* Clone the repository and create virtual environment using pipenv from project's root directory:
```commandline
    pipenv install
```
* Configure set of templates that you want to create or update in `.\config\config_template.json` file.
* Add all the email destinations for templated emails in `.\config\email_destinations.json` file.
* Also add user data that will be replaced in templated emails using placeholders in `.\config\user_data.json` file.
* File run the main file from the project's root directory:
```commandline
    python main.py
```
* You will be shown an interactive menu, choose options and proceed.

Thank You!