'''
Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
Постолович А.С. 122-В
'''
from functools import reduce
import numpy as np
import random

A = np.zeros(15) #створюємо пустий масив
z = [] #створюємо пустий список
for i in range(15):
    A[i] = random.randint(10, 50) #заповнюємо масив значенями
    if A[i]%7 == 0:
        z.append(A[i]) #додаємо в список всі числа кратні 7
z_mult = reduce(lambda x, y: x*y, z) #знаходимо добуток всіх чисел кратних 7
print(f'Добуток всіх чисел кратних 7 - {z_mult}') #виводимо добуток всіх чисел кратних 7