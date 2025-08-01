class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("\nYou're correct!")
            self.score += 1
        else:
            print("You're incorrect!")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")

    def get_score(self):
        final_score = f"{self.score}/{self.question_number}"
        return final_score

