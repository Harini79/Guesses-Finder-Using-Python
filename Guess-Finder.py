import random
x=int(input("Enter Guessing Limit:\n"))
randNumber=random.randint(1,x)
# print(randNumber)
userGuess=None
guesses=0
while(userGuess != randNumber):
    userGuess=int(input("Enter your guess:\n"))
    guesses +=1
    if(userGuess>randNumber):
        print("Lower number please!")
    elif(userGuess<randNumber):
        print("Higher number please!")
    else:
        print(f"great! you guessed the number {randNumber}!")
print(f"you guessed the number in {guesses} guesses!")
with open("Highscore.txt","r") as f:
    hiscore=int(f.read())
    
if (guesses<hiscore):
    print("you have just broken the highscore! We add your score in our reports! Great Play!")
    with open("Highscore.txt","w") as f:
        f.write(str(guesses))