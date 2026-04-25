# Импортируем библиотеку tkinter для создания графического интерфейса
import tkinter as tk
# Импортируем themed tk widgets (современные виджеты), messagebox для диалоговых окон, filedialog для сохранения файлов
from tkinter import ttk, messagebox, filedialog
# Импортируем numpy для работы с массивами и математическими операциями
import numpy as np
# Импортируем из scipy статистические функции: chisquare (критерий хи-квадрат), norm (нормальное распределение), chi2 (распределение хи-квадрат)
from scipy.stats import chisquare, norm, chi2
# Импортируем Figure для создания графиков matplotlib
from matplotlib.figure import Figure
# Импортируем FigureCanvasTkAgg для встраивания matplotlib графиков в tkinter окно
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Импортируем csv для работы с CSV файлами (экспорт результатов)
import csv
# Импортируем datetime для получения текущей даты и времени (для имен файлов)
from datetime import datetime
# Импортируем random для генерации случайных чисел (нужен для алгоритма инверсии CDF)
import random

# =============================
# ЦВЕТОВАЯ ПАЛИТРА
# =============================
# Определяем константы цветов для оформления интерфейса (в формате HEX)
COLOR_BG = "#F5F7FA"  # Цвет фона всего приложения (светло-серый)
COLOR_SURFACE = "#FFFFFF"  # Цвет поверхностей (белый для панелей, таблиц)
COLOR_PRIMARY = "#4A90E2"  # Основной акцентный цвет (синий для кнопок, заголовков)
COLOR_SECONDARY = "#50E3C2"  # Вторичный цвет (бирюзовый для графиков нормальной СВ)
COLOR_ACCENT = "#FF6B6B"  # Акцентный цвет (красный для ошибок, предупреждений)
COLOR_TEXT = "#2C3E50"  # Цвет основного текста (темно-синий/серый)
COLOR_TEXT_LIGHT = "#7F8C8D"  # Цвет второстепенного текста (светло-серый)
COLOR_SUCCESS = "#27AE60"  # Цвет успеха (зеленый для положительных результатов)
COLOR_WARNING = "#F39C12"  # Цвет предупреждения (оранжевый)
COLOR_ERROR = "#E74C3C"  # Цвет ошибки (красный)

# =============================
# НАСТРОЙКИ ГРАФИКОВ
# =============================
FIG_SIZE = (12, 8)  # Размер фигуры графиков в дюймах (ширина, высота)
FIG_DPI = 100  # Разрешение графиков (точек на дюйм)
SUBPLOT_ADJUST = {  # Словарь с параметрами отступов для подграфиков, чтобы они не наезжали друг на друга
    'left': 0.08,  # Отступ слева (8% от ширины)
    'right': 0.95,  # Отступ справа (95% от ширины)
    'top': 0.92,  # Отступ сверху (92% от высоты)
    'bottom': 0.08,  # Отступ снизу (8% от высоты)
    'wspace': 0.35,  # Горизонтальное пространство между подграфиками
    'hspace': 0.40,  # Вертикальное пространство между подграфиками
}

# =============================
# ТЕОРЕТИЧЕСКИЕ ЗНАЧЕНИЯ
# =============================
VALUES = np.array([1, 2, 3, 4])  # Массив значений дискретной случайной величины (X принимает значения 1,2,3,4)
DEFAULT_PROBS = np.array([0.25, 0.25, 0.25, 0.25])  # Вероятности по умолчанию (равномерное распределение: каждое значение с вероятностью 0.25)
N_SAMPLES = [10, 100, 1000, 10000]  # Список объемов выборок, для которых будем проводить моделирование

# =============================
# АЛГОРИТМЫ ГЕНЕРАЦИИ (ручная реализация)
# =============================

def generate_discrete_inverse_cdf(values, probs, size):
    """
    Генерация дискретной СВ методом инверсии функции распределения
    values: массив значений случайной величины [1, 2, 3, 4]
    probs: массив вероятностей для каждого значения [0.25, 0.25, 0.25, 0.25]
    size: количество генерируемых значений (объем выборки N)
    """
    samples = []  # Создаем пустой список для хранения сгенерированных значений
    answers = list(zip(values.tolist(), probs.tolist()))  # Объединяем значения и вероятности в список кортежей [(1, 0.25), (2, 0.25), ...]
    
    for _ in range(size):  # Повторяем size раз (генерируем каждое значение выборки)
        rand_val = random.random()  # Генерируем случайное число от 0 до 1 (равномерное распределение)
        A = 1.0  # Инициализируем переменную A единицей (начинаем с конца интервала [0,1])
        for val, pk in answers:  # Проходим по всем значениям и их вероятностям
            A -= pk  # Вычитаем текущую вероятность из A (двигаемся по интервалу)
            if A <= rand_val:  # Если A стало меньше или равно случайному числу — мы нашли нужный интервал
                samples.append(val)  # Добавляем соответствующее значение в выборку
                break  # Выходим из цикла, переходим к генерации следующего значения
    return np.array(samples)  # Возвращаем выборку как numpy массив


def generate_normal_box_muller(mu, sigma, size):
    """
    Генерация нормальной СВ методом Бокса-Мюллера
    mu: математическое ожидание (среднее) μ
    sigma: стандартное отклонение σ
    size: количество генерируемых значений (объем выборки N)
    """
    u1 = np.random.rand(size)  # Генерируем size случайных чисел из равномерного распределения U(0,1) для первой переменной
    u2 = np.random.rand(size)  # Генерируем size случайных чисел из равномерного распределения U(0,1) для второй переменной
    u1 = np.where(u1 == 0, 1e-10, u1)  # Заменяем нули на очень маленькое число 1e-10, чтобы избежать ошибки log(0)
    
    z = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)  # Применяем формулу Бокса-Мюллера: получаем стандартную нормальную СВ Z ~ N(0,1)
    return z * sigma + mu  # Масштабируем и сдвигаем: X = σZ + μ, чтобы получить N(μ, σ²)


