import random
number=random.randrange(1,10)
number=int(number)
print("We are a gonna gamble today.")
print("You got 2 out of 10 chances.")
print("If you guess correct number within two attempts, you got 50 percent extra money, otherwise you will lost all.")
money=input("Tell the amount of money you wanna gamble. ")
amount=int(money)+ (50*int(money))/100
guess=input("Enter a number from 1 to 10.")
if guess.isdigit():
    guess=int(guess)
    if guess<=0 and guess>=11:
        print("Please enter a number between 1 to 10.")
        quit()
else:
    print("Please type a number not a string.")

if guess==number:
    print("Congratulations! You made it in first attempt.")
    print("You got "+str(amount)+" in your account.")
    quit()
else:
    print("Wrong Number! Try again with a different number.")
    print("It's your last chance, so be careful.")
    guess=input("Enter the number again. ")
    if guess.isdigit():
         guess=int(guess)
    if guess<=0 or guess>=11:
        guess=input("Please enter a number between 1 to 10.")
        guess=int(guess)
    if guess==number:
        print("Congratulatios! You made it.")
        print("You got "+str(amount)+" amount in your account.")
    else:
        print("Better luck next time!")
        print("You have lost both of your chances as well as money.")
        print("The correct number was "+ str(number))
