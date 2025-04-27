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
