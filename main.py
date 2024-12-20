from question_model import *
from data import *
from quiz_brain import QuizzBrain

question_bank = []
for key in trivia_questions:
    q = Question(key, trivia_questions[key])
    question_bank.append(q)

quiz_brain = QuizzBrain(question_bank)


while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You have finished the quiz. Your final score is {quiz_brain.score}/{len(quiz_brain.question_list)}")
