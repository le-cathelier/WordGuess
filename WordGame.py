import random

def read_txt(filename):
    rows = []
    with open(filename) as file:
        for row in file:
            rows.append(row.strip())
    return rows

bank = read_txt("wordbank.txt")
rnd = random.choice(bank)

maxturn = 5
currturn = 0
attempt = 0
misp = []
incorrect = []

print("Welcome to Word Guess!")
print(f"You have", maxturn, f'turns to guess the right 5-lettered word.')
print(f"You are in turn", currturn+1, f".")
guess = input("Type your 5-lettered word here: ")
print("=========== LOADING ==============")

def verify(guess):
    if not guess.isalpha(): #check if numerical
        return "Not an alphabet!"
    if not len(guess) == 5:
        return "Not a 5-lettered word!"
    guess = guess.lower() #lowercases everything
    for let in guess:
        if let in rnd:
            if guess.rindex(let) != rnd.rindex(let):
                if let not in misp:
                    misp.append(let)
                print("_ ", end=' ')
            else:
                if let in misp:
                    misp.remove(let)
                print(let, end=' ')
        else:
            if let not in incorrect:
                incorrect.append(let)
            print("_", end=' ')
    print('')
    print("Misplaced letters: ", end='')
    print(misp)
    print("Incorrect letters: ", end='')
    print(incorrect)
    return "Incorrect word. Try again!"

while guess != rnd:
    print(verify(guess))
    currturn += 1
    attempt = maxturn - currturn
    if currturn == maxturn:
        print("LOSE. Failed to guess within five turns.")
        print(f"Word:", rnd)
        break
    print(f"You are in turn", currturn+1)
    print(f"You have", attempt, f"attempts left.")
    guess = input("Type your 5-lettered word here: ")
    print("=========== LOADING ==============")
else:
    print("WIN. You have guessed the correct word.")
    print(f"Word:", rnd)
