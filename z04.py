n = int(input("Введите размер шоколадки n "))
m = int(input("Введите размер шоколадки m "))
k = int(input("Введите количество долек "))
if k % n == 0 or k % m == 0:
    print("yes")
else:
    print("no")
