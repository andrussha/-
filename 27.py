'''
Лінійний масив містить відомості про кількість опадів, що випали за
кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року.
Постолович А.С. 122-В
'''
import numpy as np
import random

A = np.zeros(12) #створюємо пустий масив
k = 0 #вводимо лічильник посушливих місяців
for i in range(12):
    A[i] = random.randint(20, 50) #завовнюємо масив
    if A[i] < 30:
        k += 1 #перераховуємо посушливі місяці
A_sum = sum(A) #знаходимо заг. к-сть опадів
A_mid = sum(A)/len(A) #знаходиму сер. к-сть опадів
print(f'Загальна кількість опадів - {A_sum}\n'
      f'Середня кіскість опадів - {A_mid}\n'
      f'Кількість посушливих місяців - {k}') #виводимо дані на екран