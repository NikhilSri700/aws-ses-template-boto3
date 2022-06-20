import unittest
import os
import json
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

    def test_create_or_update(self):
        self.assertEqual(Template.create_or_update(self.sample_json), "Template 'Sample-Template' Created "
                                                                      "Successfully")
        self.assertEqual(Template.create_or_update(self.sample_json), "Template 'Sample-Template' already exist, "
                                                                      "updated successfully")

    def test_delete(self):
        self.assertEqual(Template.delete('Sample-Template'), 'Template deleted successfully')


if __name__ == '__main__':
    unittest.main()
