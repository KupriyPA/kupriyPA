import random
r = random.randint(1,10000)
i = 0
n = input("Попробуйте угадать число:")
while n != r or n != "выход":
    i = i+1
    if str(n) == "выход":
        print("Количество попыток: ", i-1)
        break
    elif int(n) < r:
        print("Загаданное число больше")
        n = input("Попробуйте угадать число:")
    elif int(n) > r:
        print("Загаданное число меньше")
        n = input("Попробуйте угадать число:")
    else:
        print("Вы угадали с ", i , "попытки" )
        break
