# Построение графика без сохранения в файл — для прямого отображения
import matplotlib.pyplot as plt

# Данные
q_values = [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60]
success_probs = [
    0.111111084,
    0.176468249,
    0.249951642,
    0.332879509,
    0.426001612,
    0.528237163,
    0.635339074,
    0.739649170,
    0.831811905,
    0.904015653,
    0.953008612
]

plt.figure(figsize=(10, 6))
plt.plot(q_values, success_probs, marker='o', linestyle='-', linewidth=2)
plt.title("Зависимость вероятности успеха 51%-атаки от доли хешрейта")
plt.xlabel("Доля хешрейта атакующего (q)")
plt.ylabel("Вероятность успеха атаки")
plt.grid(True)
plt.ylim(0, 1.05)
plt.xticks(q_values)

plt.tight_layout()
plt.show()
