# Number-Mastermind
"Number Mastermind" is a guessing game where the player's goal is to correctly guess a secret 4-digit number. The game provides feedback after each guess to help the player narrow down the possibilities.

Here's how the game works:

Setup:

The game generates a secret 4-digit number at the beginning of the game.
The player has a limited number of attempts (usually 10) to guess the secret number.
Gameplay:

The player enters a 4-digit number guess in the input field provided.
After each guess, the game provides feedback in the form of symbols (X, O, and _) to indicate how close the guess is to the secret number.
Feedback Symbols:

"X": Indicates that a digit in the player's guess is in the correct position in the secret number.
"O": Indicates that a digit in the player's guess is correct, but it's in a different position than in the secret number.
"_": Indicates that a digit in the player's guess is not present in the secret number.
Winning:

If the player's guess matches the secret number exactly, they win the game.
The game displays a congratulatory message and disables further input.
Losing:

If the player runs out of attempts without guessing the correct number, they lose the game.
The game reveals the secret number and displays a message indicating that the player is out of attempts.
The player's objective is to use the feedback provided after each guess to make educated guesses and deduce the correct sequence of digits in the secret number. It's a game of logic, deduction, and a bit of luck!

In your implementation, the feedback is generated using "X" for correct digits in the correct positions, "O" for correct digits in incorrect positions, and "_" for incorrect digits. The player continues making guesses until they either correctly guess the secret number or run out of attempts.

Runing the game (command): python3 number_mastermind.py
