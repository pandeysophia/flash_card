from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
word_list = data.to_dict(orient="records")


def next_word():
    word_choice = random.choice(word_list[random.randint(0, 100)]["French"])

    #french_word.config(text=word_list[random.randint(0, 100)]["French"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
french_word = canvas.create_text(400, 263, text=word_list[random.randint(0, 100)]["French"], font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=next_word)
right_button.grid(column=1, row=1)

window.mainloop()