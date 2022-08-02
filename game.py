from imp import load_source
from random import randint

los=randint(0,20)
odp=-1
i=00

while odp!=los:
    odp=int(input("Give the answer"))
    i+=1
    if odp<los:
        print("The drawn number is greater than your answer")
    elif odp>los:
        print("The drawn number is less than your answer")

print("Congratulations, you guessed the number", "Your number of attempts: ", i)