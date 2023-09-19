from tkinter import *
from question_model import Questions
from quiz_brain import Quiz
import html


class uiInterface:
    def __init__(self, question_model: Questions, quiz_brain: Quiz):
        self.questions = question_model
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg="#375362")
        self.window.minsize(width=200, height=200)

        # text : score
        self.score_label = Label(text="Score: 0", fg="grey", bg="#375362", font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=1, sticky=E)

        # images
        self.trueButtonImg = PhotoImage(file="./images/true.png")
        self.falseButtonImg = PhotoImage(file="./images/false.png")

        # Canvas :
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.newQuestion = self.canvas.create_text(150, 125, text="Click any button to Start!!", fill="black", width=180, font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons :
        self.true_button = Button(image=self.trueButtonImg, border=0, highlightthickness=0, command=self.ok_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.falseButtonImg, border=0, highlightthickness=0, command=self.cross_pressed)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def final_score(self):
        self.canvas.itemconfig(self.newQuestion, text=f"Game Over\nTotal Score: {self.quiz.get_score()}")
        self.true_button.destroy()
        self.false_button.destroy()

    def updated_question(self):
        self.canvas.configure(bg='white')
        self.questions.next_question()
        questionNo = self.questions.question_number
        if self.quiz.still_has_questions(questionNo):
            question = self.quiz.get_questions()[questionNo]
            question = html.unescape(question)
            self.canvas.itemconfig(self.newQuestion, text=f"Q.No.{questionNo}:\n{question}")
        else:
            self.final_score()

    def update_score(self):
        self.quiz.add_score()
        self.score_label.config(text=f"Score: {self.quiz.get_score()}")

    def ok_pressed(self):
        val = "True"
        if self.quiz.check_false(val, self.questions.question_number):
            self.feedback("green")
            self.update_score()
        else:
            self.feedback("red")

    def cross_pressed(self):
        val = "False"
        if self.quiz.check_false(val, self.questions.question_number):
            self.feedback("green")
            self.update_score()
        else:
            self.feedback("red")

    def feedback(self, color: str):
        self.canvas.config(bg=color)
        self.window.after(1000, self.updated_question)
