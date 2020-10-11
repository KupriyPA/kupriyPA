number = int(input("Введите число:"))
i = 2
if number == 1:
    print("Число простое")
elif number == 2:
    print("Число простое")
elif number > 2:
    while i < number and number % i != 0:
         i += 1
         if i == number:
             print("Число простое")
             break
    else:
        print("Число не является простым")
else:
    print("Введён некорректный символ")