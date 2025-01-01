print("Welcome to Treasure Island. \nYour mission is to find the treasure.\n")
choice1=input("You are at a crossroad. \nWhich way would you go - left or right ?\n").lower()
score = 0
if choice1=="left":
    score += 5
    choice2=input("You face a river. You can either wait for a boat or swim yourself. \nWhat will you do - swim or wait ?\n").lower()
    if choice2=="wait":
        score += 5
        choice3=input("A boat came and picked you up. You now arrive in front of 3 doors red, green, blue. \nWhich door will you choose - red or green or blue ?\n").lower()
        if choice3=="red":
            print(f"You entered the wrong door. Fire engulfed you. Game Lost!! \nTotal Score {score}")
        elif choice3=="green":
            score += 5
            print(f"You entered a room filled with gold coins. You win!! \nTotal Score {score}")
        elif choice3=="blue":
            print(f"Wrong door. You were shot by some gangsters. Game Over!! \nTotal Score {score}")
        else:
            print(f"GAME OVER!! \nTotal Score {score}")
    else:
        print(f"You tried to swim but the waves were too strong. You drowned. Game Over!!! \nTotal Score {score}")
else:
    print(f"You fell into a hole. Game over!!! \nTotal Score {score}")