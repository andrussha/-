'''
Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.
Постолович А. С. 122-В
'''
import numpy as np
import random

A = np.zeros(15) #створюємо пустий масив
for i in range(15):
    A[i] = random.randint(-15,30) # заповнюємо його випадковими числами
for i in range(15):
    print(A[i], end=', ') #поелементно виводимо масив
    if A[i] == max(A): #знаходимо найбільший елемент і виводимо його
        print(f'\n{A[i]} - найбільший елемент, індекс - {i}')
