import unittest
from utils.email import Email


class TestEmail(unittest.TestCase):
    def test_00_check(self):
        print("first")
        self.assertEqual(Email.check('test.mail23@company.com'), True)
        self.assertEqual(Email.check('test.mail23@.company.com'), False)
        self.assertEqual(Email.check('23test.mail23@company.com'), False)
        self.assertEqual(Email.check('test.mail.23@company12.com'), True)

    def test_01_verify_identity(self):
        print("second")
        self.assertEqual(Email.verify_identity('thisisfordevelopment700@gmail.com'), 'Verification email sent, Please '
                                                                                     'Verify')

    def test_02_delete_identity(self):
        print("third")
        self.assertEqual(Email.delete_identity('thisisfordevelopment700@gmail.com'), 'Identity deleted successfully')


if __name__ == '__main__':
    unittest.main()
