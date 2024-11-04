import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = '#b1d9c4'
FILE_PATH = './data/cleaned_data.xlsx'
current_card = {}

# ---------------------------- 2.DATAFRAME ------------------------------- #

df = pd.read_excel('./data/cleaned_data.xlsx')
# df.index -> Check if the df has a proper index.

words_dict = df.to_dict(orient='records')
# print(words_dict) # Test
 
# ---------------------------- 3.FLIP CARDS FUNCTIONS ------------------------- #

def next_card():
    global current_card
    current_card = random.choice(words_dict)
    canvas.itemconfig(card_title, text='Russian')
    canvas.itemconfig(card_word, text=current_card["russian"])

def flip_card():
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_word, text=current_card["english"])
    canvas.itemconfig(card_back_image, image= card_back_image)
    
# ---------------------------- 1.GUI SETUP ------------------------------- #

# Window setup
window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Flip cards every 3 secs
window.after(3000, func=flip_card) 

# Canvas (card area) creation
canvas = tk.Canvas(window, width=800, height=526, bg='#b1d9c4', highlightthickness=0)  # Card background area
card_front_image = tk.PhotoImage(file='./images/card_front.png')  # Card image
card_back_image = tk.PhotoImage(file='./images/card_back.png')

canvas.create_image(400, 263, image=card_front_image)  # Center card image
canvas.grid(row=0, column=0, columnspan=2)  # Place canvas

# Text on canvas (inside the card)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")  # Top label
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")  # Centered label

# Buttons outside the card
left_button = tk.Button(window, text="❌", font=("Arial", 30), command=next_card)  # Left button
left_button.grid(row=1, column=0, padx=50, pady=50)

right_button = tk.Button(window, text="✅", font=("Arial", 30), command=next_card)  # Right button
right_button.grid(row=1, column=1, padx=50, pady=50)

# Starts the function
next_card()

# Main loop to display window
window.mainloop()
