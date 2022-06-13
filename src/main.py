'''
Main python file for the project.
'''

import email_template as template

# Program execution will start from here
if __name__ == '__main__':
    template.create('Test-Template', 'New Subject', 'This is the text part', 'This is the HTML part')