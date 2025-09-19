from html import unescape

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def is_correct(self, choice):
        return self.answer.lower() == choice.lower()


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.index = 0

    def get_question(self):
        return self.questions[self.index]

    def check_answer(self, choice):
        question = self.get_question()
        correct = False
        if question.is_correct(choice):
            self.score += 1
            correct = True
        self.index += 1
        return correct

    def is_more(self):
        return self.index < len(self.questions)
