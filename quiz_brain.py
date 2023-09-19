from data import *


class Quiz:
    def __init__(self):
        self.answers = []
        self.score = 0
        self.questions = []

    def get_score(self):
        """ returns the score """
        return self.score

    def add_score(self):
        """ updates score with each correct answer """
        self.score += 1

    def get_questions(self):
        return self.questions

    def still_has_questions(self, question_no):
        return question_no < len(self.questions)

    def get_answers(self):
        return self.answers

    def generate_question_bank(self):
        qObj = fetch_questions()
        qObj.questions()
        for i in qObj.question_data:
            self.questions.append(i["question"])
            self.answers.append(i["correct_answer"])

    def check_true(self, val, question_number):
        if val == self.get_answers()[question_number]:
            return "True"

    def check_false(self, val, question_number):
        if val == self.get_answers()[question_number]:
            return "False"
