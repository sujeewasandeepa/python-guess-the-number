import random

print("Hello welcome to guess-the-number game!")
print("I have a number in my mind.")
print("You have 5 chances to guess it!")
print("Good luck!")

def playGame(random_number):
    for attempt in range(5):
        user_input = int(input("Your guess is : "))
        if user_input == random_number:
            print (f"Congratulations! You win! Its {user_input}")
            break
        else:
            print(f"Nope. Not { user_input }")
            if user_input > random_number:
                print("It's less than that.")
            else:
                print("it's bigger than that.")
    print(f"What I guessed is { random_number }")

wantToPlay = True

while wantToPlay:
    random_number = random.randint(0, 50)
    playGame(random_number)
    userChoice = input("Want to play again?")
    if userChoice == 'n':
        wantToPlay = False
        print("Bye bye!")    