from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
from my_trivia import get_question
import html
from ui import MyQuizer


question_bank = []
new_question_data = get_question()
for question in new_question_data:
    question_text = question["question"]
    question_text = html.unescape(question_text)
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
my_quize_ui = MyQuizer(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
