'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
Постолович А.С. 122-В
'''
import numpy as np
import random

A = np.zeros(20) #створюємо пустий масив
for i in range(20):
    A[i] = random.randint(-20,20) #заповнюємо масивї
print(A)
print(A[-2:10:-1]) #виводимо значення з необхідного інтервалу