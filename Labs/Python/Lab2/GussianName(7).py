import random
def hangman():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    chose_word = random.choice(word_list)
    guessed_letters = set()
    attempts = 7
    display_word = ['*'] * len(chose_word)

    print("Welcome to Hangman!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's start the game.")

    while attempts > 0 and '*' in display_word:
        print("\n" + " ".join(display_word))
        guess = input("guess letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("please enter character.")
            continue

        if guess in guessed_letters:
            print("you already that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in chose_word:
            for index, letter in enumerate(chose_word):
                if letter == guess:
                    display_word[index] = guess
        else:
            attempts -= 1
            print(f"wrong guess! You have {attempts} attempts left.")

    if '*' not in display_word:
        print(f"\ncongratulations, {name}! you guessed the word: {chose_word}")
    else:
        print(f"\nsorry, {name}. You've run out of attempts. The word was: {chose_word}")

hangman()