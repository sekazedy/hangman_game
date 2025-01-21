import random
import tkinter as tk

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("900x600")
        self.word_list = ["PYTHON", "JAVASCRIPT", "KOTLIN", "JAVA", "RUBY", "SWIFT", "PHP"]
        self.secret_word = self.choose_secret_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        self.initialize_gui()
    
    def initialize_gui(self):
        self.hangman_canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.hangman_canvas.pack(pady=20)

        self.word_display = tk.Label(self.master, text="_ " * len(self.secret_word), font=("Helvetica", 30))
        self.word_display.pack(pady=(40, 20))

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)
        self.setup_alphabet_buttons()
    
    def choose_secret_word(self):
        return random.choice(self.word_list)
    
    def update_hangman_canvas(self):
        self.hangman_canvas.delete("all") # Clear the canvas for redrawing
        incorrect_guesses_count = len(self.incorrect_guesses)
        
        if incorrect_guesses_count >= 1:
            self.hangman_canvas.create_line(50, 180, 150, 180) # Base
    
    def guess_letter(self, letter):
        if letter in self.secret_word and letter not in self.correct_guesses:
            self.correct_guesses.add(letter)
        elif letter not in self.incorrect_guesses:
            self.incorrect_guesses.add(letter)
            self.attempts_left -= 1
            self.update_hangman_canvas()
        
        self.update_word_display()
        self.check_game_over()
    
    def update_word_display(self):
        displayed_word = " ".join([letter if letter in self.correct_guesses else "_" for letter in self.secret_word])
        self.word_display.config(text=displayed_word)
    
    def check_game_over(self):
        if set(self.secret_word).issubset(self.correct_guesses):
            self.display_game_over_message("Congratulations, you've won!")
        elif self.attempts_left == 0:
            self.display_game_over_message(f"Game over! The word was: {self.secret_word}")
    
    def setup_alphabet_buttons(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper_row = alphabet[:13] # First half of the alphabet
        lower_row = alphabet[13:] # Second half of the alphabet

        upper_frame = tk.Frame(self.buttons_frame)
        upper_frame.pack()
        lower_frame = tk.Frame(self.buttons_frame)
        lower_frame.pack()
        
        for letter in upper_row:
            button = tk.Button(upper_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2)
            button.pack(side="left", padx=2, pady=2)
        
        for letter in lower_row:
            button = tk.Button(lower_frame, text=letter, command=lambda l=letter: self.guess_letter(l), width=4, height=2)
            button.pack(side="left", padx=2, pady=2)
    
    def display_game_over_message(self, message):
        # Hide the alphabet buttons by hiding the entire buttons_frame
        self.buttons_frame.pack_forget()
        
        # Display the game over message in the now-empty area
        self.game_over_label = tk.Label(self.master, text=message, font=("Helvetica", 18), fg="red")
        self.game_over_label.pack(pady=(10, 20))

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()