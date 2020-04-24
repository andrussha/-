'''
Розсортуйте заданий лінійний масив по зростанню.
Постолович А.С. 122-В
'''
import numpy as np
import random

A = np.zeros(10) #створюємо пустий масив
for i in range(10):
    A[i] = random.randint(-20,20) #заповнюємо масив
i =  0
n = len(A)
while i < n-1: #сортуємо масив бульбушковим методом
    j = 0
    while j < n-i-1:
        if A[j] > A[j+1]:
            if A[i] == A[i+1]:
                np.delete(A,i)
            A[j], A[j+1] = A[j+1], A[j]
        j +=1
    i +=1
for i in range(10):
    print(A[i], end=', ') #виводимо масив