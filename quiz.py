class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def start(self):
        score = 0
        for question, answer in self.questions.items():
            user_answer = input(f"{question}\nYour answer: ")
            if user_answer.strip().lower() == answer.lower():
                score += 1
        print(f"Your score: {score}/{len(self.questions)}")

def create_quiz():
    questions = {
        "What is the output of print('Hello, World!')?": "Hello, World!",
        "What keyword is used to define a function in Python?": "def"
    }
    return Quiz(questions)
