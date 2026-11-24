import numpy as np
#Задание 1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print()

#Задание 2

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])

# Каждый второй элемент
print("Каждый второй элемент:", hours[::2])

# Массив в обратном порядке
print("Обратный порядок:", hours[::-1])
print()

#Задание 3
# Создание двумерного массива (3 строки, 4 столбца)
temperatures = np.array([[12, 14, 13, 15], [11, 13, 16, 17], [10, 12, 15, 18]])

# 1. Форма, число измерений и число элементов
print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)

# 2. Значение из второй строки (индекс 1) и третьего столбца (индекс 2)
print("Вторая строка, третий столбец:", temperatures[1, 2])

# 3. Первая строка (индекс 0)
print("Первая строка:", temperatures[0])

# 4. Последний столбец (все строки ':', последний столбец '-1')
print("Последний столбец:", temperatures[:, -1])

# 5. Первые две строки (индексы 0 и 1) без первого столбца (начиная с индекса 1)
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])

# 6. Центральный фрагмент 2x2 (строки 0 и 1, столбцы 1 и 2)
center_fragment = temperatures[:2, 1:3]
print("Центральный фрагмент 2x2:\n", center_fragment)
print("Форма центрального фрагмента:", center_fragment.shape)
print()

