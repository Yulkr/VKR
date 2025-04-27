import matplotlib.pyplot as plt

# Параметры модели остаются прежними
block_size = 50           # количество транзакций в блоке
mempool_capacity = 1000   # максимальный размер mempool
ticks = 50                # число временных шагов
legit_tx_per_tick = 40    # число легитимных транзакций за шаг
attack_ratios = [0.0, 0.2, 0.4, 0.6, 0.8]  # доли атакующих транзакций

# Моделируем задержку для легитимной транзакции
def simulate_delay(attack_ratio):
    mempool = []
    delays = []
    for tick in range(ticks):
        num_attacks = int(attack_ratio * legit_tx_per_tick)
        num_legits = legit_tx_per_tick
        new_txs = [('attack', tick)] * num_attacks + [('legit', tick)] * num_legits
        mempool.extend(new_txs)

        # если mempool переполнен — отбрасываем самые старые
        if len(mempool) > mempool_capacity:
            mempool = mempool[-mempool_capacity:]

        # имитируем включение транзакций в блок
        block = mempool[:block_size]
        mempool = mempool[block_size:]

        # считаем задержку только для честных транзакций
        for tx_type, arrival_tick in block:
            if tx_type == 'legit':
                delays.append(tick - arrival_tick)

    return sum(delays) / len(delays) if delays else 0

def simulate_delay_improved(attack_ratio):
    """
    Моделирует задержку легитимных транзакций с применением механизма приоритезации.
    Перед формированием блока транзакции сортируются так, что легитимные транзакции имеют приоритет.
    """
    mempool = []
    delays = []

    for tick in range(ticks):
        num_attacks = int(attack_ratio * legit_tx_per_tick)
        num_legits = legit_tx_per_tick
        new_txs = [('attack', tick)] * num_attacks + [('legit', tick)] * num_legits
        mempool.extend(new_txs)

        # При переполнении mempool оставляем только последние транзакции
        if len(mempool) > mempool_capacity:
            mempool = mempool[-mempool_capacity:]

        # Сортировка пула: легитимные транзакции получают приоритет
        mempool.sort(key=lambda tx: (0 if tx[0]=='legit' else 1, tx[1]))

        # Формирование блока
        block = mempool[:block_size]
        mempool = mempool[block_size:]

        # Вычисление задержки для легитимных транзакций
        for tx_type, arrival_tick in block:
            if tx_type == 'legit':
                delays.append(tick - arrival_tick)

    return sum(delays) / len(delays) if delays else 0

# Расчёт средней задержки для разных долей атакующих транзакций
avg_delays = [simulate_delay(r) for r in attack_ratios]
# Расчёт задержек для улучшенной модели
avg_delays_improved = [simulate_delay_improved(r) for r in attack_ratios]

# График сравнения базовой и улучшенной моделей
plt.figure(figsize=(10, 6))
plt.plot([r * 100 for r in attack_ratios], avg_delays, marker='o', label='Базовая модель')
plt.plot([r * 100 for r in attack_ratios], avg_delays_improved, marker='x', linestyle='--', label='Улучшенная модель')
plt.title('Сравнение влияния спам-атаки на задержку легитимных транзакций')
plt.xlabel('Доля атакующих транзакций в общем потоке (%)')
plt.ylabel('Средняя задержка (в тактах)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
