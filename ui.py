THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

import os

CWD = os.getcwd()
temp_true_img = "true.png"
true_img_path = os.path.join(CWD, temp_true_img)

temp_false_img = "false.png"
false_img_path = os.path.join(CWD, temp_false_img)

class MyQuizer:

    def __init__(self, my_quiz_brain:QuizBrain) -> None:
        self.my_quiz = my_quiz_brain
        self.window = Tk()
        self.window.title('My_Quizer')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_lable = Label(text='Score: 0', fg='white',bg=THEME_COLOR)
        self.score_lable.grid(row=0,column=1)

        self.canvas =  Canvas(width=300, height=250)
        self.que_text =  self.canvas.create_text(
            150,
            125,
            width=270,
            text='Que will be here...',
            font=("Arial", 18, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1,column=0, columnspan=2,pady=50)

        true_img = PhotoImage(file=true_img_path)
        self.true_img_btn = Button(image=true_img, highlightthickness=0,command=self.true_clicked)
        self.true_img_btn.grid(row=2,column=0)


        false_img = PhotoImage(file=false_img_path)
        self.false_img_btn = Button(image=false_img, highlightthickness=0, command=self.false_clicked)
        self.false_img_btn.grid(row=2,column=1)


        self.get_next_que()








        self.window.mainloop()

    def get_next_que(self):
        self.canvas.config(bg="white")
        self.score_lable.config(text=f"Score :{self.my_quiz.score}")
        if self.my_quiz.still_has_questions():            
            my_q_text = self.my_quiz.next_question()
            self.canvas.itemconfig(self.que_text, text=my_q_text)
        else:
            self.canvas.itemconfig(self.que_text,text=f"Thanks..!!, You have completed the quiz..!")
            self.true_img_btn.config(state="disabled")
            self.false_img_btn.config(state="disabled")


    def true_clicked(self):
        self.is_correct(self.my_quiz.check_answer("True"))

    def false_clicked(self):
        self.is_correct(self.my_quiz.check_answer("False"))

    def is_correct(self,is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_que)




if __name__ == '__main__':
    test_ui = MyQuizer()