import matplotlib.pyplot as plt
#Моделирование атаки переполнения пула транзакций
# Параметры модели
block_size = 50  # сколько транзакций вмещает один блок
mempool_capacity = 1000  # максимальный размер mempool
ticks = 50  # шагов времени
legit_tx_per_tick = 40  # честных транзакций в секунду

# Доли атакующих транзакций в общем потоке
attack_ratios = [0.0, 0.2, 0.4, 0.6, 0.8]

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

# Рассчёт задержек при разных долях атак
avg_delays = [simulate_delay(r) for r in attack_ratios]

# График
plt.figure(figsize=(10, 6))
plt.plot([r * 100 for r in attack_ratios], avg_delays, marker='o')
plt.title('Влияние спам-атаки на задержку легитимных транзакций')
plt.xlabel('Доля атакующих транзакций в общем потоке (%)')
plt.ylabel('Средняя задержка (в тактах)')
plt.grid(True)
plt.tight_layout()
plt.show()
