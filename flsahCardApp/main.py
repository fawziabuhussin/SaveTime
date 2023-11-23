from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_CARD1 = ("arial", 40, "italic")
FONT_CARD2 = ("arial", 60, "bold")


try :
    data = pandas.read_csv("./data/to_learn.csv")
    data_words = data.to_dict(orient="records")

except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data_words = data.to_dict(orient="records")

current_card = {}

# ---------------------------- PICK A WORD TO TRANSLATE ------------------------------- #
def flip_card():
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text = current_card['English'], fill="white")
    canvas.itemconfig(fore_image, image = card_back_image)

def get_word() :
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(fore_image, image = card_front_image)
    current_card = random.choice(data_words)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text= current_card['French'], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def known_card() :
    data_words.remove(current_card)
    get_word()
    data_frame = pandas.DataFrame(data_words)
    data_frame.to_csv("data/to_learn.csv", index=False)


# ---------------------------- USER INTERFACE ------------------------------- #

window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# Image:

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526)
fore_image = canvas.create_image(400,263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, borderwidth=0,  highlightthickness=0)


#Title :
lang_text = canvas.create_text(400, 150, text="", font= FONT_CARD1 )
word_text = canvas.create_text(400, 263, text="", font= FONT_CARD2 )


# Buttons :
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, borderwidth = 0, command = known_card )
wrong_button = Button(image=wrong_image, highlightthickness=0,  borderwidth = 0 , relief="flat", command = get_word)


right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)


get_word()











window.mainloop()