'''
Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву.
Постолович А.С. 122-В
'''
import numpy as np
import math

A = np.zeros(5) #створюємо пустий масив розмірністю 5
for i in range(5):
    A[i] = int(input('input: ')) #заповнюємо його числами
for i in range(len(A)):
    print(f'{A[i]} - корінь: {math.sqrt(A[i])}, квадрат: {A[i]**2}')