'''
Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
Постолович А. С. 122-В
'''
import numpy as np
import random

A = np.zeros(10) #створюємо пустий масив
k = 0 #створюємо лічильник
for i in range(10):
    A[i] = random.randint(-20,20) #заповнюємо масив значенями
for j in range(10):
    if A[j] < -10:
        k += 1 #підраховуємо скільки разів температура опускалась нижче -10 градусів
print(f'Температура опускалась нижче -10 градусів {k} разів')