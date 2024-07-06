class Player:
    def __init__(self, name):
        self.name = name
        self.completed_lessons = []

    def complete_lesson(self, lesson):
        self.completed_lessons.append(lesson)

    def __str__(self):
        return f"{self.name} has completed: {', '.join([lesson.title for lesson in self.completed_lessons])}"
