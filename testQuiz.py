import unittest
from quiz import Quiz
from unittest import mock


class TestQuiz(unittest.TestCase):
    def setUp(self):
        question1 = {
            'questionID': 1,
            'questionType': 'MCQ',
            'questionStr': 'How many cartridges are there in Xerox Printer?',
            'answerOptions': [('A', 1), ('B', 2), ('C', 4)],
            'answer': ('C', 4),
            'marks': 2
        }

        question2 = {
            'questionID': 2,
            'questionType': 'TF',
            'questionStr': 'A Xerox Printer can print double-sided',
            'answerOptions': [('A', 'True'), ('B', 'False')],
            'answer': ('A', 'True'),
            'marks': 2
        }
        questions = [question1, question2]

        self.s = Quiz(quizID=1, quizName='Chapter 1 Quiz',
                      questions=questions, ungradedQuiz=True, learnerID=1, score=0)

    def tearDown(self):
        self.s = None

    # Converts to JSON, so its easier for front end later
    def test_to_dict(self):
        #Mock 2 Question Class
        Question1 = mock.MagicMock()
        Question1.to_dict.return_value = {
            'questionID': 1,
            'questionType': 'MCQ',
            'questionStr': 'How many cartridges are there in Xerox Printer?',
            'answerOptions': [('A', 1), ('B', 2), ('C', 4)],
            'answer': ('C',4),
            'marks': 2
        }

        Question2 = mock.MagicMock()
        Question2.to_dict.return_value = {
            'questionID': 2,
            'questionType': 'TF',
            'questionStr': 'A Xerox Printer can print double-sided',
            'answerOptions': [('A', 'True'), ('B', 'False')],
            'answer': ('A', 'True'),
            'marks': 2
        }

        questions_mock = [Question1.to_dict(), Question2.to_dict()]

        #Testing of to_dict
        self.assertEqual(self.s.to_dict(), {
            'quizID': 1,
            'quizName': 'Chapter 1 Quiz',
            'questions': questions_mock,
            'ungradedQuiz': True,
            "learnerID": 1,
            "score": 0}
        )

    def test_updateScore(self):
        self.assertEqual(self.s.updateScore(10), 10)

    def test_computeScore(self):
        #Mock 2 Question Class
        Question1 = mock.MagicMock()
        Question1.gradeAnswer.return_value = {
            'questionID': 1,
            'marks': 2
        }

        Question2 = mock.MagicMock()
        Question2.gradeAnswer.return_value = {
            'questionID': 2,
            'marks': 2
        }

        userMarksList = [Question1.gradeAnswer(), Question2.gradeAnswer()]
        
        #Testing of computeScore
        self.assertEqual(self.s.computeScore(userMarksList), 4)

                
