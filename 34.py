'''
Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
Постолович А.С. 122-В
'''
import numpy as np
import random

A = np.zeros(20)
B = np.zeros(20)
C = np.zeros(20) #створюємо три пустих масив
for i in range(20):
    B[i] = random.randint(-20,20)
    A[i] = random.randint(-20,20) #заповнюємо два з них значеннями
for i in range(20):
    C[i] = A[i]*B[i] #утворюємо третій масв з добутку перших двох
for i in range(20):
    print(C[i], end=', ') #виводимо масив