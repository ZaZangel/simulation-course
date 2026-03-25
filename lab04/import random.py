import statistics
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Настройка стиля
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9

# LCG генератор
def lcg_random(seed=1, n=100000):
    m = 2**32
    a = 1664525
    c = 1013904223
    numbers = []
    x = seed
    for i in range(n):
        x = (a * x + c) % m
        numbers.append(x / m)
    return numbers

# Генерация данных
print("Генерация данных...")
lcg_nums = lcg_random(seed=42, n=100000)
lcg_mean = statistics.mean(lcg_nums)
lcg_var = statistics.variance(lcg_nums)

random.seed(42)
rand_nums = [random.random() for _ in range(100000)]
rand_mean = statistics.mean(rand_nums)
rand_var = statistics.variance(rand_nums)

# Теоретические значения
theory_mean = 0.5
theory_var = 1/12

# Создание фигуры с улучшенной компоновкой
fig = plt.figure(figsize=(16, 12))
fig.patch.set_facecolor('#f0f2f5')

# Главный заголовок
fig.suptitle('📊 АНАЛИЗ ГЕНЕРАТОРОВ СЛУЧАЙНЫХ ЧИСЕЛ', 
             fontsize=20, fontweight='bold', 
             y=0.98, color='#2c3e50')

# Создаем сетку графиков с большими отступами
gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1.2], 
                      hspace=0.4, wspace=0.35)

# ============ ГРАФИК 1: Гистограмма LCG ============
ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(lcg_nums, bins=50, density=True, 
         color='#e74c3c', alpha=0.7, edgecolor='#c0392b', 
         linewidth=0.5, label='LCG распределение')
ax1.axhline(y=1.0, color='#2c3e50', linestyle='--', 
            linewidth=2, label='Теоретическая плотность', alpha=0.8)
ax1.set_title('🔴 Базовый датчик (LCG)', fontsize=12, 
              fontweight='bold', color='#c0392b', pad=10)
ax1.set_xlabel('Значение', fontsize=10, color='#34495e')
ax1.set_ylabel('Плотность вероятности', fontsize=10, color='#34495e')
ax1.legend(loc='upper right', framealpha=0.9, fancybox=True, fontsize=8)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1.3)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_facecolor('#fafafa')

# ============ ГРАФИК 2: Гистограмма Random ============
ax2 = fig.add_subplot(gs[0, 1])
ax2.hist(rand_nums, bins=50, density=True, 
         color='#3498db', alpha=0.7, edgecolor='#2980b9', 
         linewidth=0.5, label='Random распределение')
ax2.axhline(y=1.0, color='#2c3e50', linestyle='--', 
            linewidth=2, label='Теоретическая плотность', alpha=0.8)
ax2.set_title('🔵 Встроенный генератор (Random)', fontsize=12, 
              fontweight='bold', color='#2980b9', pad=10)
ax2.set_xlabel('Значение', fontsize=10, color='#34495e')
ax2.set_ylabel('Плотность вероятности', fontsize=10, color='#34495e')
ax2.legend(loc='upper right', framealpha=0.9, fancybox=True, fontsize=8)
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1.3)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.set_facecolor('#fafafa')

# ============ ГРАФИК 3: Сравнение средних ============
ax3 = fig.add_subplot(gs[1, 0])
generators = ['LCG', 'Random', 'Теория']
means = [lcg_mean, rand_mean, theory_mean]
colors_bar = ['#e74c3c', '#3498db', '#2ecc71']
bars = ax3.barh(generators, means, color=colors_bar, 
                alpha=0.8, edgecolor='black', linewidth=1.2, height=0.5)
ax3.axvline(x=0.5, color='#2c3e50', linestyle=':', 
            linewidth=2, alpha=0.5)
ax3.set_title('📈 Сравнение средних значений', fontsize=12, 
              fontweight='bold', color='#2c3e50', pad=10)
ax3.set_xlabel('Среднее значение', fontsize=10, color='#34495e')
ax3.set_xlim(0.495, 0.505)
ax3.grid(True, alpha=0.3, axis='x', linestyle='--')
ax3.set_facecolor('#fafafa')

# Добавляем значения на столбцы
for bar, val in zip(bars, means):
    ax3.text(val + 0.0001, bar.get_y() + bar.get_height()/2, 
             f'{val:.6f}', va='center', fontsize=9, 
             fontweight='bold', color='#2c3e50')

# ============ ГРАФИК 4: Сравнение дисперсий ============
ax4 = fig.add_subplot(gs[1, 1])
variances = [lcg_var, rand_var, theory_var]
bars2 = ax4.barh(generators, variances, color=colors_bar, 
                 alpha=0.8, edgecolor='black', linewidth=1.2, height=0.5)
ax4.axvline(x=theory_var, color='#2c3e50', linestyle=':', 
            linewidth=2, alpha=0.5)
ax4.set_title('📉 Сравнение дисперсий', fontsize=12, 
              fontweight='bold', color='#2c3e50', pad=10)
ax4.set_xlabel('Дисперсия', fontsize=10, color='#34495e')
ax4.set_xlim(0.0825, 0.0840)
ax4.grid(True, alpha=0.3, axis='x', linestyle='--')
ax4.set_facecolor('#fafafa')

