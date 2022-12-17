# Написать генератор песенки «TEN green bottles
# hanging on the wall».
# В песенке вместо цифр должны быть именно слова,
# обозначающие цифры, т.е. TEN, NINE, EIGHT, etc.

# counter = 0
# for i in range(1, 10):
#     if i == 1:
#         counter = 'nine'
#     elif i == 2:
#         counter = 'eight'
#     elif i == 3:
#         counter = 'seven'
#     elif i == 4:
#         counter = 'six'
#     elif i  == 5:
#         counter = 'five'
#     elif i == 6:
#         counter = 'four'
#     elif i == 7:
#         counter = 'three'
#     elif i == 8:
#         counter = 'two'
#     elif i == 9:
#         counter = 'one'
#     print(f" {counter} green bottles hanging on the wall,")
#     print(f" {counter} green bottles hanging on the wall,")
#     print(f"And if one green bottle should accidentally fall,")
#     print(f"There‛ll be... ")
# else:
#     print("NO green bottles hanging on the wall!")

list_num = ['nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two',
'one']

for i in list_num:
    print(f" {i} green bottles hanging on the wall,")
    print(f" {i} green bottles hanging on the wall,")
    print(f"And if one green bottle should accidentally fall,")
    print(f"There‛ll be... ")

print("NO green bottles hanging on the wall!")
