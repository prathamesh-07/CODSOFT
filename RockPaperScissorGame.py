import tkinter as tk
import random

# Dictionary to map choices to their corresponding outcomes
outcomes = {
    'rock': {'rock': 'Tie', 'paper': 'Lose', 'scissors': 'Win'},
    'paper': {'rock': 'Win', 'paper': 'Tie', 'scissors': 'Lose'},
    'scissors': {'rock': 'Lose', 'paper': 'Win', 'scissors': 'Tie'}
}

# Function to handle game logic
def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    user_result = outcomes[user_choice][computer_choice]
    
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {user_result}")
    
    if user_result == 'Win':
        global user_score
        user_score += 1
        user_score_label.config(text=f"Your Score: {user_score}")
    elif user_result == 'Lose':
        global computer_score
        computer_score += 1
        computer_score_label.config(text=f"Computer Score: {computer_score}")

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

def create_choice_button(choice):
    button = tk.Button(root, text=choice.capitalize(), width=10, height=2,
                       command=lambda: play_game(choice))
    button.pack(pady=5)

choices = ['rock', 'paper', 'scissors']
for choice in choices:
    create_choice_button(choice)

result_label = tk.Label(root, text="", font=('Helvetica', 12))
result_label.pack(pady=20)

user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=('Helvetica', 12))
user_score_label.pack()
computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=('Helvetica', 12))
computer_score_label.pack()

root.mainloop()