# Добавляем значения на столбцы
for bar, val in zip(bars2, variances):
    ax4.text(val + 0.00005, bar.get_y() + bar.get_height()/2, 
             f'{val:.6f}', va='center', fontsize=9, 
             fontweight='bold', color='#2c3e50')

# ============ ТАБЛИЦА РЕЗУЛЬТАТОВ (на отдельной оси) ============
ax5 = fig.add_subplot(gs[2, :])
ax5.axis('off')

# Данные для таблицы (сокращенные заголовки)
table_data = [
    ['Параметр', 'Теория', 'LCG', 'Random', 'Откл. LCG', 'Откл. Random'],
    ['Среднее', f'{theory_mean:.6f}', f'{lcg_mean:.6f}', f'{rand_mean:.6f}', 
     f'{lcg_mean - theory_mean:+.6f}', f'{rand_mean - theory_mean:+.6f}'],
    ['Дисперсия', f'{theory_var:.6f}', f'{lcg_var:.6f}', f'{rand_var:.6f}', 
     f'{lcg_var - theory_var:+.6f}', f'{rand_var - theory_var:+.6f}'],
    ['Погрешность ср., %', '—', 
     f'{abs(lcg_mean - theory_mean)/theory_mean*100:.3f}', 
     f'{abs(rand_mean - theory_mean)/theory_mean*100:.3f}', '—', '—'],
    ['Погрешность дисп., %', '—', 
     f'{abs(lcg_var - theory_var)/theory_var*100:.3f}', 
     f'{abs(rand_var - theory_var)/theory_var*100:.3f}', '—', '—']
]

# Создание таблицы с улучшенным дизайном
table = ax5.table(cellText=table_data[1:], 
                  colLabels=table_data[0],
                  cellLoc='center', 
                  loc='center',
                  bbox=[0.05, 0.1, 0.9, 0.8])  # Уменьшили область таблицы

# Настройка стиля таблицы
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.8)  # Уменьшили высоту строк

# Цвета заголовка
for i in range(6):
    table[(0, i)].set_facecolor('#34495e')
    table[(0, i)].set_text_props(color='white', fontweight='bold', fontsize=11)

# Чередование цветов строк
colors_rows = ['#ecf0f1', '#ffffff', '#ecf0f1', '#ecf0f1']
for row_idx in range(1, 5):
    for col_idx in range(6):
        table[(row_idx, col_idx)].set_facecolor(colors_rows[row_idx - 1])
        table[(row_idx, col_idx)].set_edgecolor('#bdc3c7')
        table[(row_idx, col_idx)].set_linewidth(1)

# Выделение лучших результатов
table[(1, 2)].set_facecolor('#d5f4e6')  # LCG среднее ближе к теории
table[(2, 3)].set_facecolor('#d5f4e6')  # Random дисперсия ближе к теории

# Заголовок таблицы
ax5.text(0.5, 0.95, '📋 ДЕТАЛЬНОЕ СРАВНЕНИЕ СТАТИСТИК', 
         ha='center', va='top',
         fontsize=14, fontweight='bold', 
         color='#2c3e50', transform=ax5.transAxes)

# Добавляем информацию о выборке
fig.text(0.5, 0.02, 
         f'📦 Размер выборки: {100000:,} значений | 🎲 Распределение: равномерное U[0, 1)', 
         ha='center', fontsize=11, fontweight='bold', 
         color='#7f8c8d', style='italic')

plt.tight_layout(rect=[0, 0.05, 1, 0.96])
plt.show()

# Вывод в консоль
print("\n" + "="*70)
print("📊 РЕЗУЛЬТАТЫ АНАЛИЗА ГЕНЕРАТОРОВ СЛУЧАЙНЫХ ЧИСЕЛ")
print("="*70)
print(f"\n🔴 БАЗОВЫЙ ДАТЧИК (LCG):")
print(f"   Среднее:   {lcg_mean:.6f} (отклонение: {lcg_mean - theory_mean:+.6f})")
print(f"   Дисперсия: {lcg_var:.6f} (отклонение: {lcg_var - theory_var:+.6f})")
print(f"   Погрешность среднего: {abs(lcg_mean - theory_mean)/theory_mean*100:.3f}%")
print(f"   Погрешность дисперсии: {abs(lcg_var - theory_var)/theory_var*100:.3f}%")

print(f"\n🔵 ВСТРОЕННЫЙ ГЕНЕРАТОР (Random):")
print(f"   Среднее:   {rand_mean:.6f} (отклонение: {rand_mean - theory_mean:+.6f})")
print(f"   Дисперсия: {rand_var:.6f} (отклонение: {rand_var - theory_var:+.6f})")
print(f"   Погрешность среднего: {abs(rand_mean - theory_mean)/theory_mean*100:.3f}%")
print(f"   Погрешность дисперсии: {abs(rand_var - theory_var)/theory_var*100:.3f}%")

print(f"\n🎯 ТЕОРЕТИЧЕСКИЕ ЗНАЧЕНИЯ:")
print(f"   Среднее:   {theory_mean:.6f}")
print(f"   Дисперсия: {theory_var:.6f}")

print("\n" + "="*70)
print("✅ Анализ завершён! Всем спасибо")
print("="*70 + "\n")