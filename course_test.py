import unittest
from course import Course;

class testCourse(unittest.TestCase):
  
    def setUp(self):
        self.course = Course(1,'IS212 SPM', None)

    def tearDown(self):
        self.course = None

#    def test_enroll(self):
#        #id, name, section, startDate, endDate, prerequisite, trainer, learners
#        c = Course("212", "SPM", "6", "190821", "181121", "111", "Swarna", ["Claudia", "Haziq", "Jun Hong", "Marcus", "Xinyi"])
#        cor = c.course()
#        self.assertEqual(c.id, "212")
#        self.assertEqual(c.name(), "SPM")
#        self.assertEqual(c.section(), "6")
#        self.assertEqual(c.startDate(), "190821")
#        self.assertEqual(c.endDate(), "181121")
#        self.assertEqual(c.prerequisite(), "111")
#        self.assertEqual(c.trainer(), "Swarna")
#        self.assertEqual(c.learners(), ["Haziq", "Jun Hong", "Marcus"])

#        self.assertEqual(s.deposit(500), 1500)
#        self.assertRaises(Exception, s.deposit(9))
#        self.assertRaises(Exception, s.deposit(1001))

#    def test_withdraw(self):
#        s = Course(1500, "Swarna")
#        self.assertEqual(s.withdraw(1000), 500)
#        self.assertEqual(s.balance(), 500)
#        self.assertRaises(Exception, s.withdraw(100))
#        
#        s = Course(1500, "Swarna")
#        self.assertRaises(Exception, s.withdraw(1100))