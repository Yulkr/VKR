import matplotlib.pyplot as plt

# Данные из симуляции
q_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
success_probs = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
fail_probs = [0.99999991, 0.99973477, 0.97955554, 0.80093769, 0.40503225, 0.10547328]

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(q_values, success_probs, marker='o', label='P(success)', linewidth=2)
plt.plot(q_values, fail_probs, marker='s', label='P(failure)', linewidth=2)
plt.title("Вероятность успеха и провала атаки в зависимости от доли хешрейта (q)")
plt.xlabel("Доля хешрейта атакующего (q)")
plt.ylabel("Вероятность")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()