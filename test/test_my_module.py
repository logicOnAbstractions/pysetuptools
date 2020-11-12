import unittest
from pysetuptools.my_module import count_matrix

class TestDummy(unittest.TestCase):


    def __init__(self, *args, **kwargs):
        super(TestDummy, self).__init__(*args, **kwargs)


    def setUp(self):
        self.answer = 36.0

    def test_mymatrix(self):
        self.assertEqual(float(count_matrix()),  float(self.answer))

