import unittest
from user import Trainers;

class testUser(unittest.TestCase):
    def setUp(self):
        self.trainer = Trainers(1, 'Marcus', 'Boss', 'department', 'Trainers')

    def tearDown(self):
        self.trainer = None
        self.
