# exam_project.py
import random
import time

class Question:
    def __init__(self, text, options, correct_option, difficulty):
        self.text = text
        self.options = options
        self.correct_option = correct_option
        self.difficulty = difficulty

    def is_correct(self, selected_option):
        return selected_option == self.correct_option


class User:
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.time_taken = 0

    def update_score(self, points):
        self.score += points

    def update_time_taken(self, start_time):
        end_time = time.time()
        self.time_taken = round(end_time - start_time, 2)


class Exam:
    def __init__(self, questions):
        self.questions = questions

    def start_exam(self, user):
        print(f"Welcome, {user.username}! Let's start the exam.")
        
        difficulty_level = input("Choose difficulty level (easy, medium, or hard): ").lower()
        selected_questions = [q for q in self.questions if q.difficulty == difficulty_level]
        
        if not selected_questions:
            print(f"No {difficulty_level} level questions available. Starting with a random set.")

        start_time = time.time()
        random.shuffle(selected_questions)

        for i, question in enumerate(selected_questions, start=1):
            print(f"\nQuestion {i}: {question.text}")
            for j, option in enumerate(question.options, start=1):
                print(f"{j}. {option}")

            selected_option = int(input("Select an option (1-4): "))
            if 1 <= selected_option <= 4:
                if question.is_correct(selected_option):
                    print("Correct! You earned 1 point.")
                    user.update_score(1)
                else:
                    print(f"Wrong! The correct answer was {question.correct_option}.")
            else:
                print("Invalid option. Please choose a number between 1 and 4.")

        user.update_time_taken(start_time)
        print(f"\nExam completed, {user.username}!")
        print(f"Your score: {user.score}/{len(selected_questions)}")
        print(f"Time taken: {user.time_taken} seconds")

        # Display correct answers and provide feedback
        print("\nCorrect Answers:")
        for i, question in enumerate(selected_questions, start=1):
            print(f"Question {i}: {question.text} - Correct Answer: {question.correct_option}")
        
        self.provide_feedback(user)

    def provide_feedback(self, user):
        percentage_score = (user.score / len(self.questions)) * 100

        if percentage_score >= 70:
            print(f"Congratulations, {user.username}! You performed well.")
        elif 50 <= percentage_score < 70:
            print(f"Good effort, {user.username}. You can improve with more practice.")
        else:
            print(f"{user.username}, you might need more preparation. Keep practicing!")

if __name__ == "__main__":
    # Create questions with difficulty levels
    questions_data = {
        "Capital of France": ["Berlin", "Madrid", "Paris", "Rome", 3, "easy"],
        "Red Planet": ["Mars", "Venus", "Jupiter", "Saturn", 1, "medium"],
        "Largest Mammal": ["Elephant", "Blue Whale", "Giraffe", "Lion", 2, "hard"],
        "Programming Language": ["Java", "Python", "C++", "Ruby", 2, "easy"],
        "Python Framework": ["Django", "Flask", "Rails", "Express", 1, "medium"],
        "Data Science Library": ["Pandas", "TensorFlow", "Scikit-learn", "Matplotlib", 3, "hard"],
    }

    questions = [Question(q, options[:-2], options[-2], options[-1]) for q, options in questions_data.items()]

    # Create a user
    username = input("Enter your username: ")
    user = User(username)

    # Create an exam and start it for the user
    exam = Exam(questions)
    exam.start_exam(user)
