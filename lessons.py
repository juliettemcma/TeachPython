class Lesson:
    def __init__(self, title, content, exercises):
        self.title = title
        self.content = content
        self.exercises = exercises

    def __str__(self):
        return f"Lesson: {self.title}"

def create_lessons():
    lesson1 = Lesson(
        "Introduction to Python",
        "Welcome to Python programming. In this lesson, you will learn the basics of Python.",
        ["Write a 'Hello, World!' program.", "Explain the use of variables in Python."]
    )
    lesson2 = Lesson(
        "Control Structures",
        "Learn about if statements, loops, and other control structures in Python.",
        ["Write a program using a for loop.", "Write a program using an if statement."]
    )
    return [lesson1, lesson2]
