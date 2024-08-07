from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# Window
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('Flash Cards')

# Images
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
x_button_img = PhotoImage(file='images/wrong.png')
check_button_img = PhotoImage(file='images/right.png')

# Canvas
canvas = Canvas(window, width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text='Title', fill='black', font=('Arial', 40, 'italic'))
canvas.create_text(400, 263, text='Word', fill='black', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Buttons
x_button = Button(image=x_button_img, highlightthickness=0, borderwidth=0, border=0)
x_button.grid(row=1, column=0)

check_button = Button(image=check_button_img, highlightthickness=0, borderwidth=0, border=0)
check_button.grid(row=1, column=1)

window.mainloop()
