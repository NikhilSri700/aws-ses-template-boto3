import unittest
from unittest.mock import patch
import os
import json
from moto import mock_ses
from utils.template import Template


class TestTemplate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        my_dict = {
            "Test-Template": {
                "TemplateName": "Sample-Template",
                "SubjectPart": "Sample Subject",
                "TextPart": "Sample text",
                "HtmlPart": "Sample text"
            }
        }
        with open('sample.json', 'w') as sampleFile:
            result = json.dumps(my_dict)
            sampleFile.write(result)
            cls.sample_json = os.path.abspath('sample.json')

    @classmethod
    def tearDownClass(cls):
        os.remove('sample.json')

    def test_00_create_or_update(self):
        self.assertEqual(Template.create_or_update(self.sample_json), "Template 'Sample-Template' Created "
                                                                      "Successfully")
        self.assertEqual(Template.create_or_update(self.sample_json), "Template 'Sample-Template' already exist, "
                                                                      "updated successfully")

    @mock_ses
    def test_01_view(self):
        with patch('utils.template.Template.ses.get_template') as mocked:
            mocked.return_value.text = 'Template Fetched'
            self.assertEqual(Template.view('Sample-Template').text, 'Template Fetched')
        self.assertEqual(Template.view('New-Template'), 'Template does not exist')

    @mock_ses
    def test_02_list_all(self):
        with patch('utils.template.Template.ses.list_templates') as mocked:
            self.assertEqual(Template.list_all(), [])

    def test_03_delete(self):
        self.assertEqual(Template.delete('Sample-Template'), 'Template deleted successfully')


if __name__ == '__main__':
    unittest.main()
