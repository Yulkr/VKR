import sys
sys.path.append("c:/BlockSim/BlockSim")  # замени на путь к проекту, если другой

from Models.Transaction import LightTransaction
from InputsConfig import InputsConfig as p

p.Tn = 5             # кол-во транзакций/сек
p.Binterval = 10     # длительность интервала
p.Bsize = 1000000    # размер блока
p.Tfee = 0.01        # средняя комиссия
p.Tsize = 0.0005     # размер транзакции
p.NODES = []         # минимум 1 узел

# Добавим фиктивные узлы
class DummyNode:
    def __init__(self, id):
        self.id = id

p.NODES = [DummyNode(i) for i in range(5)]

# Генерация и выполнение
LightTransaction.create_transactions()
LightTransaction.execute_transactions(0)
