# Повторный импорт после сброса состояния
import matplotlib.pyplot as plt
import numpy as np
import math

# Функция для вычисления вероятности успеха атаки 51% по формуле Накамото
def attack_success_probability(z, q):
    prob = 0.0
    for k in range(z + 1):
        comb = math.comb(z + k - 1, k)
        prob += comb * ((1 - q) ** z) * (q ** k)
    return 1 - prob

# Настройка параметров
z_values = list(range(1, 21))  # количество подтверждений (глубина)
q_values = [0.3, 0.4, 0.5, 0.6]  # доля хэшрейта злоумышленника

# Расчёт вероятностей
results = {}
for q in q_values:
    results[q] = [attack_success_probability(z, q) for z in z_values]

# Построение графика
plt.figure(figsize=(10, 6))
for q, probs in results.items():
    plt.plot(z_values, probs, marker='o', label=f'q = {q}')

plt.title('Вероятность успеха атаки 51% при разных долях вычислительной мощности')
plt.xlabel('Количество подтверждённых блоков (z)')
plt.ylabel('Вероятность успеха атаки')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
