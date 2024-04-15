import unittest
from validate_email import validate_email

class TestEmail(unittest.TestCase):
    def test_validate_email(self):
        """
        Unit test for emails
        """
        self.assertTrue(validate_email("sachinacharya44@gmail.com"))
        self.assertTrue(validate_email("sachin@fusemachines.com"))
        self.assertFalse(validate_email("random@random.com"))
        self.assertFalse(validate_email("sachin?acharya@gmail.com"))
if __name__=="__main__":
    unittest.main()