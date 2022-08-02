from random import randint

los=randint(0,20)
odp=-1
i=0 #ilość prób
money=0
nazwa=input("Jak masz na imie ")

while odp!=los:
    odp=int(input("Podaj odpowiedź "))
    i+=1
    if odp<los:
        print("Wylosowana liczba jest większa od Twojej odpowiedzi")
    elif odp>los:
        print("Wylosowana liczba jest mniejsza od Twojej odpowiedzi")
money+=1

if i>=15:
    money+=1
    print("Nie poradziłeś sobie wybitnie")
elif i>=10:
    money+=2
    print("nie jest źle ale może być lepiej")
else:
    money+=3
    print("Świetnie sobie poradziłeś")
print("Gratulacje odgadłeś liczbe", nazwa,  "Liczba prób: ", i, "Pieniądze: ", money,)