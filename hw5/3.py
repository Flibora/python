#Дано число. На ти сумму и произведение его цифр.

num = str(input())
sum = 0
mult = 1
for i in num:
    sum += int(i)
    mult *= int(i)

print(sum)
print(mult)
