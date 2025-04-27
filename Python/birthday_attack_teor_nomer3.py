import matplotlib.pyplot as plt
import random
import hashlib

# Симуляция "атаки на день рождения" в блокчейн-контексте
# Цель: злоумышленник пытается создать поддельную транзакцию с тем же хешем, что и у настоящей

def simulate_blockchain_birthday_attack(hash_bits, max_attempts=200, simulations=1000):
    hash_len = hash_bits // 4  # длина хеша в hex-символах
    success_rates = []

    for attempts in range(10, max_attempts + 1, 10):
        success_count = 0
        for _ in range(simulations):
            seen = set()
            for _ in range(attempts):
                tx = str(random.getrandbits(64)).encode()
                tx_hash = hashlib.sha256(tx).hexdigest()[:hash_len]
                if tx_hash in seen:
                    success_count += 1
                    break
                seen.add(tx_hash)
        success_rate = success_count / simulations
        success_rates.append(success_rate)

    return list(range(10, max_attempts + 1, 10)), success_rates

# Смоделируем для 16 и 32 бит
x_16, y_16 = simulate_blockchain_birthday_attack(16)
x_32, y_32 = simulate_blockchain_birthday_attack(32)

# Построим график
plt.figure(figsize=(10, 6))
plt.plot(x_16, y_16, label="16 бит", marker='o')
plt.plot(x_32, y_32, label="32 бита", marker='s', linestyle='--')
plt.title("Атака на день рождения в контексте подделки транзакций в блокчейне")
plt.xlabel("Количество сгенерированных транзакций (попыток)")
plt.ylabel("Вероятность коллизии (успешной подделки)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import numpy as np

# Теоретическая модель вероятности коллизии
def theoretical_birthday_prob(k_vals, N):
    return [1 - np.exp(-k * (k - 1) / (2 * N)) for k in k_vals]

# Значения
k_values = np.arange(10, 210, 10)
N_16 = 2 ** 16
N_32 = 2 ** 32

# Теоретические вероятности
prob_theory_16 = theoretical_birthday_prob(k_values, N_16)
prob_theory_32 = theoretical_birthday_prob(k_values, N_32)

# График
plt.figure(figsize=(10, 6))
plt.plot(k_values, prob_theory_16, label='Теория (16 бит)', linestyle='--', color='blue')
plt.plot(k_values, prob_theory_32, label='Теория (32 бита)', linestyle='--', color='orange')
plt.plot(x_16, y_16, label='Симуляция (16 бит)', marker='o', color='blue')
plt.plot(x_32, y_32, label='Симуляция (32 бита)', marker='s', color='orange')

plt.title('Сравнение: теоретическая и эмпирическая вероятность коллизии')
plt.xlabel('Количество попыток (k)')
plt.ylabel('Вероятность коллизии')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
