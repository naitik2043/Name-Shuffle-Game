import random

names = ["naitik", "naman", "navya", "nitin", "pankaj", "suraj", "saloni",
         "ravi", "tashu", "sahil", "soumya", "nandini", "akash", "priya",
         "rahul", "sneha"]

def play_game():
    print("Welcome to the Name Shuffle Game!")
    print("Rules:")
    print("- A name will be shuffled and you need to guess it.")
    print("- Type 'hint' to see the first letter (you lose 0.5 points).")
    print("- Type 'quit' anytime to exit.\n")

    rounds = int(input("How many rounds do you want to play? "))
    difficulty = input("Choose difficulty (easy / medium / hard): ").lower()

    if difficulty == "easy":
        pool = [n for n in names if len(n) <= 5]
    elif difficulty == "hard":
        pool = [n for n in names if len(n) >= 6]
    else:
        pool = names[:]

    score = 0
    wrong = 0

    for r in range(1, rounds + 1):
        name = random.choice(pool)
        shuffled = name
        while shuffled == name:
            shuffled = ''.join(random.sample(name, len(name)))

        print(f"\nRound {r}/{rounds}")
        print("Shuffled name:", shuffled)

        while True:
            guess = input("Your guess: ").lower().strip()

            if guess == "quit":
                print("You quit the game.")
                rounds = r - 1
                return

            if guess == "hint":
                print("Hint: the first letter is", name[0])
                score -= 0.5
                continue

            if guess == name:
                print("Correct!")
                score += 1
                break
            else:
                print("Wrong, try again!")

        if guess != name:
            wrong += 1

    print("\nGame Over!")
    print("Correct answers:", score)
    print("Wrong answers:", wrong)
    if rounds > 0:
        print("Accuracy:", round((score / rounds) * 100, 2), "%")
    print("Thanks for playing!")

while True:
    play_game()
    restart = input("\nDo you want to play again? (y/n): ").lower().strip()
    if restart != "y":
        print("Goodbye! 👋")
        break