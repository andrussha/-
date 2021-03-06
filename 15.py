'''
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
Постолович А.С. 122-В
'''
import numpy as np
import random

A = np.zeros(20) #створюємо пустий масив
z = [] #створюємо пустий список
for i in range(20):
    A[i] = random.randint(100, 200) #заповнюємо масив значенями
    if A[i]%2 == 0:
        z.append(A[i]) #додаємо в список всі парні значення масиву
z_sum = sum(z) #знаходимо суму всіх парних значень
print(f'Сума всіх парних чисел масиву - {z_sum}') #виводимо суму всіх парних значень