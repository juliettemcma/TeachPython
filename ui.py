import tkinter as tk
from tkinter import messagebox
from player import Player
from lessons import create_lessons
from quiz import create_quiz

class TeachPythonApp:
    def __init__(self):
        self.player = Player("Student")
        self.lessons = create_lessons()
        self.current_lesson = None

    def run(self):
        self.root = tk.Tk()
        self.root.title("TeachPython")

        self.label = tk.Label(self.root, text="Welcome to TeachPython!")
        self.label.pack()

        self.lesson_listbox = tk.Listbox(self.root)
        for lesson in self.lessons:
            self.lesson_listbox.insert(tk.END, lesson.title)
        self.lesson_listbox.pack()

        self.start_button = tk.Button(self.root, text="Start Lesson", command=self.start_lesson)
        self.start_button.pack()

        self.quiz_button = tk.Button(self.root, text="Take Quiz", command=self.start_quiz)
        self.quiz_button.pack()

        self.root.mainloop()

    def start_lesson(self):
        selected_index = self.lesson_listbox.curselection()
        if selected_index:
            self.current_lesson = self.lessons[selected_index[0]]
            messagebox.showinfo("Lesson Content", self.current_lesson.content)

    def start_quiz(self):
        quiz = create_quiz()
        quiz.start()
