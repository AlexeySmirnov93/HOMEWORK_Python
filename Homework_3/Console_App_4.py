# ; Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# ; Пример:
# ; - 45 -> 101101
# ; - 3 -> 11
# ; - 2 -> 10

N = int(input())
b = ''

while N > 0:
    b = b + str(N % 2)
    N = N // 2

                
str = b
stringlength = len(str)
slicedString = str[stringlength::-1]
print (slicedString)