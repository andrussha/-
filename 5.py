'''
Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
Постолович А. С. 122-В
'''
import numpy as np
import random

A = np.zeros(7) #створюємо пустий масив
for i in range(7):
    A[i] = 2*random.randint(1,100) # заповнюємо його випадковими числами
for i in range(7): #поелементно виводимо масив
    print(A[i])