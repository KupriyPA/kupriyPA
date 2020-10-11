day = int(input("Введите день"))
hour = int(input("Введите час"))
if day > 31 or day < 1  :
    print("Введён некорректный день")
elif hour > 23 or hour <0 :
    print("Введено некорректное время")
elif day % 2 == 0 and hour <= 21:
    print("Парковка на левой стороне")
elif day % 2 ==1 and hour < 19:
    print("Парковка на левой стороне")
elif day % 2 ==1 and hour <= 21:
    print("Парковка на правой стороне")
elif day % 2 == 0 and hour <19:
    print("Парковка на правой стороне")
else:
    print("Парковка на любой стороне")