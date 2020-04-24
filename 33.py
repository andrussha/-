'''
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
Постолович А.С. 122-В
'''
from functools import reduce
import numpy as np
import random

A = np.zeros(20) #створюємо пустий масив
z = [] #створюємо пустий список
for i in range(20):
    A[i] = random.randint(-50,50) #заповнюємо масив
    if A[i] > 0:
        z.append(A[i]) #додаєм ненульові елементи в список
z_mult = reduce(lambda x, y: x*y, z) # перемножуємо елементи списка
print(f'Добуток всых ненульових елементів - {z_mult}')