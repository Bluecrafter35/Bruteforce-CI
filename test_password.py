from unittest import TestCase
from password import Password


class TestPassword(TestCase):

    def test_check(self):
        pwd = Password("abc")
        self.assertEqual(True, pwd.check())

    def test_check2(self):
        pwd = Password("abc")
        self.assertEqual(True, pwd.check())
