'''
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
Постолович А. С. 122-В
'''
from functools import reduce
import numpy as np
import random

A = np.zeros(10) #створюємо пустий масив
z = [] #створюємо пустий список
for i in range(10):
    A[i] = random.randint(5,500) #заповнюємо масив значеннями
    if A[i]%9 == 0 and A[i]%3 == 0:
        z.append(A[i]) #додаємо в список всі числа кратні 3 і 9
if len(z) != 0:
    z_mult = reduce(lambda x, y: x * y, z)  # знаходимо і виводимо добуток всіх чисел кратних 3 і 9
    print(f"Добуток всіх чисел кратних 3 і 9 - {z_mult}")
else:
    print(f'Немає чисел кратних 3 і 9')