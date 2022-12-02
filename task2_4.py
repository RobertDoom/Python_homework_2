# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

with open('file.txt', 'r') as data:
    f = data.read().split('\n')
n = int(input('Введите число: ' ))
result = 1
spisok = []
for i in range(-n, n + 1):
    spisok.append(i)
print(f"Промежуток от -N до N: {spisok}")
for k in f:
    result *= spisok[int(k)]
print(f'Произведение элементов на указанных позициях: {result}')