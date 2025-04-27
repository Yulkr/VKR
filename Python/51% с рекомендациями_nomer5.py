import matplotlib.pyplot as plt
import numpy as np
import math

# Функция для вычисления вероятности успеха атаки по формуле Накамото
def attack_success_probability(z, q):
    prob = 0.0
    for k in range(z + 1):
        comb = math.comb(z + k - 1, k)
        prob += comb * ((1 - q) ** z) * (q ** k)
    return 1 - prob

# Функция для вычисления вероятности успеха атаки с учетом рекомендаций:
# 1. Увеличение числа подтверждений (дополнительных блоков)
# 2. Снижение эффективного хэшрейта злоумышленника
def attack_success_probability_improved(z, q, additional_confirmations=5, effective_hashrate_reduction=0.8):
    new_z = z + additional_confirmations
    new_q = q * effective_hashrate_reduction
    return attack_success_probability(new_z, new_q)

# Настройка параметров
z_values = list(range(1, 21))  # базовое число подтверждений
q_values = [0.3, 0.4, 0.5, 0.6]  # доли хэшрейта злоумышленника

# Вычисление вероятностей для исходного сценария
results_original = {}
for q in q_values:
    results_original[q] = [attack_success_probability(z, q) for z in z_values]

# Вычисление вероятностей для улучшенного сценария (применены рекомендации)
additional_confirmations = 5          # дополнительное число подтверждений
effective_hashrate_reduction = 0.8      # снижение эффективного хэшрейта на 20%
results_improved = {}
for q in q_values:
    results_improved[q] = [attack_success_probability_improved(z, q, additional_confirmations, effective_hashrate_reduction) for z in z_values]

# График 1: Сравнение вероятностей до и после применения рекомендаций
plt.figure(figsize=(12, 7))
for q in q_values:
    plt.plot(z_values, results_original[q], marker='o', label=f'Исходно: q={q}')
    plt.plot(z_values, results_improved[q], marker='x', linestyle='--', label=f'Улучшено: q={q}')
plt.title('Сравнение вероятности успеха атаки 51% до и после применения рекомендаций')
plt.xlabel('Количество подтверждённых блоков (z)')
plt.ylabel('Вероятность успеха атаки')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# График 2: Разница между исходной и улучшенной вероятностями
results_diff = {}
for q in q_values:
    results_diff[q] = [orig - imp for orig, imp in zip(results_original[q], results_improved[q])]

plt.figure(figsize=(12, 7))
for q in q_values:
    plt.plot(z_values, results_diff[q], marker='s', label=f'Разница: q={q}')
plt.title('Разница в вероятности успеха атаки до и после применения рекомендаций')
plt.xlabel('Количество подтверждённых блоков (z)')
plt.ylabel('Разница вероятности (Исходно - Улучшено)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
