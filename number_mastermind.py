import tkinter as tk
import random


class NumberMastermind:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Mastermind")
        self.root.geometry("1000x1050")

        self.secret_number = self.generate_secret_number()
        self.attempts_left = 10
        self.guess_history = []

        self.instruction_label = tk.Label(
            root, text="Guess the 4-digit number:", font=("Arial", 30)
        )
        self.instruction_label.pack(pady=10)

        self.guess_entry = tk.Entry(root, font=("Arial", 12))
        self.guess_entry.pack(pady=15)

        self.submit_button = tk.Button(
            root, text="Submit", command=self.check_guess, font=("Arial", 18)
        )
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=250)
        self.result_label.pack(pady=10)

    def generate_secret_number(self):
        return str(random.randint(1000, 9999))

    def check_guess(self):
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)

        if not guess.isdigit() or len(guess) != 4:
            self.result_label.config(
                text="Invalid guess. Please enter a 4-digit number."
            )
            return

        self.attempts_left -= 1
        feedback = self.generate_feedback(guess)
        self.guess_history.append((guess, feedback))

        if guess == self.secret_number:
            self.result_label.config(
                text=f"Congratulations! You guessed the number: {self.secret_number}"
            )
            self.submit_button.config(state=tk.DISABLED)
        else:
            feedback_history = "\n".join(
                [f"Guess: {g}, Feedback: {f}" for g, f in self.guess_history]
            )
            self.result_label.config(
                text=f"Attempts left: {self.attempts_left}\n\n{feedback_history}"
            )

            if self.attempts_left == 0:
                self.result_label.config(
                    text=f"Out of attempts. The number was {self.secret_number}."
                )
                self.submit_button.config(state=tk.DISABLED)

    def generate_feedback(self, guess):
        feedback = []

        for i in range(4):
            if guess[i] == self.secret_number[i]:
                feedback.append("X")
            elif guess[i] in self.secret_number:
                feedback.append("O")
            else:
                feedback.append("_")

        return " ".join(feedback)


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberMastermind(root)
    root.mainloop()
