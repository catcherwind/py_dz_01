num = int(input("Введите номер билета "))

d1 = num % 10
d2 = num // 10 % 10
d3 = num // 100 % 10
d4 = num // 1000 % 10
d5 = num // 10000 % 10
d6 = num // 100000 % 10
first_sum = d1 + d2 + d3
last_sum = d4 + d5 + d6
print("yes" if first_sum == last_sum else "no")