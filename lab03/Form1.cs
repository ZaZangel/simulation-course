// Подключение необходимых библиотек для работы с графикой и Windows Forms
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Lab_3
{
    // Основной класс формы приложения
    public partial class Form1 : Form
    {
        // Перечисление состояний каждой клетки на поле
        enum CellState { Empty = 0, Tree = 1, Fire = 2, Barrier = 3 }

        // Константа: размер сетки 50x50 клеток
        const int gridSize = 50;
        // Константа: размер одной клетки в пикселях (10x10)
        const int cellSize = 10;

        // Двумерный массив для хранения текущего состояния сетки
        int[,] grid;
        // Двумерный массив для хранения следующего состояния (для двойной буферизации)
        int[,] nextGrid;

        // Объект для генерации случайных чисел
        Random rand = new Random();
        // Флаг: работает ли симуляция в данный момент
        bool isRunning = false;

        // Флаги для включения/выключения дополнительных правил
        bool useWind = false;        // Правило ветра
        bool useLightning = false;   // Правило молний
        bool useBarrier = false;     // Правило реки (преграды)
        bool useHumidity = false;    // Правило влажности

        // Параметры моделирования
        double probTreeInitial = 0.65;    // Вероятность появления дерева при генерации леса (65%)
        double probGrowth = 0.01;         // Вероятность роста нового дерева на пустой клетке (1%)
        double probLightning = 0.003;     // Вероятность удара молнии в дерево (0.3%)
        double probCatchFire = 0.75;      // Базовая вероятность возгорания дерева от соседа (75%)

        int windDirection = 1;            // Направление ветра: 1 = вправо, -1 = влево, 0 = нет ветра
        double windBonus = 0.20;          // Бонус к вероятности возгорания по ветру (+20%)

        double humidity = 0.5;            // Уровень влажности (0.0 = сухо, 1.0 = очень влажно)

        // Конструктор формы - вызывается при создании окна
        public Form1()
        {
            // Инициализация всех компонентов интерфейса (кнопки, PictureBox и т.д.)
            InitializeComponent();
            // Инициализация симуляции: создание сетки и отрисовка
            InitializeSimulation();
            // Обновление информации об активных правилах
            UpdateRuleStatus();
        }

        // Метод начальной настройки симуляции
        private void InitializeSimulation()
        {
            // Создание двумерного массива для текущего состояния (50x50)
            grid = new int[gridSize, gridSize];
            // Создание двумерного массива для следующего состояния
            nextGrid = new int[gridSize, gridSize];
            // Генерация начального состояния леса
            GenerateForest();
            // Отрисовка сетки на экране
            DrawGrid();
            // Подписка на событие Tick таймера (вызывается каждые 150 мс)
            timerSim.Tick += TimerSim_Tick;
            // Установка интервала таймера: 150 миллисекунд между кадрами
            timerSim.Interval = 150;
        }

        // Метод генерации начального состояния леса
        private void GenerateForest()
        {
            // Проход по всем клеткам сетки по горизонтали (x от 0 до 49)
            for (int x = 0; x < gridSize; x++)
            {
                // Проход по всем клеткам сетки по вертикали (y от 0 до 49)
                for (int y = 0; y < gridSize; y++)
                {
                    // Если включено правило реки и текущая строка - середина поля
                    if (useBarrier && y == gridSize / 2)
                        // Создаём преграду (реку) - клетка не может гореть
                        grid[x, y] = (int)CellState.Barrier;
                    else
                        // С вероятностью 65% создаём дерево, иначе пустую клетку
                        grid[x, y] = rand.NextDouble() < probTreeInitial
                            ? (int)CellState.Tree
                            : (int)CellState.Empty;
                }
            }
        }

        // Метод отрисовки всей сетки на PictureBox
        private void DrawGrid()
        {
            // Создание нового Bitmap объекта размером с PictureBox (500x500 пикселей)
            Bitmap bmp = new Bitmap(pbGrid.Width, pbGrid.Height);
            // Создание объекта Graphics для рисования на Bitmap
            using (Graphics g = Graphics.FromImage(bmp))
            {
                // Проход по всем клеткам по горизонтали
                for (int x = 0; x < gridSize; x++)
                {
                    // Проход по всем клеткам по вертикали
                    for (int y = 0; y < gridSize; y++)
                    {
                        // Получение цвета для текущей клетки на основе её состояния
                        Color cellColor = GetCellColor((CellState)grid[x, y]);
                        // Рисование прямоугольника (клетки) нужного цвета
                        // x * cellSize и y * cellSize - координаты верхнего левого угла
                        // cellSize - 1 - ширина и высота (минус 1 для зазора между клетками)
                        g.FillRectangle(new SolidBrush(cellColor),
                            x * cellSize, y * cellSize, cellSize - 1, cellSize - 1);
                    }
                }
            }
            // Установка отрисованного Bitmap в качестве изображения PictureBox
            pbGrid.Image = bmp;
            // Обновление статистики (количество деревьев, огня и т.д.)
            UpdateStatistics();
        }

        // Метод получения цвета для каждого состояния клетки
        private Color GetCellColor(CellState state)
        {
            // Выбор цвета в зависимости от состояния клетки
            switch (state)
            {
                case CellState.Empty:
                    // Пустая клетка - чёрный цвет
                    return Color.Black;
                case CellState.Tree:
                    // Дерево - тёмно-зелёный цвет
                    return Color.ForestGreen;
                case CellState.Fire:
                    // Огонь - оранжево-красный цвет
                    return Color.OrangeRed;
                case CellState.Barrier:
                    // Преграда (река) - ярко-голубой цвет
                    return Color.DeepSkyBlue;
                default:
                    // По умолчанию - чёрный
                    return Color.Black;
            }
        }

        // Основной метод обновления состояния сетки (один шаг симуляции)
        private void UpdateGrid()
        {
            // Проход по всем клеткам сетки
            for (int x = 0; x < gridSize; x++)
            {
                for (int y = 0; y < gridSize; y++)
                {
                    // Получение текущего состояния клетки из массива
                    CellState current = (CellState)grid[x, y];

                    // Если клетка - преграда (река), она не меняется
                    if (current == CellState.Barrier)
                    {
                        // Сохраняем преграду в следующем состоянии
                        nextGrid[x, y] = (int)CellState.Barrier;
                        // Переходим к следующей клетке
                        continue;
                    }

                    // Обработка в зависимости от текущего состояния
                    switch (current)
                    {
                        case CellState.Fire:
                            // Горящее дерево становится пустой клеткой (сгорает)
                            nextGrid[x, y] = (int)CellState.Empty;
                            break;

                        case CellState.Tree:
                            // Для дерева вычисляем следующее состояние
                            nextGrid[x, y] = ProcessTree(x, y);
                            break;

                        case CellState.Empty:
                            // Пустая клетка: с вероятностью 1% вырастает новое дерево
                            nextGrid[x, y] = rand.NextDouble() < probGrowth
                                ? (int)CellState.Tree
                                : (int)CellState.Empty;
                            break;
                    }
                }
            }
            // Копирование следующего состояния в текущее (одновременное обновление всех клеток)
            Array.Copy(nextGrid, grid, grid.Length);
        }

        // Метод обработки состояния дерева (загорится ли оно)
        private int ProcessTree(int x, int y)
        {
            // Правило молнии: с вероятностью 0.3% дерево загорается случайно
            if (useLightning && rand.NextDouble() < probLightning)
                return (int)CellState.Fire;

            // Подсчёт количества горящих соседей и проверка направления ветра
            int fireNeighbors = CountFireNeighbors(x, y, out bool hasWindSideFire);

            // Если рядом нет горящих деревьев, дерево остаётся здоровым
            if (fireNeighbors == 0)
                return (int)CellState.Tree;

            // Вычисление вероятности возгорания с учётом всех правил
            double catchProb = CalculateCatchFireProbability(hasWindSideFire);

            // Возгорание с вычисленной вероятностью
            return rand.NextDouble() < catchProb
                ? (int)CellState.Fire
                : (int)CellState.Tree;
        }

        // Метод подсчёта горящих соседей вокруг клетки
        private int CountFireNeighbors(int x, int y, out bool hasWindSideFire)
        {
            // Счётчик количества горящих соседей
            int count = 0;
            // Флаг: есть ли огонь с наветренной стороны
            hasWindSideFire = false;

            // Проверка всех 8 соседних клеток (dx, dy от -1 до 1)
            for (int dx = -1; dx <= 1; dx++)
            {
                for (int dy = -1; dy <= 1; dy++)
                {
                    // Пропускаем саму клетку (dx=0, dy=0)
                    if (dx == 0 && dy == 0) continue;

                    // Вычисление координат соседней клетки
                    int nx = x + dx, ny = y + dy;
                    // Проверка, что сосед находится в пределах сетки
                    if (nx >= 0 && nx < gridSize && ny >= 0 && ny < gridSize)
                    {
                        // Если сосед горит
                        if (grid[nx, ny] == (int)CellState.Fire)
                        {
                            // Увеличиваем счётчик горящих соседей
                            count++;
                            // Если включен ветер и огонь находится по направлению ветра
                            if (useWind && windDirection != 0 && dx == windDirection && dy == 0)
                                // Устанавливаем флаг, что огонь с наветренной стороны
                                hasWindSideFire = true;
                        }
                    }
                }
            }
            // Возврат количества горящих соседей
            return count;
        }

        // Метод расчёта итоговой вероятности возгорания
        private double CalculateCatchFireProbability(bool hasWindSideFire)
        {
            // Начинаем с базовой вероятности (75%)
            double prob = probCatchFire;

            // Если включен ветер и огонь с наветренной стороны
            if (useWind && hasWindSideFire)
                // Увеличиваем вероятность на 20%
                prob += windBonus;

            // Если включена влажность
            if (useHumidity)
                // Уменьшаем вероятность пропорционально влажности
                // При влажности 100% вероятность снижается на 70%
                prob *= (1.0 - humidity * 0.7);

            // Возвращаем вероятность, но не более 100%
            return Math.Min(prob, 1.0);
        }

        // Обработчик события таймера (вызывается каждые 150 мс)
        private void TimerSim_Tick(object sender, EventArgs e)
        {
            // Обновление состояния сетки (один шаг симуляции)
            UpdateGrid();
            // Перерисовка сетки на экране
            DrawGrid();
        }

        // Метод обновления статистики (количество клеток каждого типа)
        private void UpdateStatistics()
        {
            // Счётчики для каждого типа клеток
            int trees = 0, fires = 0, empty = 0, barriers = 0;

            // Проход по всей сетке для подсчёта
            for (int x = 0; x < gridSize; x++)
                for (int y = 0; y < gridSize; y++)
                {
                    // Увеличиваем соответствующий счётчик в зависимости от состояния
                    switch ((CellState)grid[x, y])
                    {
                        case CellState.Tree: trees++; break;
                        case CellState.Fire: fires++; break;
                        case CellState.Empty: empty++; break;
                        case CellState.Barrier: barriers++; break;
                    }
                }

            // Обновление текста метки со статистикой
            lblStats.Text = $"🌲 Деревья: {trees}\n🔥 Огонь: {fires}\n⬛ Пусто: {empty}\n🌊 Река: {barriers}";
        }

        // Метод обновления статуса правил (какие правила активны)
        private void UpdateRuleStatus()
        {
            // Чтение состояния чекбоксов
            useWind = cbWind.Checked;
            useLightning = cbLightning.Checked;
            useBarrier = cbBarrier.Checked;
            useHumidity = cbHumidity.Checked;

            // Если включена река, пересоздаём лес с преградой
            if (useBarrier)
                GenerateForest();

            // Обновление текста с информацией о правилах
            UpdateRuleLabels();
        }

        // Метод обновления текстовой информации об активных правилах
        private void UpdateRuleLabels()
        {
            // Начальный текст
            string rules = "Активные правила:\n";
            // Счётчик активных правил
            int count = 0;

            // Добавление информации о каждом активном правиле
            if (useWind) { rules += $"🌬️ Ветер (→) +{windBonus * 100}%\n"; count++; }
            if (useLightning) { rules += $"⚡ Молнии {probLightning * 100:F1}%\n"; count++; }
            if (useBarrier) { rules += "🌊 Река (преграда)\n"; count++; }
            if (useHumidity) { rules += $"💧 Влажность {(1 - humidity) * 100:F0}%\n"; count++; }

            // Если ни одно правило не активно
            if (count == 0)
                rules += "• Базовая модель\n";
            // Если все 4 правила активны
            else if (count == 4)
                rules += "✅ ВСЕ правила активны!";

            // Установка текста в метку
            lblRules.Text = rules;
        }

        // Обработчик кнопки "Старт"
        private void btnStart_Click(object sender, EventArgs e)
        {
            // Если симуляция ещё не запущена
            if (!isRunning)
            {
                // Устанавливаем флаг запуска
                isRunning = true;
                // Включаем таймер (начнёт вызывать TimerSim_Tick)
                timerSim.Enabled = true;
                // Отключаем кнопку "Старт" (чтобы не нажали повторно)
                btnStart.Enabled = false;
                // Включаем кнопку "Стоп"
                btnStop.Enabled = true;
                // Отключаем кнопку "Сброс" во время симуляции
                btnReset.Enabled = false;
            }
        }

        // Обработчик кнопки "Стоп"
        private void btnStop_Click(object sender, EventArgs e)
        {
            // Останавливаем симуляцию
            isRunning = false;
            // Отключаем таймер
            timerSim.Enabled = false;
            // Включаем кнопку "Старт"
            btnStart.Enabled = true;
            // Отключаем кнопку "Стоп"
            btnStop.Enabled = false;
            // Включаем кнопку "Сброс"
            btnReset.Enabled = true;
        }

        // Обработчик кнопки "Сброс"
        private void btnReset_Click(object sender, EventArgs e)
        {
            // Останавливаем симуляцию (вызываем метод кнопки "Стоп")
            btnStop_Click(sender, e);
            // Генерируем новый лес
            GenerateForest();
            // Отрисовываем его
            DrawGrid();
        }

        // Обработчик кнопки "Поджечь (центр)"
        private void btnIgnite_Click(object sender, EventArgs e)
        {
            // Поджигаем область в центре поля (радиус 2 клетки)
            IgniteArea(gridSize / 2, gridSize / 2, 2);
        }

        // Обработчик кнопки "Случайные очаги"
        private void btnIgniteRandom_Click(object sender, EventArgs e)
        {
            // Создаём 3 случайных очага пожара
            for (int i = 0; i < 3; i++)
            {
                // Генерация случайных координат (с отступом 5 клеток от края)
                int rx = rand.Next(5, gridSize - 5);
                int ry = rand.Next(5, gridSize - 5);
                // Поджигание области радиусом 1 клетка
                IgniteArea(rx, ry, 1);
            }
        }

        // Метод поджигания области вокруг указанной точки
        private void IgniteArea(int cx, int cy, int radius)
        {
            // Проход по квадрату вокруг точки (cx, cy)
            for (int dx = -radius; dx <= radius; dx++)
                for (int dy = -radius; dy <= radius; dy++)
                {
                    // Вычисление координат соседней клетки
                    int nx = cx + dx, ny = cy + dy;
                    // Проверка, что клетка в пределах сетки
                    if (nx >= 0 && nx < gridSize && ny >= 0 && ny < gridSize)
                        // Если в клетке дерево, поджигаем его
                        if (grid[nx, ny] == (int)CellState.Tree)
                            grid[nx, ny] = (int)CellState.Fire;
                }
            // Перерисовываем поле с огнём
            DrawGrid();
        }

        // Обработчик клика мыши по полю
        private void pbGrid_MouseClick(object sender, MouseEventArgs e)
        {
            // Вычисление координаты X клетки (делим пиксели на размер клетки)
            int x = e.X / cellSize;
            // Вычисление координаты Y клетки
            int y = e.Y / cellSize;

            // Проверка, что клик в пределах сетки
            if (x >= 0 && x < gridSize && y >= 0 && y < gridSize)
            {
                // Если в клетке дерево
                if (grid[x, y] == (int)CellState.Tree)
                {
                    // Поджигаем его
                    grid[x, y] = (int)CellState.Fire;
                    // Перерисовываем поле
                    DrawGrid();
                }
            }
        }

        // Обработчик изменения состояния любого чекбокса правил
        private void Rule_CheckedChanged(object sender, EventArgs e)
            // Просто обновляем статус правил
            => UpdateRuleStatus();

        // Обработчик изменения ползунка влажности
        private void trackHumidity_Scroll(object sender, EventArgs e)
        {
            // Преобразование значения ползунка (0-100) в коэффициент (0.0-1.0)
            humidity = trackHumidity.Value / 100.0;
            // Обновление текстового значения (например, "50%")
            lblHumidityValue.Text = $"{trackHumidity.Value}%";
            // Обновление статуса правил (пересчёт вероятностей)
            UpdateRuleStatus();
        }

        // Обработчик изменения ползунка скорости
        private void trackSpeed_Scroll(object sender, EventArgs e)
        {
            // Изменение интервала таймера: от 50 мс (10x) до 275 мс (1x)
            timerSim.Interval = 300 - trackSpeed.Value * 25;
            // Обновление текстового значения скорости (например, "5x")
            lblSpeedValue.Text = $"{trackSpeed.Value}x";
        }

        // Обработчик кнопки "Все правила"
        private void btnAllRules_Click(object sender, EventArgs e)
        {
            // Включаем все чекбоксы
            cbWind.Checked = true;
            cbLightning.Checked = true;
            cbBarrier.Checked = true;
            cbHumidity.Checked = true;
            // Обновляем статус
            UpdateRuleStatus();
        }

        // Обработчик кнопки "Без правил"
        private void btnNoRules_Click(object sender, EventArgs e)
        {
            // Выключаем все чекбоксы
            cbWind.Checked = false;
            cbLightning.Checked = false;
            cbBarrier.Checked = false;
            cbHumidity.Checked = false;
            // Обновляем статус
            UpdateRuleStatus();
        }

        // Обработчик закрытия формы
        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            // Останавливаем таймер перед закрытием
            timerSim.Stop();
            // Вызов базового метода закрытия
            base.OnFormClosing(e);
        }
    }
}