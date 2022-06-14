"""
Main python file for the project.
"""

from utils.template import Template

# Program execution will start from here
if __name__ == '__main__':
    Template.create('Test-Template', 123, 'This is the text part', 'This is the HTML part')
    # print(Template.list_all())
