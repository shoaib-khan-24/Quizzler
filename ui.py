from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self , quiz_obj:QuizBrain):
        self.quiz = quiz_obj

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30 , pady=20 , bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0" , fg="white" , bg=THEME_COLOR , font=("Arial",10,"italic") )             #score label

        self.canvas = Canvas(width=300 , height=250 , bg="white" , highlightthickness=0)                #canvas

        self.question = self.canvas.create_text(
            150 , 125 ,
            width=280 ,
            text="questions to display" ,
            font=("Arial",18,"italic") ,
            fill=THEME_COLOR
        )

        right_button_img = PhotoImage(file="images/true.png")
        wrong_button_img = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right_button_img , highlightthickness=0 , command=self.right_pressed)      #right button
        self.wrong_button = Button(image=wrong_button_img , highlightthickness=0 , command=self.wrong_pressed)      #wrong button

        #placing every entity
        self.score_label.grid(row=0 , column=1)
        self.canvas.grid(row=1 , column=0 , columnspan=2 , pady=50)
        self.right_button.grid(row=2 , column=0)
        self.wrong_button.grid(row=2 , column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question , fill=THEME_COLOR)
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.config(bg="yellow")
            self.canvas.itemconfig(self.question , text="You have reached the limit\nSee you tomorrow." , fill="blue")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_pressed(self):
        ans_status = self.quiz.check_answer("True")
        self.give_feedback(ans_status)

    def wrong_pressed(self):
        ans_status = self.quiz.check_answer("False")
        self.give_feedback(ans_status)

    def give_feedback(self , status):
        if status:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question , fill="white")
            self.window.after(1000 , self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question, fill="white")
            self.window.after(1000 , self.get_next_question)
