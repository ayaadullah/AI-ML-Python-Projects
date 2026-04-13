import random

# ─────────────────────────────────────────
#  HANGMAN GAME —
# ─────────────────────────────────────────

WORDS = ["python", "Alpha", "Tasks", "keyboard", "Visuals"]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ==========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ==========""",
]

def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("\n🎮  Welcome to Hangman!")
    print("─" * 35)

    while incorrect_guesses < max_incorrect:
        # Display hangman stage
        print(HANGMAN_STAGES[incorrect_guesses])

        # Display word progress
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f"\n  Word: {display}")
        print(f"  Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print(f"  Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n✅  You won! The word was: '{word}' 🎉")
            break

        # Get player input
        guess = input("\n  Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠️  Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"  ⚠️  You already guessed '{guess}'. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"  ✅  '{guess}' is in the word!")
        else:
            incorrect_guesses += 1
            print(f"  ❌  '{guess}' is not in the word.")
    else:
        print(HANGMAN_STAGES[max_incorrect])
        print(f"\n💀  Game over! The word was: '{word}'")

    # Play again?
    again = input("\n  Play again? (y/n): ").lower().strip()
    if again == 'y':
        play_hangman()
    else:
        print("\n  Thanks for playing! 👋\n")

if __name__ == "__main__":
    play_hangman()