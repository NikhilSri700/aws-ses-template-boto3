import unittest
from utils.email import Email


class TestEmail(unittest.TestCase):

    def test_check(self):
        self.assertEqual(Email.check('test.mail23@company.com'), True)
        self.assertEqual(Email.check('test.mail23@.company.com'), False)
        self.assertEqual(Email.check('23test.mail23@company.com'), False)
        self.assertEqual(Email.check('test.mail.23@company12.com'), True)

    def test_verify_identity(self):
        self.assertEqual(Email.verify_identity('thisisfordevelopment700@gmail.com'), 'Verification email sent, Please '
                                                                                     'Verify')

    def test_delete_identity(self):
        self.assertEqual(Email.delete_identity('thisisfordevelopment700@gmail.com'), 'Identity deleted successfully')


if __name__ == '__main__':
    unittest.main()
