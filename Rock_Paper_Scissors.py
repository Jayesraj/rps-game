import time
import random

user_score = 0
comp_score = 0
round = 1
choices = {
    1 : "Rock ✊",
    2 : "Paper 🖐️" ,
    3 : "Scissors ✌️"
}

name = input("'Hell'o there! What's your name?")

print(" Welcome to Rock Paper Scissors League!")
time.sleep(0.75)

print("Instructions:")
time.sleep(0.75)
print("You have three choices.")
time.sleep(0.75)
print("Rock ✊ : 1")
time.sleep(0.75)
print("Paper 🖐️ : 2")
time.sleep(0.75)
print("Scissors ✌️ : 3")
time.sleep(0.75)

def play_ground():
    global user_score, comp_score, round

    print(f"\n --- Round {round} --- ")
    round += 1

    try:
        user = int(input("Enter your choice: "))
        if user not in choices:
            print("Invalid choice. Please try again.")
            time.sleep(0.75)
            return

        computer = random.choice([1,2,3])
        print(f"You chose {choices[user]} and I chose {choices[computer]}")
        time.sleep(0.75)

        if user ==computer:
            print("It's a Tie!")
        elif (user == 1 and computer == 2) or (user ==2 and computer == 3) or (user == 3 and computer ==1):
            print("You win this round!")
            user_score += 1
        else:
            print("I won this round!")
            comp_score += 1
        time.sleep(0.75)
        print(f"Score => \n{name.capitalize()}: {user_score} \nMe: {comp_score} ")
        time.sleep(0.75)

    except ValueError:
        print("Invalid Number. Try again.")
        time.sleep(0.75)

def final_result():
    print(f"Final Scores => \n{name.capitalize()}: {user_score} \nMe: {comp_score}")
    time.sleep(0.75)

    if user_score > comp_score:
        print("I let you win. GG. Now go screenshot it — you'll never see it again. ")
    elif user_score == comp_score:
        print("We are a perfect match!")
    else: print("If i were you, I'd uninstall life for a bit. 🤮")
    time.sleep(0.75)

try:
    while True:
        answer = input("Play? ").lower()
        if answer in ["yes", "y"]:
            time.sleep(0.75)
            print("Lets Begin!")
            play_ground()
        elif answer in ["no", "n"]:
            time.sleep(0.75)
            print("Your 'No' was expected. Legends play, spectators say No 😜")
            time.sleep(0.75)
            final_result()
            break
        else:
            print("Sorry, I don't understand. Shall we try again?")
        time.sleep(0.75)
except KeyboardInterrupt:
    print("\nCoward detected! You rage-quit. 😵")
    time.sleep(0.75)
    final_result()

print("Thank you for playing!")
time.sleep(0.75)
print("Waiting to crush you the next time! \ncheers!")