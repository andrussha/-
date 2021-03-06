'''
Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.
Постолович А. С. 122-В
'''
from functools import reduce
import numpy as np
import random

A = np.zeros(10) #створюємо пустий масив
z = [] #створюємо пустий список
for i in range(10):
    A[i] = random.randint(10,100) #заповнюємо масив значеннями
    if A[i]%5 == 0:
        z.append(A[i]) #додаємо в список всі числа кратні 5
if len(z) != 0:
    z_mult = reduce(lambda x, y: x * y, z)  # знаходимо і виводимо добуток всіх чисел кратних 5
    print(f"Добуток всіх чисел кратних 5 - {z_mult}")
else:
    print('Немає чисел кратних 5')