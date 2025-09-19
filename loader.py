import requests
from random import shuffle
from html import unescape
from models import Question

def load_questions():
    URL = "https://opentdb.com/api.php?amount=5&type=multiple"
    response = requests.get(URL)
    data = response.json()
    questions = []
    for item in data["results"]:
        text = unescape(item["question"])
        correct_answer = unescape(item["correct_answer"])
        options = [unescape(opt) for opt in item["incorrect_answers"]] + [correct_answer]
        shuffle(options)
        questions.append(Question(text, options, correct_answer))
    return questions
