import unittest
from user import Administrator;
from user import Trainers;
from user import Learners;

class testUser(unittest.TestCase):
    def setUp(self):
        self.trainer = Trainers(1, 'mname', 'Marcus', 'Boss', 'department', 'Trainers')
        self.admin = Administrator(1, 'hname', 'Haziq', 'Boss', 'department', 'Administrator')
        self.learner = Learners(1, 'xname', 'Xinyi', 'Engineer', 'Technical', 'Learners')

    def tearDown(self):
        self.trainer = None
        self.admin = None
        self.learner = None

    def testGetNames(self):
        self.assertEquals(self.trainer.getName(), 'Marcus')
        self.assertEquals(self.admin.getName(), 'Haziq')
        self.assertEquals(self.learner.getName(), 'Xinyi')