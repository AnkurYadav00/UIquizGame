class Questions:
    def __init__(self):
        self.answer = None
        self.question_number = 0

    def next_question(self):
        self.question_number += 1

    def question(self, question_bank):
        """ returns random question """
        return f"{question_bank[self.question_number]} "

    def answer(self):
        """ returns answer to the question """
        return self.answer
