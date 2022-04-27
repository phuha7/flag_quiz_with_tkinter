from tkinter import *
import random
from PIL import Image, ImageTk
import pip._vendor.requests as requests
from io import BytesIO
from tkinter import messagebox

class QuizInterface:
    def __init__(self, codes, answers, choices):
        self.codes = codes
        self.answers = answers
        self.choices = choices
        self.total_questions = len(codes)
        self.img_width = 300
        self.img_height = 200
        self.current_question = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.tk_image = None
        self.root = Tk()
        self.root.title("Flag Game")
        self.root.geometry("550x550")
        self.root.config(padx=20, pady=20)

        Label(self.root, text="What flag is this?", font=("Arial", 30)).pack()

        self.image = self.display_image()

        self.user_ans = StringVar()
        self.buttons = self.radio_buttons()
        self.display_options()

        self.score = self.display_score_correct()
        self.wrong = self.display_score_wrong()
        self.answer = self.display_correct_answer()

        self.next_button = self.button()
        self.root.mainloop()

    def display_image(self):
        code = self.codes[self.current_question]
        api_url_flag = f"https://countryflagsapi.com/png/{code}"
        response = requests.get(api_url_flag)
        img = Image.open(BytesIO(response.content))
        resize_img = img.resize((self.img_width, self.img_height))
        self.tk_image = ImageTk.PhotoImage(resize_img)
        my_label = Label(self.root, image=self.tk_image)
        my_label.pack(padx=20, pady=20)
        return my_label

    def radio_buttons(self):
        bttns = []

        for i in range(3):
            radio_bttn = Radiobutton(self.root, text="", variable=self.user_ans, value="")
            bttns.append(radio_bttn)
            radio_bttn.pack(anchor=W)

        return bttns

    def display_options(self):
        val = 0

        self.user_ans.set(None)

        choices = self.choices[self.current_question]
        random.shuffle(choices)
        for choice in choices:
            self.buttons[val]["text"] = choice
            self.buttons[val]["value"] = choice
            val += 1

    def next_buttn(self):
        self.answer.config(text=f"The answer was: {self.answers[self.current_question]}")
        if self.user_ans.get() == self.answers[self.current_question]:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
        self.current_question += 1
        self.change_score()
        if self.current_question < self.total_questions:
            self.change_image()
            self.display_options()
        else:
            messagebox.showinfo("score", f"You got {self.correct_answers}/{self.current_question} right.")
            self.next_button["state"] = "disabled"

    def button(self):
        next_button = Button(self.root, text="Next", command=self.next_buttn)
        next_button.pack()
        return next_button

    def display_score_correct(self):
        right = Label(self.root, text=f"Right Answer: {self.correct_answers}")
        right.pack()
        return right

    def display_score_wrong(self):
        left = Label(self.root, text=f"Wrong Answer: {self.incorrect_answers}")
        left.pack()
        return left

    def display_correct_answer(self):
        answer = Label(self.root, text="")
        answer.pack()
        return answer

    def change_image(self):
        code = self.codes[self.current_question]
        api_url_flag = f"https://countryflagsapi.com/png/{code}"
        response = requests.get(api_url_flag)
        img = Image.open(BytesIO(response.content))
        resize_img = img.resize((self.img_width, self.img_height))
        self.tk_image = ImageTk.PhotoImage(resize_img)
        self.image["image"] = self.tk_image

    def change_score(self):
        self.score["text"] = f"Right Answer: {self.correct_answers}"
        self.wrong["text"] = f"Wrong Answer: {self.incorrect_answers}"

