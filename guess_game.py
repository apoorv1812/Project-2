import random
class guess_game():
    def __init__(self):
        print("The game is starting....")
    def guess_game(self):
        secret_number=random.randint(1,100)
        while True:
            user_input= int(input("Enter the number(1,100): "))
            if user_input<secret_number:
                print("The input is lower than the number. Please enter again: ")
            elif user_input>secret_number:
                print("The input is higher than the number. Please enter again: ")
            else:
                print("Yayy you entered it right!")
                break

s=guess_game()
s.guess_game()