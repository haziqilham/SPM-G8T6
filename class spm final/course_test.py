import unittest
from course import Course;

class testCourse(unittest.TestCase):
  
    def setUp(self):
        self.course = Course(1,'IS212 SPM', None)

    def tearDown(self):
        self.course = None