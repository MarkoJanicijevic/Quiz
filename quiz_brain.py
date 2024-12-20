class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        


    def next_question(self):
        answer = self.question_list[self.question_number].answer
        guess = input(f"Q. {self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(answer, guess)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, guess):
        if answer.lower() == guess.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is: {answer}")
        print(f"Your score is {self.score}/{len(self.question_list)}")

