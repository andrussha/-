'''
Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
'''
import numpy as np
import random

A = np.zeros(10) #створюємо пустий масив
k = 0 #створюємо лічильник
for i in range(10):
    A[i] = random.randint(-20,5) #заповнюємо масив значенями
mid = sum(A)/len(A)
for j in range(10):
    if A[j] > mid:
        k += 1  # підраховуємо скільки разів температура була вищою за середню
print(f'Кількість днів коли температура була вищою за середню - {k}')