from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_to_learn_dictionary = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    words_to_learn_dictionary = original_data.to_dict('records')
else:
    words_to_learn_dictionary = data.to_dict(orient='records')


def next_card():
    global three_second_timer, current_card
    window.after_cancel(three_second_timer)
    three_second_timer = window.after(3000, flip_card)
    current_card = random.choice(words_to_learn_dictionary)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_text, text=current_card['French'], fill='black')


def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_text, text=current_card['English'], fill='white')


def remove_from_words_to_learn():
    words_to_learn_dictionary.remove(current_card)
    pandas.DataFrame(words_to_learn_dictionary).to_csv('data/words_to_learn.csv', index=False)
    next_card()


# Window
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('Flash Cards')
three_second_timer = window.after(3000, func=flip_card)

# Images
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
x_button_img = PhotoImage(file='images/wrong.png')
check_button_img = PhotoImage(file='images/right.png')

# Canvas
canvas = Canvas(window, width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', fill='black', font=('Arial', 40, 'italic'))
card_text = canvas.create_text(400, 263, text='',
                               fill='black', font=('Arial', 60, 'bold'), tags='card_front_text')
canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Buttons
x_button = Button(image=x_button_img, highlightthickness=0, borderwidth=0, border=0, command=next_card)
x_button.grid(row=1, column=0)

check_button = Button(image=check_button_img, highlightthickness=0,
                      borderwidth=0, border=0, command=remove_from_words_to_learn)
check_button.grid(row=1, column=1)

next_card()
window.mainloop()