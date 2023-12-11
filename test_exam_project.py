# test_exam_project.py
import unittest
from unittest.mock import patch
from exam_project import Question, User, Exam

class TestQuestion(unittest.TestCase):
    def test_is_correct(self):
        question = Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3, "easy")
        self.assertTrue(question.is_correct(3))
        self.assertFalse(question.is_correct(2))

class TestUser(unittest.TestCase):
    def test_update_score(self):
        user = User("test_user")
        user.update_score(3)
        self.assertEqual(user.score, 3)

    def test_update_time_taken(self):
        user = User("test_user")
        user.update_time_taken(10)
        self.assertGreaterEqual(user.time_taken, 0)

class TestExam(unittest.TestCase):
    def setUp(self):
        self.questions = [
            Question("Question 1", ["Option 1", "Option 2", "Option 3", "Option 4"], 2, "easy"),
            Question("Question 2", ["Option 1", "Option 2", "Option 3", "Option 4"], 1, "medium"),
            Question("Question 3", ["Option 1", "Option 2", "Option 3", "Option 4"], 3, "hard"),
        ]

  
if __name__ == '__main__':
    unittest.main()