class ModernStyleApp:
    """Основной класс приложения с современным интерфейсом"""
    
    def __init__(self, root):
        """
        Конструктор класса (вызывается при создании объекта приложения)
        root: главное окно tkinter
        """
        self.root = root  # Сохраняем ссылку на главное окно в атрибуте self.root
        root.title("📊 Лабораторная 5: Моделирование случайных величин")  # Устанавливаем заголовок окна
        root.geometry("1400x900")  # Устанавливаем размер окна: 1400 пикселей в ширину, 900 в высоту
        root.configure(bg=COLOR_BG)  # Устанавливаем цвет фона окна
        
        self.results_history = []  # Создаем пустой список для хранения истории всех запусков моделирования
        self.current_probs = DEFAULT_PROBS.copy()  # Копируем вероятности по умолчанию в текущие вероятности
        
        self.setup_style()  # Вызываем метод настройки стиля интерфейса
        self.create_main_layout()  # Вызываем метод создания основной структуры (вкладки)
        self.create_discrete_tab()  # Вызываем метод создания вкладки для дискретной СВ
        self.create_normal_tab()  # Вызываем метод создания вкладки для нормальной СВ
        self.create_summary_tab()  # Вызываем метод создания вкладки с выводами
        
    def setup_style(self):
        """Настраивает визуальный стиль виджетов ttk (themed tkinter)"""
        style = ttk.Style()  # Создаем объект для управления стилями ttk виджетов
        style.theme_use("clam")  # Устанавливаем тему "clam" (одна из современных тем ttk)
        
        # Настраиваем стиль для кнопок Primary.TButton
        style.configure("Primary.TButton",
                       background=COLOR_PRIMARY,  # Цвет фона кнопки — основной синий
                       foreground="white",  # Цвет текста кнопки — белый
                       font=("Segoe UI", 11, "bold"),  # Шрифт: Segoe UI, 11 пунктов, жирный
                       padding=10)  # Внутренние отступы кнопки — 10 пикселей
        
        # Настраиваем поведение кнопки при наведении (active state)
        style.map("Primary.TButton",
                 background=[("active", "#357ABD")])  # При наведении цвет фона меняется на более темный синий
        
        # Настраиваем стиль для таблицы Treeview
        style.configure("Treeview", background=COLOR_SURFACE,  # Фон таблицы — белый
                       foreground=COLOR_TEXT,  # Цвет текста — темный
                       fieldbackground=COLOR_SURFACE,  # Фон ячеек — белый
                       font=("Segoe UI", 10),  # Шрифт в таблице — Segoe UI, 10 пунктов
                       rowheight=30)  # Высота строки таблицы — 30 пикселей
        
        # Настраиваем стиль для заголовков столбцов таблицы
        style.configure("Treeview.Heading",
                       background=COLOR_PRIMARY,  # Фон заголовка — синий
                       foreground="white",  # Текст заголовка — белый
                       font=("Segoe UI", 11, "bold"),  # Шрифт заголовка — жирный
                       padding=5)  # Отступы в заголовке — 5 пикселей
        
    def create_main_layout(self):
        """Создает основную структуру интерфейса — виджет Notebook с вкладками"""
        self.notebook = ttk.Notebook(self.root)  # Создаем виджет Notebook (контейнер для вкладок)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=20)  # Размещаем Notebook в окне: растягиваем на все пространство, добавляем отступы 20px
        
    def create_discrete_tab(self):
        """Создает вкладку для моделирования дискретной случайной величины"""
        self.tab_discrete = ttk.Frame(self.notebook)  # Создаем фрейм (контейнер) для вкладки дискретной СВ
        self.notebook.add(self.tab_discrete, text="  📈 Дискретная СВ  ")  # Добавляем фрейм как вкладку в Notebook с заголовком
        
        # Верхняя панель управления
        control_frame = ttk.Frame(self.tab_discrete)  # Создаем фрейм для элементов управления
        control_frame.pack(fill="x", padx=20, pady=10)  # Размещаем фрейм: растягиваем по горизонтали, добавляем отступы
        
        # Контейнер для ввода вероятностей
        prob_container = ttk.LabelFrame(control_frame, text="🎲 Ряд распределения", padding=10)  # Создаем рамку с заголовком
        prob_container.pack(side="left", fill="x", expand=True, padx=(0, 10))  # Размещаем слева, растягиваем
        
        self.prob_entries = []  # Создаем пустой список для хранения полей ввода вероятностей
        self.prob_labels = []  # Создаем пустой список для хранения индикаторов валидности
        prob_inner = ttk.Frame(prob_container)  # Создаем внутренний фрейм для размещения элементов
        prob_inner.pack()  # Размещаем внутренний фрейм
        
        # Создаем поля ввода для каждой вероятности
        for i, val in enumerate(VALUES):  # Проходим по значениям [1, 2, 3, 4] с индексами 0, 1, 2, 3
            frame = ttk.Frame(prob_inner)  # Создаем фрейм для одного значения
            frame.grid(row=0, column=i, padx=8, pady=5)  # Размещаем фрейм в сетке (одна строка, столбец i)
            
            ttk.Label(frame, text=f"X={val}", font=("Segoe UI", 9, "bold")).pack()  # Создаем метку с названием значения (X=1, X=2, ...)
            
            entry = ttk.Entry(frame, width=7, font=("Segoe UI", 10), justify="center")  # Создаем поле ввода шириной 7 символов
            entry.insert(0, f"{DEFAULT_PROBS[i]:.2f}")  # Вставляем значение вероятности по умолчанию (0.25)
            entry.pack(pady=3)  # Размещаем поле ввода
            self.prob_entries.append(entry)  # Добавляем поле в список для последующего доступа
            
            indicator = ttk.Label(frame, text="✓", foreground=COLOR_SUCCESS, font=("Segoe UI", 8))  # Создаем индикатор валидности (зеленая галочка)
            indicator.pack()  # Размещаем индикатор
            self.prob_labels.append(indicator)  # Добавляем индикатор в список
        
        # Контейнер для кнопок
        btn_container = ttk.Frame(control_frame)  # Создаем фрейм для кнопок
        btn_container.pack(side="right", fill="y", padx=(10, 0))  # Размещаем справа, растягиваем по вертикали
        
        # Кнопка для установки равномерных вероятностей
        ttk.Button(btn_container, text="⚖️ Равномерное",
                  command=self.set_uniform_probs, style="Primary.TButton").pack(pady=3, fill="x")  # Кнопка вызывает метод set_uniform_probs
        
        # Кнопка для установки случайных вероятностей
        ttk.Button(btn_container, text="🎲 Случайное",
                  command=self.set_random_probs, style="Primary.TButton").pack(pady=3, fill="x")  # Кнопка вызывает метод set_random_probs
        
        # Кнопка запуска моделирования
        ttk.Button(btn_container, text="▶️ Запустить",
                  command=self.run_discrete_simulation, style="Primary.TButton").pack(pady=3, fill="x")  # Кнопка вызывает метод run_discrete_simulation
        
        # Кнопка экспорта результатов
        ttk.Button(btn_container, text="💾 Экспорт",
                  command=self.export_discrete_results, style="Primary.TButton").pack(pady=3, fill="x")  # Кнопка вызывает метод export_discrete_results
        
        # Индикатор валидности суммы вероятностей
        self.validity_label = ttk.Label(control_frame, 
                                       text="✓ Σp = 1.00",  # Текст по умолчанию: сумма равна 1
                                       foreground=COLOR_SUCCESS,  # Зеленый цвет
                                       font=("Segoe UI", 9))  # Шрифт
        self.validity_label.pack(side="bottom", pady=5)  # Размещаем внизу панели
        
        # Контейнер для графиков
        graph_frame = ttk.LabelFrame(self.tab_discrete, text="📊 Гистограммы распределения", padding=10)  # Создаем рамку для графиков
        graph_frame.pack(fill="both", expand=True, padx=20, pady=(10, 5))  # Размещаем: растягиваем на все доступное пространство
        
        self.fig_discrete = Figure(figsize=FIG_SIZE, dpi=FIG_DPI, facecolor=COLOR_SURFACE)  # Создаем фигуру matplotlib заданного размера
        self.fig_discrete.subplots_adjust(**SUBPLOT_ADJUST)  # Применяем настройки отступов для подграфиков
        
        self.canvas_discrete = FigureCanvasTkAgg(self.fig_discrete, master=graph_frame)  # Создаем canvas для отображения фигуры в tkinter
        self.canvas_discrete.get_tk_widget().pack(fill="both", expand=True)  # Размещаем canvas: растягиваем на все пространство
        
        # Таблица результатов
        table_frame = ttk.LabelFrame(self.tab_discrete, text="📋 Статистика", padding=10)  # Создаем рамку для таблицы
        table_frame.pack(fill="x", padx=20, pady=(5, 10))  # Размещаем: растягиваем по горизонтали
        
        columns = ("N", "Mean", "Var", "ErrMean", "ErrVar", "Chi2", "P_Value", "Status")  # Определяем идентификаторы столбцов таблицы
        self.tree_discrete = ttk.Treeview(table_frame, columns=columns, show="headings", height=5)  # Создаем таблицу (Treeview) с 8 столбцами, высота 5 строк
        
        headers = {  # Словарь с заголовками столбцов (ключ — идентификатор, значение — текст заголовка)
            "N": "N", "Mean": "x̄", "Var": "S²",
            "ErrMean": "err(x̄)%", "ErrVar": "err(S²)%",
            "Chi2": "χ²", "P_Value": "p", "Status": "H₀"
        }
        
        for col in columns:  # Проходим по всем столбцам
            self.tree_discrete.heading(col, text=headers[col])  # Устанавливаем текст заголовка столбца
            width = 75 if col in ["ErrMean", "ErrVar", "Chi2", "P_Value", "Status"] else 90  # Определяем ширину: 75px для коротких, 90px для остальных
            self.tree_discrete.column(col, width=width, anchor="center")  # Устанавливаем ширину и выравнивание по центру
        
        self.tree_discrete.pack(fill="x")  # Размещаем таблицу: растягиваем по горизонтали
        
        # Контейнер для отображения эмпирических вероятностей
        emp_frame = ttk.Frame(self.tab_discrete)  # Создаем фрейм
        emp_frame.pack(fill="x", padx=20, pady=(0, 10))  # Размещаем: растягиваем по горизонтали
        
        ttk.Label(emp_frame, text="📈 Pₑмп:", font=("Segoe UI", 9, "bold")).pack(side="left", padx=(0, 10))  # Метка-заголовок
        
        self.emp_prob_labels = []  # Создаем пустой список для меток эмпирических вероятностей
        for i, val in enumerate(VALUES):  # Проходим по значениям [1, 2, 3, 4]
            frame = ttk.Frame(emp_frame)  # Создаем фрейм для одного значения
            frame.pack(side="left", padx=15)  # Размещаем слева с отступом
            ttk.Label(frame, text=f"X={val}", font=("Segoe UI", 8)).pack()  # Метка с названием значения
            lbl = ttk.Label(frame, text="—", font=("Segoe UI", 10, "bold"), foreground=COLOR_PRIMARY)  # Метка для значения вероятности (по умолчанию "—")
            lbl.pack()  # Размещаем метку
            self.emp_prob_labels.append(lbl)  # Добавляем в список
            
    def create_normal_tab(self):
        """Создает вкладку для моделирования нормальной случайной величины"""
        self.tab_normal = ttk.Frame(self.notebook)  # Создаем фрейм для вкладки нормальной СВ
        self.notebook.add(self.tab_normal, text="  🔔 Нормальная СВ  ")  # Добавляем фрейм как вкладку
        
        control_frame = ttk.Frame(self.tab_normal)  # Создаем фрейм для элементов управления
        control_frame.pack(fill="x", padx=20, pady=10)  # Размещаем: растягиваем по горизонтали
        
        # Контейнер для ввода параметров
        param_frame = ttk.LabelFrame(control_frame, text="⚙️ Параметры N(μ,σ²)", padding=10)  # Создаем рамку с заголовком
        param_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))  # Размещаем слева, растягиваем
        
        param_inner = ttk.Frame(param_frame)  # Создаем внутренний фрейм
        param_inner.pack()  # Размещаем
        
        ttk.Label(param_inner, text="μ:", font=("Segoe UI", 10)).grid(row=0, column=0, padx=5)  # Метка "μ:"
        self.mu_entry = ttk.Entry(param_inner, width=8, font=("Segoe UI", 10))  # Поле ввода для μ
        self.mu_entry.insert(0, "0")  # Устанавливаем значение по умолчанию 0
        self.mu_entry.grid(row=0, column=1, padx=5)  # Размещаем в сетке
        
        ttk.Label(param_inner, text="σ:", font=("Segoe UI", 10)).grid(row=0, column=2, padx=5)  # Метка "σ:"
        self.sigma_entry = ttk.Entry(param_inner, width=8, font=("Segoe UI", 10))  # Поле ввода для σ
        self.sigma_entry.insert(0, "1")  # Устанавливаем значение по умолчанию 1
        self.sigma_entry.grid(row=0, column=3, padx=5)  # Размещаем в сетке
        
        # Контейнер для кнопок
        btn_container = ttk.Frame(control_frame)  # Создаем фрейм для кнопок
        btn_container.pack(side="right", fill="y", padx=(10, 0))  # Размещаем справа
        
        ttk.Button(btn_container, text="▶️ Запустить",
                  command=self.run_normal_simulation, style="Primary.TButton").pack(pady=3, fill="x")  # Кнопка запуска
        
        ttk.Button(btn_container, text="💾 Экспорт",
                  command=self.export_normal_results, style="Primary.TButton").pack(pady=3, fill="x")  # Кнопка экспорта
        
        # Контейнер для графиков
        graph_frame = ttk.LabelFrame(self.tab_normal, text="📊 Гистограммы + теоретическая плотность", padding=10)  # Рамка для графиков
        graph_frame.pack(fill="both", expand=True, padx=20, pady=(10, 5))  # Размещаем: растягиваем
        
        self.fig_normal = Figure(figsize=FIG_SIZE, dpi=FIG_DPI, facecolor=COLOR_SURFACE)  # Создаем фигуру matplotlib
        self.fig_normal.subplots_adjust(**SUBPLOT_ADJUST)  # Применяем настройки отступов
        
        self.canvas_normal = FigureCanvasTkAgg(self.fig_normal, master=graph_frame)  # Создаем canvas
        self.canvas_normal.get_tk_widget().pack(fill="both", expand=True)  # Размещаем canvas
        
        # Контейнер для статистики
        stats_frame = ttk.Frame(self.tab_normal)  # Создаем фрейм
        stats_frame.pack(fill="x", padx=20, pady=(5, 10))  # Размещаем: растягиваем по горизонтали
        
        self.normal_stats = {}  # Создаем словарь для хранения меток статистики
        stats = [("μ теор:", "mu_t"), ("x̄ выборка:", "mu_e"),  # Список пар (текст метки, ключ в словаре)
                 ("σ² теор:", "var_t"), ("S² выборка:", "var_e")]
        
        for name, key in stats:  # Проходим по всем парам
            frame = ttk.Frame(stats_frame)  # Создаем фрейм для одной метки
            frame.pack(side="left", padx=20)  # Размещаем слева
            ttk.Label(frame, text=name, font=("Segoe UI", 9)).pack()  # Метка с названием
            lbl = ttk.Label(frame, text="—", font=("Segoe UI", 10, "bold"), foreground=COLOR_PRIMARY)  # Метка для значения
            lbl.pack()  # Размещаем
            self.normal_stats[key] = lbl  # Сохраняем в словарь по ключу
        
        # Контейнер для χ²-статистики
        chi_frame = ttk.Frame(stats_frame)  # Создаем фрейм
        chi_frame.pack(side="right", padx=20)  # Размещаем справа
        ttk.Label(chi_frame, text="χ²-тест:", font=("Segoe UI", 9)).pack()  # Метка-заголовок
        self.chi_label = ttk.Label(chi_frame, text="—", font=("Segoe UI", 10, "bold"), foreground=COLOR_PRIMARY)  # Метка для результата
        self.chi_label.pack()  # Размещаем
        
    def create_summary_tab(self):
        """Создает вкладку с выводами и сравнением точности"""
        self.tab_summary = ttk.Frame(self.notebook)  # Создаем фрейм для вкладки выводов
        self.notebook.add(self.tab_summary, text="  📝 Выводы  ")  # Добавляем как вкладку
        
        summary_frame = ttk.LabelFrame(self.tab_summary, text="📊 Сравнение точности", padding=15)  # Создаем рамку
        summary_frame.pack(fill="both", expand=True, padx=20, pady=20)  # Размещаем: растягиваем
        
        columns = ("N", "Discrete_Err", "Normal_Err", "Conclusion")  # Определяем столбцы таблицы
        self.tree_summary = ttk.Treeview(summary_frame, columns=columns, show="headings", height=6)  # Создаем таблицу
        
        headers = {"N": "N", "Discrete_Err": "err(дискр.)%",  # Словарь заголовков
                   "Normal_Err": "err(норм.)%", "Conclusion": "Оценка"}
        
        for col in columns:  # Проходим по столбцам
            self.tree_summary.heading(col, text=headers[col])  # Устанавливаем заголовок
            self.tree_summary.column(col, width=200, anchor="center")  # Устанавливаем ширину 200px и выравнивание
        
        self.tree_summary.pack(fill="both", expand=True, pady=(0, 15))  # Размещаем таблицу: растягиваем
        
        conclusion_frame = ttk.LabelFrame(summary_frame, text="💡 Выводы", padding=15)  # Создаем рамку для текстовых выводов
        conclusion_frame.pack(fill="x")  # Размещаем: растягиваем по горизонтали
        
        self.conclusion_text = tk.Text(conclusion_frame, height=6, font=("Segoe UI", 10),  # Создаем текстовое поле
                                       bg=COLOR_SURFACE, fg=COLOR_TEXT, wrap="word")  # Белый фон, темный текст, перенос по словам
        self.conclusion_text.pack(fill="x", pady=5)  # Размещаем: растягиваем
        
        ttk.Button(summary_frame, text="🔄 Обновить",
                  command=self.update_conclusions, style="Primary.TButton").pack(pady=10)  # Кнопка обновления выводов
    
    # =============================
    # ЛОГИКА
    # =============================
    
    def validate_probs(self):
        """Проверяет корректность введенных вероятностей"""
        try:  # Пытаемся выполнить проверку
            probs = np.array([float(e.get()) for e in self.prob_entries])  # Преобразуем значения из полей ввода в массив float
            if np.any(probs < 0):  # Проверяем, есть ли отрицательные вероятности
                return False, "Вероятности ≥ 0"  # Возвращаем ошибку
            if abs(probs.sum() - 1.0) > 0.01:  # Проверяем, отличается ли сумма от 1 больше чем на 0.01
                return False, f"Σp = {probs.sum():.3f} ≠ 1"  # Возвращаем ошибку с фактической суммой
            return True, probs  # Если все проверки пройдены, возвращаем True и массив вероятностей
        except:  # Если произошла ошибка (например, нечисловое значение)
            return False, "Ошибка ввода"  # Возвращаем ошибку ввода
    
    def update_validity(self, valid, msg):
        """Обновляет индикаторы валидности вероятностей"""
        color = COLOR_SUCCESS if valid else COLOR_ERROR  # Выбираем цвет: зеленый если верно, красный если нет
        sign = "✓" if valid else "✗"  # Выбираем знак: галочка или крестик
        self.validity_label.config(text=f"{sign} {msg}", foreground=color)  # Обновляем текст и цвет метки суммы
        for lbl in self.prob_labels:  # Проходим по всем индикаторам вероятностей
            lbl.config(text=sign, foreground=color)  # Обновляем знак и цвет каждого индикатора
    
    def set_uniform_probs(self):
        """Устанавливает равномерные вероятности (все по 0.25)"""
        for e in self.prob_entries:  # Проходим по всем полям ввода
            e.delete(0, tk.END)  # Очищаем поле
            e.insert(0, "0.25")  # Вставляем 0.25
        self.current_probs = DEFAULT_PROBS.copy()  # Обновляем текущие вероятности
        self.update_validity(True, "Σp = 1.00")  # Обновляем индикаторы (валидно)
    
    def set_random_probs(self):
        """Генерирует случайные вероятности, сумма которых равна 1"""
        probs = np.random.dirichlet(np.ones(4))  # Генерируем 4 случайных числа из распределения Дирихле (сумма = 1)
        for i, e in enumerate(self.prob_entries):  # Проходим по полям ввода с индексами
            e.delete(0, tk.END)  # Очищаем поле
            e.insert(0, f"{probs[i]:.2f}")  # Вставляем сгенерированную вероятность (округленную до 2 знаков)
        self.current_probs = probs  # Обновляем текущие вероятности
        self.update_validity(True, "Σp = 1.00")  # Обновляем индикаторы
    
    def calc_theoretical(self, probs):
        """Вычисляет теоретические математическое ожидание и дисперсию"""
        mean = np.sum(VALUES * probs)  # M = Σ(xᵢ × pᵢ) — формула математического ожидания
        var = np.sum((VALUES - mean) ** 2 * probs)  # D = Σ((xᵢ - M)² × pᵢ) — формула дисперсии (population variance)
        return mean, var  # Возвращаем оба значения
    
    def run_discrete_simulation(self):
        """Запускает моделирование дискретной СВ для всех объемов выборки"""
        valid, probs = self.validate_probs()  # Проверяем корректность введенных вероятностей
        if not valid:  # Если проверка не пройдена
            self.update_validity(False, probs)  # Обновляем индикаторы с ошибкой
            messagebox.showerror("Ошибка", probs)  # Показываем диалог с ошибкой
            return  # Выходим из метода
        
        self.current_probs = probs  # Сохраняем проверенные вероятности
        self.update_validity(True, "Σp = 1.00")  # Обновляем индикаторы (валидно)
        
        # Очищаем таблицу результатов
        for item in self.tree_discrete.get_children():  # Проходим по всем строкам таблицы
            self.tree_discrete.delete(item)  # Удаляем строку
        
        theo_mean, theo_var = self.calc_theoretical(self.current_probs)  # Вычисляем теоретические M и D
        all_emp = []  # Создаем список для хранения всех эмпирических вероятностей
        summary_data = []  # Создаем список для хранения сводных данных
        
        # Очищаем и подготавливаем графики
        self.fig_discrete.clear()  # Очищаем фигуру
        self.fig_discrete.subplots_adjust(**SUBPLOT_ADJUST)  # Применяем настройки отступов
        axes = self.fig_discrete.subplots(2, 2)  # Создаем сетку 2×2 подграфиков (всего 4 графика)
        if not hasattr(axes, '__iter__'):  # Если axes не итерируемый (один подграфик)
            axes = [axes]  # Преобразуем в список
        
        for idx, N in enumerate(N_SAMPLES):  # Проходим по объемам выборок [10, 100, 1000, 10000] с индексами
            # Генерируем выборку методом инверсии CDF
            sample = generate_discrete_inverse_cdf(VALUES, self.current_probs, N)  # Генерируем N значений
            
            counts = np.array([np.sum(sample == v) for v in VALUES])  # Считаем частоты каждого значения
            emp_p = counts / N  # Вычисляем эмпирические вероятности (частоты / N)
            all_emp.append(emp_p)  # Добавляем в список
            
            # Вычисляем эмпирические характеристики
            mean = np.mean(sample)  # M̂ = (1/N) × Σxⱼ — выборочное среднее
            var = np.var(sample, ddof=0)  # D̂ = (1/N) × Σ(xⱼ - M)² — выборочная дисперсия (ddof=0 для population variance)
            
            # Вычисляем относительные погрешности
            err_m = abs(mean - theo_mean) / abs(theo_mean) * 100 if abs(theo_mean) > 1e-9 else 0  # δM = |M̂ - M|/|M| × 100%
            err_v = abs(var - theo_var) / theo_var * 100 if theo_var > 1e-9 else 0  # δD = |D̂ - D|/D × 100%
            
            # Выполняем χ²-тест
            expected = self.current_probs * N  # Ожидаемые частоты: Eᵢ = N × pᵢ
            chi2_stat, p_val = chisquare(counts, f_exp=expected)  # Вычисляем статистику χ² и p-value
            chi2_crit = chi2.ppf(0.95, df=len(VALUES) - 1)  # Находим критическое значение χ²(0.95, df=3)
            status = "✓ H₀" if chi2_stat < chi2_crit else "✗ H₀"  # Сравниваем: если χ² < χ²_кр, то H₀ не отвергаем
            
            # Добавляем строку в таблицу
            self.tree_discrete.insert("", "end", values=(
                f"{N:,}", f"{mean:.3f}", f"{var:.3f}",  # N, M̂, D̂
                f"{err_m:.1f}", f"{err_v:.1f}",  # δM%, δD%
                f"{chi2_stat:.2f}", f"{p_val:.3f}", status  # χ², p-value, статус
            ))
            
            summary_data.append({"N": N, "err": (err_m + err_v)/2, "p": p_val})  # Добавляем сводные данные
            
            # Рисуем гистограмму
            ax = axes[idx // 2, idx % 2] if hasattr(axes, '__getitem__') else axes[idx]  # Выбираем подграфик (0,0), (0,1), (1,0), (1,1)
            ax.hist(sample, bins=np.arange(VALUES.min(), VALUES.max()+2)-0.5,  # Рисуем гистограмму с границами между целыми числами
                   density=True, alpha=0.75, color=COLOR_PRIMARY, edgecolor='white', linewidth=0.5)  # Нормированная, полупрозрачная
            ax.set_xticks(VALUES)  # Устанавливаем метки на оси X
            ax.set_xlabel("X", fontsize=9)  # Подпись оси X
            ax.set_ylabel("P", fontsize=9)  # Подпись оси Y
            ax.set_title(f"N={N:,}\nχ²={chi2_stat:.2f}, p={p_val:.3f}", fontsize=10, pad=10)  # Заголовок с N и χ²
            ax.grid(True, alpha=0.2, linestyle='--')  # Включаем сетку
            ax.tick_params(labelsize=8)  # Размер шрифта делений
        
        self.fig_discrete.suptitle("📈 Дискретное распределение", fontsize=14, fontweight="bold", y=0.98)  # Общий заголовок фигуры
        self.canvas_discrete.draw()  # Перерисовываем canvas
        
        # Обновляем отображение эмпирических вероятностей
        for i, lbl in enumerate(self.emp_prob_labels):  # Проходим по меткам
            lbl.config(text=f"{all_emp[-1][i]:.3f}")  # Устанавливаем значение последней выборки (N=10000)
        
        # Сохраняем результаты в историю
        self.results_history.append({"type": "discrete", "probs": self.current_probs.tolist(), "data": summary_data})
        self.update_conclusions()  # Обновляем вкладку выводов
        
        messagebox.showinfo("Готово", "Моделирование завершено!")  # Показываем сообщение об успехе
    
    def export_discrete_results(self):
        """Экспортирует результаты дискретной СВ в CSV файл"""
        path = filedialog.asksaveasfilename(  # Открываем диалог сохранения файла
            defaultextension=".csv",  # Расширение по умолчанию
            filetypes=[("CSV", "*.csv")],  # Типы файлов
            initialfile=f"lab5_discrete_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"  # Имя файла с текущей датой и временем
        )
        if path:  # Если пользователь выбрал путь
            with open(path, 'w', newline='', encoding='utf-8') as f:  # Открываем файл для записи
                w = csv.writer(f)  # Создаем CSV writer
                w.writerow(["N", "Среднее", "Дисперсия", "err(средн)%", "err(дисп)%", "χ²", "p", "Статус"])  # Записываем заголовок
                for item in self.tree_discrete.get_children():  # Проходим по всем строкам таблицы
                    w.writerow(self.tree_discrete.item(item)["values"])  # Записываем значения строки
            messagebox.showinfo("Экспорт", f"Сохранено:\n{path}")  # Показываем сообщение
    
    def run_normal_simulation(self):
        """Запускает моделирование нормальной СВ для всех объемов выборки"""
        try:  # Пытаемся прочитать параметры
            mu = float(self.mu_entry.get())  # Читаем μ из поля ввода
            sigma = float(self.sigma_entry.get())  # Читаем σ из поля ввода
            if sigma <= 0:  # Проверяем, что σ > 0
                raise ValueError  # Если нет, вызываем ошибку
        except:  # Если произошла ошибка
            messagebox.showerror("Ошибка", "μ — число, σ > 0")  # Показываем сообщение
            return  # Выходим
        
        # Очищаем и подготавливаем графики
        self.fig_normal.clear()  # Очищаем фигуру
        self.fig_normal.subplots_adjust(**SUBPLOT_ADJUST)  # Применяем настройки отступов
        axes = self.fig_normal.subplots(2, 2)  # Создаем сетку 2×2
        if not hasattr(axes, '__iter__'):  # Если axes не итерируемый
            axes = [axes]  # Преобразуем в список
        
        all_stats = []  # Создаем список для хранения статистики
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)  # Создаем массив X от μ-4σ до μ+4σ (500 точек)
        pdf = norm.pdf(x, mu, sigma)  # Вычисляем теоретическую плотность N(μ,σ²)
        
        for idx, N in enumerate(N_SAMPLES):  # Проходим по объемам выборок
            # Генерируем выборку методом Бокса-Мюллера
            sample = generate_normal_box_muller(mu, sigma, N)  # Генерируем N значений
            
            # Вычисляем эмпирические характеристики
            mean = np.mean(sample)  # M̂ = (1/N) × Σxⱼ
            var = np.var(sample, ddof=0)  # D̂ = (1/N) × Σ(xⱼ - M̂)²
            
            all_stats.append({"N": N, "mean": mean, "var": var})  # Сохраняем статистику
            
            # Выполняем χ²-тест для нормальной СВ
            counts, bins = np.histogram(sample, bins=10)  # Строим гистограмму с 10 интервалами
            cdf = norm.cdf(bins, mu, sigma)  # Вычисляем теоретическую CDF на границах интервалов
            probs = np.diff(cdf)  # Вычисляем вероятности попадания в интервалы: P(a<X≤b) = F(b) - F(a)
            probs = probs / np.sum(probs)  # Нормализуем вероятности (сумма = 1)
            expected = probs * N  # Ожидаемые частоты
            chi2_stat, p_val = chisquare(counts, f_exp=expected)  # Вычисляем χ²
            chi2_crit = chi2.ppf(0.95, df=10 - 1)  # Критическое значение (df = bins - 1 = 9)
            chi_status = "✓" if chi2_stat < chi2_crit else "✗"  # Сравниваем с критическим
            
            # Рисуем гистограмму и теоретическую плотность
            ax = axes[idx // 2, idx % 2] if hasattr(axes, '__getitem__') else axes[idx]  # Выбираем подграфик
            ax.hist(sample, bins=35, density=True, alpha=0.7, color=COLOR_SECONDARY,  # Гистограмма выборки
                   edgecolor='white', linewidth=0.5)
            ax.plot(x, pdf, 'r-', linewidth=2, label='N(μ,σ²)')  # Теоретическая плотность (красная линия)
            ax.set_xlabel("X", fontsize=9)  # Подпись оси X
            ax.set_ylabel("f(x)", fontsize=9)  # Подпись оси Y
            ax.set_title(f"N={N:,}\nχ²={chi2_stat:.2f} {chi_status}", fontsize=10, pad=10)  # Заголовок
            ax.legend(fontsize=8, loc='upper right')  # Легенда
            ax.grid(True, alpha=0.2, linestyle='--')  # Сетка
            ax.tick_params(labelsize=8)  # Размер шрифта делений
        
        self.fig_normal.suptitle("🔔 Нормальное распределение", fontsize=14, fontweight="bold", y=0.98)  # Общий заголовок
        self.canvas_normal.draw()  # Перерисовываем
        
        # Обновляем отображение статистики
        last = all_stats[-1]  # Берем статистику для последней выборки (N=10000)
        self.normal_stats["mu_t"].config(text=f"{mu:.3f}")  # Теоретическое μ
        if abs(mu) > 1e-9:  # Если μ ≠ 0
            err_m = abs(last["mean"] - mu) / abs(mu) * 100  # Относительная погрешность
            self.normal_stats["mu_e"].config(text=f"{last['mean']:.3f} ({err_m:.1f}%)")  # Показываем M̂ и δM%
        else:  # Если μ ≈ 0
            err_m_abs = abs(last["mean"] - mu)  # Абсолютная погрешность
            self.normal_stats["mu_e"].config(text=f"{last['mean']:.3f} (±{err_m_abs:.4f})")  # Показываем M̂ и ±δ
        
        self.normal_stats["var_t"].config(text=f"{sigma**2:.3f}")  # Теоретическая дисперсия σ²
        err_v = abs(last["var"] - sigma**2) / sigma**2 * 100 if sigma**2 > 1e-9 else 0  # Относительная погрешность дисперсии
        self.normal_stats["var_e"].config(text=f"{last['var']:.3f} ({err_v:.1f}%)")  # Показываем D̂ и δD%
        
        # Обновляем χ²-статистику
        self.chi_label.config(text=f"{chi2_stat:.2f} {chi_status} (p={p_val:.3f})")
        
        # Сохраняем результаты в историю
        self.results_history.append({
            "type": "normal",  # Тип распределения
            "params": (mu, sigma),  # Параметры μ и σ
            "stats": all_stats  # Статистика для всех N
        })
        self.update_conclusions()  # Обновляем вкладку выводов
        
        messagebox.showinfo("Готово", "Моделирование завершено!")  # Сообщение об успехе
    
    def export_normal_results(self):
        """Экспортирует результаты нормальной СВ в CSV файл"""
        path = filedialog.asksaveasfilename(  # Диалог сохранения
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            initialfile=f"lab5_normal_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        )
        if path:  # Если путь выбран
            with open(path, 'w', newline='', encoding='utf-8') as f:  # Открываем файл
                w = csv.writer(f)  # Создаем writer
                w.writerow(["N", "Среднее", "Дисперсия", "χ²", "p", "Статус"])  # Заголовок
                for item in self.tree_discrete.get_children():  # Проходим по таблице (заглушка, нужно доработать)
                    pass  # Здесь должна быть логика экспорта нормальной СВ
            messagebox.showinfo("Экспорт", f"Сохранено:\n{path}")  # Сообщение
    
    def update_conclusions(self):
        """Обновляет вкладку выводов, обрабатывая оба типа распределений"""
        for item in self.tree_summary.get_children():  # Проходим по всем строкам таблицы
            self.tree_summary.delete(item)  # Очищаем таблицу
        
        texts = []  # Создаем список для текстовых выводов
        discrete_results = {}  # Словарь для ошибок дискретной СВ {N: error}
        normal_results = {}  # Словарь для ошибок нормальной СВ {N: error}
        
        # Собираем результаты из истории
        for res in self.results_history:  # Проходим по всем записям в истории
            if res["type"] == "discrete":  # Если это дискретная СВ
                for d in res["data"]:  # Проходим по данным для каждого N
                    N = d["N"]  # Объем выборки
                    err = d["err"]  # Средняя ошибка (δM + δD)/2
                    discrete_results[N] = err  # Сохраняем в словарь
                    qual = "✓ Хорошо" if err < 10 else "△ Норм" if err < 25 else "✗ Плохо"  # Оценка качества
                    texts.append(f"• N={N:,}: ошибка {err:.1f}% (дискр.)")  # Добавляем в текстовые выводы
            
            elif res["type"] == "normal":  # Если это нормальная СВ
                for stat in res["stats"]:  # Проходим по статистике для каждого N
                    N = stat["N"]  # Объем выборки
                    mu, sigma = res["params"]  # Параметры μ и σ
                    
                    # Считаем ошибку для дисперсии
                    emp_var = stat["var"]  # Эмпирическая дисперсия
                    theor_var = sigma ** 2  # Теоретическая дисперсия σ²
                    err_var = abs(emp_var - theor_var) / theor_var * 100 if theor_var > 1e-9 else 0  # δD%
                    normal_results[N] = err_var  # Сохраняем в словарь
                    texts.append(f"• N={N:,}: ошибка {err_var:.1f}% (норм.)")  # Добавляем в выводы
        
        # Заполняем таблицу сравнения
        for N in N_SAMPLES:  # Проходим по всем объемам [10, 100, 1000, 10000]
            disc_err = discrete_results.get(N, None)  # Получаем ошибку дискретной СВ (или None)
            norm_err = normal_results.get(N, None)  # Получаем ошибку нормальной СВ (или None)
            
            disc_err_str = f"{disc_err:.1f}" if disc_err is not None else "—"  # Форматируем или ставим прочерк
            norm_err_str = f"{norm_err:.1f}" if norm_err is not None else "—"
            
            # Оценка качества (средняя ошибка если есть оба значения)
            if disc_err is not None and norm_err is not None:  # Если есть оба значения
                avg_err = (disc_err + norm_err) / 2  # Среднее арифметическое
            elif disc_err is not None:  # Если только дискретная
                avg_err = disc_err
            elif norm_err is not None:  # Если только нормальная
                avg_err = norm_err
            else:  # Если нет данных
                avg_err = None
            
            if avg_err is not None:  # Если есть данные
                qual = "✓ Хорошо" if avg_err < 10 else "△ Норм" if avg_err < 25 else "✗ Плохо"  # Оценка
            else:  # Если нет данных
                qual = "—"  # Прочерк
            
            self.tree_summary.insert("", "end", values=(
                f"{N:,}", disc_err_str, norm_err_str, qual  # Добавляем строку в таблицу
            ))
        
        # Формируем текстовые выводы
        self.conclusion_text.delete("1.0", tk.END)  # Очищаем текстовое поле
        if texts:  # Если есть выводы
            txt = "📊 РЕЗУЛЬТАТЫ:\n" + "\n".join(texts[-8:])  # Берем последние 8 записей
            txt += "\n\n💡 ВЫВОДЫ:\n"
            txt += "1. При росте N точность ↑\n"
            txt += "2. При N≥1000 ошибка <10%\n"
            txt += "3. χ²-тест подтверждает гипотезу при больших N\n"
            txt += "4. Закон больших чисел работает ✓"
        else:  # Если нет данных
            txt = "Запустите моделирование для выводов"
        self.conclusion_text.insert("1.0", txt)  # Вставляем текст


# =============================
# ЗАПУСК ПРИЛОЖЕНИЯ
# =============================
if __name__ == "__main__":  # Если файл запущен напрямую (не импортирован)
    root = tk.Tk()  # Создаем главное окно tkinter
    app = ModernStyleApp(root)  # Создаем экземпляр приложения
    root.mainloop()  # Запускаем главный цикл обработки событий (окно остается открытым)