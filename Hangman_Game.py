import random

# List of predefined 5 words
words = ["python", "hangman", "computer", "program", "developer"]

# Pick a random word
secret_word = random.choice(words)

# Create a list with underscores for each letter
guessed_word = ["_"] * len(secret_word)

# Maximum incorrect guesses
max_attempts = 6
wrong_guesses = 0

# Store letters already guessed
guessed_letters = []

#for emogi press window key + .(dot)
print("🎮 Welcome to Hangman!")
print("Guess the word letter by letter.")

while wrong_guesses < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is in the secret word
    if guess in secret_word:
        print("✔️ Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

# Result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n💀 You lost! The word was:", secret_word)
