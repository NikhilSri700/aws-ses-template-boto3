import unittest
from unittest.mock import patch
from utils.email import Email
from moto import mock_ses
from tests.base_test import set_keyboard_input


class TestEmail(unittest.TestCase):
    def test_00_check(self):
        self.assertEqual(Email.check('test.mail23@company.com'), True)
        self.assertEqual(Email.check('test.mail23@.company.com'), False)
        self.assertEqual(Email.check('23test.mail23@company.com'), False)
        self.assertEqual(Email.check('test.mail.23@company12.com'), True)

    @mock_ses
    def test_01_verify_identity(self):
        self.assertEqual(Email.verify_identity('testmail@company.com'), 'Verification email sent, Please Verify')

    @mock_ses
    def test_02_delete_identity(self):
        self.assertEqual(Email.delete_identity('testmail@company.com'), 'Identity deleted successfully')

    @mock_ses
    def test_03_send_using_template(self):
        set_keyboard_input(["1", "1", "1", "1"])

        with patch('utils.email.Email.ses.send_templated_email') as mocked:
            mocked.return_value.ok = True
            self.assertEqual(Email.send_using_template('testmail@company.com'), 'Mail sent successfully')
        self.assertEqual(Email.send_using_template('testmail@company.com'), 'Message Rejected')

        with patch('utils.email.Email.ses.send_bulk_templated_email') as mocked_bulk:
            mocked_bulk.return_value.ok = True
            self.assertEqual(Email.send_using_template('testmail@company.com', True), 'All mails sent successfully')
        self.assertEqual(Email.send_using_template('testmail@company.com', bulk=True), 'Message Rejected')


if __name__ == '__main__':
    unittest.main()
