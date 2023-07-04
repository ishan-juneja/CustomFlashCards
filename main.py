import csv
import random

import pandas

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
from pandas import *

# ------------------------------------------------------------ Collecting Data
# reading CSV file
small_list_condition = False
try:
    with open('data/words_to_learn.csv', 'r') as f:
        data = read_csv(f)
        small_list_condition = True
except(FileNotFoundError):
    data = read_csv("/Users/ishanjuneja/Downloads/flash-card-project-start/data/french_words.csv")


data = data.to_dict(orient="records") # working with a data frame and converting it into a data frame
current_card = random.choice(data)
timer_id = ''

def generate_card():
    global current_card
    global timer_id
    current_card = random.choice(data)
    language_label.config(text="French", bg="WHITE")
    word_label.config(text=current_card["French"], bg="WHITE")
    canvas.itemconfig(image_id, image=card_front_img)
    window.after_cancel(timer_id)
    timer_id=window.after(3000, flip_card)

# ------------------------------------------------------------ Card Flipping
# changing the card every 3 seconds
def flip_card():
    global current_card
    global timer_id
    language_label.config(text="English")
    language_label.config(bg=BACKGROUND_COLOR)
    word_label.config(text=current_card["English"]) #accessing the current card's english version
    word_label.config(bg=BACKGROUND_COLOR)
    canvas.itemconfig(image_id, image=card_back_img)
    timer_id=window.after(3000, flip_card)

# ------------------------------------------------------------ Saving Progress

def incorrect_card():
    # global small_list_condition
    # global current_card
    # if not small_list_condition:
    #     with open('data/words_to_learn.csv', 'w') as f:
    #         writer = csv.writer(f)
    #         data = [current_card["French"], current_card["English"]]
    #         writer.writerow(data)
    generate_card()

def correct_card():
    data.remove(current_card)
    print(len(data))
    data_temp = pandas.DataFrame(data)
    data_temp.to_csv("data/words_to_learn.csv",index=False)
    generate_card()










# ------------------------------------------------------------ UI

# creating the window
window = Tk()
window.config(padx=50,pady=125,bg=BACKGROUND_COLOR)

#creating the canvas
canvas = Canvas(width=800,height=526)
canvas.grid(row=0,column=0)
card_front_img = PhotoImage(file='/Users/ishanjuneja/Desktop/Python Bootcamp/flash-card-project-start/images/card_front.png')
card_back_img = PhotoImage(file='/Users/ishanjuneja/Desktop/Python Bootcamp/flash-card-project-start/images/card_front.png')

image_id = canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

#creating buttons
right_img = PhotoImage(file='/Users/ishanjuneja/Desktop/Python Bootcamp/flash-card-project-start/images/right.png')
right_button = Button(image=right_img,highlightthickness=0,bg=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR,command=correct_card)
right_button.place(x=150,y=520)

wrong_img = PhotoImage(file='/Users/ishanjuneja/Desktop/Python Bootcamp/flash-card-project-start/images/wrong.png')
wrong_button = Button(image=wrong_img,highlightthickness=0,bg=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR,command=incorrect_card)
wrong_button.place(x=550,y=520)

#Creating Labels
language_label = Label(text="language", font=("Helvetica", 25, "italic"), bg="WHITE", fg="BLACK")
language_label.place(x=400,y=200, anchor="center")

word_label = Label(text="word", font=("Helvetica", 45, "bold"), bg="WHITE", fg="BLACK", anchor="center")
word_label.place(x=400,y=300,anchor="center")

flip_card()
generate_card()
window.mainloop()



