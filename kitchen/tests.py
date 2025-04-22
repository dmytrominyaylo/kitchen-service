from django.test import TestCase

class DummyTest(TestCase):
    def test_sanity(self):
        self.assertEqual(1 + 1, 2)
