# IMPORTS
from tkinter import *
import pandas as pd
import random
import time


# CONSTANTS AND GLOBAL VARIABLES
BG_COLOR = "#B1DDC6"
FILE_PATH = './data/cleaned_data.xlsx'
current_card = {} # Define card instance to be used in functions
dict = {} # Dictionary


# SEARCH FOR DATA FILES
try: 
    data = pd.read_csv("./data/words_to_lean.csv")
except FileNotFoundError:
    original_data = pd.read_excel(FILE_PATH,nrows=1000)
    dict = original_data.to_dict(orient='records')
else:
    dict = data.to_dict(orient='records')


# FUNCTIONS    
def next_card() -> None:
    """
    Selects and displays a random card from the cards dictionary. Displays the russian side of the card. Sets the timer to flip the card after 5 seconds.
    """
    global current_card, flip_timer
    
    root.after_cancel(flip_timer) # After ckicking the btns to go to the next card, reset the timer to flip that card.
    
    current_card = random.choice(dict)
    canvas.itemconfig(language_title, text=list(current_card.keys())[0], fill='black')
    canvas.itemconfig(word_text, text=current_card['russian'], fill='black')
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer = root.after(5000, flip_card) # We need to flip any card every single time we go to the next card

def known_card():
   """
   Removes the card from the dictionary when user correctly guess the meaning. Save the changes to a csv with the unknown words. 
   """
   dict.remove(current_card)
   data = pd.DataFrame(dict)
   data.to_csv("./data/words_to_lean.csv", index=False)
   next_card()
   
def flip_card():
    """
    Displays the english translation of the card and changes the interface accordingly.
    """
    canvas.itemconfig(language_title, text=list(current_card.keys())[1], fill='white')
    canvas.itemconfig(word_text, text=current_card['english'], fill='white')
    canvas.itemconfig(card_background, image=back_card_img)
   

# GUI
# Window
root = Tk()
root.title("Flash Card Game - Russian Words!")
root.config(padx=50, pady=50, bg=BG_COLOR)


# Canvas
canvas = Canvas(width=800, height=526)  # Creates the canvas with specified dimensions 
front_card_img = PhotoImage(file="images/card_front.png")  # Loads the lock image from a file
back_card_img = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=front_card_img)  # Places the image at the center of the canvas
language_title = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.config(bg=BG_COLOR, highlightthickness=0) 
canvas.grid(row=0, column=0, columnspan=2) 

# Buttons
correct_img = PhotoImage(file="images/right.png")
incorrect_img = PhotoImage(file="images/wrong.png")
correct_btn = Button(root, image=correct_img, highlightthickness=0, command=known_card)
correct_btn.grid(row=1, column=0)
incorrect_btn = Button(root, image=incorrect_img, highlightthickness=0, command=next_card)
incorrect_btn.grid(row=1, column=1)

# Timer function for flipping the card
flip_timer = root.after(5000, flip_card)
next_card() # Here we call the function in order to pick a word inmediately after the GUI is created

root.mainloop()     