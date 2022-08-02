from random import randint

los=randint(0,20)
odp=-1
i=0
money=1

while odp!=los:
    odp=int(input("Podaj odpowiedź"))
    i+=1
    if odp<los:
        print("Wylosowana liczba jest większa od Twojej odpowiedzi")
    elif odp>los:
        print("Wylosowana liczba jest mniejsza od Twojej odpowiedzi")
money+=1
print("Gratulacje odgadłeś liczbe", "Liczba prób: ", i, "Pieniądze: ", money)
