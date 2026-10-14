a = 2345678899

reversed_num = int(str(a)[::-1])

print(reversed_num)

##############################
a = 2345678899
reverse = 0

while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10

print(reverse)