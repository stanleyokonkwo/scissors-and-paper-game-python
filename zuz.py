import random


while True:
    options = ["R","P","S"]
    computer = random.choice(options)
    user = input("select between R P S ")
    if user in options:
        print (f"computer selected {computer} and user selected {user}")
    else:
        print("select valid option")
    if user == computer:
        print("there was a tie")

    elif user =="R":
        if computer =="S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user =="P":
        if computer =="R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
            
    elif user=="S":
        if computer == "P":
            print("Scissors cuts paper! You win")
        else:
            print("Rock smashes scissors! You lose.")

    Replay = input("Play again? (y/n): ")
    if Replay.lower() != "y":
        break
print("Thanks for playing")
