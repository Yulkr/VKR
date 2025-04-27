import random
import hashlib
import matplotlib.pyplot as plt
#№1
# Параметры моделирования
attempt_range = list(range(10, 210, 10))  # Число попыток от 10 до 200
hash_size_bits = 16  # Размер хеша (бит)
hash_length = hash_size_bits // 4  # 4 бита на символ hex

# Функция моделирования атаки на день рождения
def birthday_attack_probability(attempts, simulations=1000):
    collisions = 0
    for _ in range(simulations):
        seen = set()
        for _ in range(attempts):
            val = str(random.randint(0, 2**32)).encode()
            hash_val = hashlib.sha256(val).hexdigest()[:hash_length]
            if hash_val in seen:
                collisions += 1
                break
            seen.add(hash_val)
    return collisions / simulations




# Построение графика зависимости вероятности от числа попыток
probabilities = [birthday_attack_probability(a) for a in attempt_range]

hash_size_bits_32 = 32
hash_length_32 = hash_size_bits_32 // 4  # в hex-символах

# Моделирование вероятности для 32-битного хеша
probabilities_32 = [birthday_attack_probability(a, simulations=1000) for a in attempt_range]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(attempt_range, probabilities_32, marker='s', color='orange', label='32-битный хеш')
plt.plot(attempt_range, probabilities, marker='o', label='16-битный хеш', linestyle='--')
plt.title('Сравнение вероятности коллизии для 16- и 32-битных хешей')
plt.xlabel('Число попыток')
plt.ylabel('Вероятность коллизии')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
