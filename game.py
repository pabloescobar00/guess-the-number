from random import randint

los=randint(0,20)
odp=-1
i=0 #ilość prób
money=0
nazwa=input("What's your name: ")

while odp!=los:
    odp=int(input("Enter the answer "))
    i+=1
    if odp<los:
        print("The drawn number is greater than your answer")
    elif odp>los:
        print("The drawn number is less than your answer")
money+=1

if i>=15:
    money+=1
    print("You didn't do very well")
elif i>=10:
    money+=2
    print("it's not bad but it could be better")
else:
    money+=3
    print("You did great")
print("Congratulations, you have guessed the drawn number", nazwa,  "Number of tries: ", i, "Money: ", money,)