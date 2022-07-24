import random


number = random.randint(1 , 100)
attempt = 1
guess = int(input("Guess the number : "))
while(True):
    if(guess>number):
        guess = int(input("The Number is bigger than the number! Try again: "))
        attempt +=1
    elif(guess<number):
        guess = int(input("The Number is smaller than the number! Try again: "))
        attempt +=1
    else:
        print(f"YAY! You guessed it right in {attempt} attempts")
        break
