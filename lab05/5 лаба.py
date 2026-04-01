import tkinter as tk
from tkinter import ttk
import random
import math

# =============================
# ЦВЕТОВАЯ ПАЛИТРА
# =============================
COLOR_BG = "#FFE5B4"
COLOR_SURFACE = "#FFF3E0"
COLOR_PRIMARY = "#FF8A65"
COLOR_TEXT = "#5D4037"
COLOR_ACCENT_YES = "#4CAF50"
COLOR_ACCENT_NO = "#F44336"
COLOR_SPLASH_BG = "#FFCCBC"

root = tk.Tk()
root.title("Magic Ball")
root.geometry("650x650")
root.configure(bg=COLOR_BG)
root.resizable(False, False)

# =============================
# ВКЛАДКИ
# =============================
style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background=COLOR_BG, borderwidth=0)
style.configure("TNotebook.Tab", background=COLOR_SURFACE, foreground=COLOR_TEXT, 
                font=("Segoe UI", 12, "bold"), padding=20)
style.map("TNotebook.Tab", 
          background=[("selected", COLOR_PRIMARY)], 
          foreground=[("selected", "white")])

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=20, pady=20)

# =============================
# ВКЛАДКА 1: ДА / НЕТ (С КОТИКОМ)
# =============================
frame_yesno = tk.Frame(notebook, bg=COLOR_BG)
notebook.add(frame_yesno, text="  🐱 Да / Нет  ")

yn_title = tk.Label(frame_yesno, 
                    text="🎯 Спроси котика", 
                    font=("Segoe UI", 20, "bold"), 
                    bg=COLOR_BG, 
                    fg=COLOR_TEXT)
yn_title.pack(pady=10)

q_entry_yn = tk.Entry(frame_yesno, font=("Segoe UI", 12), bg=COLOR_SURFACE, fg=COLOR_TEXT, 
                      insertbackground=COLOR_PRIMARY, relief="flat", justify="center")
q_entry_yn.pack(pady=10, ipadx=150, ipady=8)

# Canvas для котика
cat_canvas = tk.Canvas(frame_yesno, width=400, height=350, bg=COLOR_BG, highlightthickness=0)
cat_canvas.pack(pady=10)

cat_center_x = 200
cat_center_y = 175

# Элементы котика
cat_items = {}

def draw_cat():
    """Рисуем милого котика"""
    cat_canvas.delete("all")
    
    # Тело котика (овал)
    cat_items['body'] = cat_canvas.create_oval(
        cat_center_x-80, cat_center_y-20, 
        cat_center_x+80, cat_center_y+100, 
        fill="#FFB74D", outline="#E65100", width=3
    )
    
    # Голова
    cat_items['head'] = cat_canvas.create_oval(
        cat_center_x-70, cat_center_y-90, 
        cat_center_x+70, cat_center_y+10, 
        fill="#FFB74D", outline="#E65100", width=3
    )
    
    # Уши
    cat_canvas.create_polygon(
        cat_center_x-60, cat_center_y-70,
        cat_center_x-50, cat_center_y-110,
        cat_center_x-20, cat_center_y-85,
        fill="#FFB74D", outline="#E65100", width=2
    )
    cat_canvas.create_polygon(
        cat_center_x+60, cat_center_y-70,
        cat_center_x+50, cat_center_y-110,
        cat_center_x+20, cat_center_y-85,
        fill="#FFB74D", outline="#E65100", width=2
    )
    
    # Внутренняя часть ушей
    cat_canvas.create_polygon(
        cat_center_x-55, cat_center_y-72,
        cat_center_x-48, cat_center_y-95,
        cat_center_x-25, cat_center_y-82,
        fill="#FFCCBC", outline=""
    )
    cat_canvas.create_polygon(
        cat_center_x+55, cat_center_y-72,
        cat_center_x+48, cat_center_y-95,
        cat_center_x+25, cat_center_y-82,
        fill="#FFCCBC", outline=""
    )
    
    # Глаза
    cat_items['eye_left'] = cat_canvas.create_oval(
        cat_center_x-45, cat_center_y-50,
        cat_center_x-20, cat_center_y-25,
        fill="white", outline="#5D4037", width=2
    )
    cat_items['eye_right'] = cat_canvas.create_oval(
        cat_center_x+20, cat_center_y-50,
        cat_center_x+45, cat_center_y-25,
        fill="white", outline="#5D4037", width=2
    )
    
    # Зрачки
    cat_items['pupil_left'] = cat_canvas.create_oval(
        cat_center_x-38, cat_center_y-45,
        cat_center_x-27, cat_center_y-30,
        fill="#5D4037"
    )
    cat_items['pupil_right'] = cat_canvas.create_oval(
        cat_center_x+27, cat_center_y-45,
        cat_center_x+38, cat_center_y-30,
        fill="#5D4037"
    )
    
    # Нос
    cat_canvas.create_polygon(
        cat_center_x-8, cat_center_y-15,
        cat_center_x+8, cat_center_y-15,
        cat_center_x, cat_center_y-5,
        fill="#FF8A65", outline=""
    )
    
    # Рот
    cat_canvas.create_arc(
        cat_center_x-20, cat_center_y-10,
        cat_center_x+20, cat_center_y+5,
        start=180, extent=180, style=tk.ARC, outline="#5D4037", width=2
    )
    
    # Усы
    cat_canvas.create_line(cat_center_x-70, cat_center_y-25, cat_center_x-110, cat_center_y-30, fill="#5D4037", width=2)
    cat_canvas.create_line(cat_center_x-70, cat_center_y-18, cat_center_x-110, cat_center_y-18, fill="#5D4037", width=2)
    cat_canvas.create_line(cat_center_x-70, cat_center_y-10, cat_center_x-110, cat_center_y-5, fill="#5D4037", width=2)
    cat_canvas.create_line(cat_center_x+70, cat_center_y-25, cat_center_x+110, cat_center_y-30, fill="#5D4037", width=2)
    cat_canvas.create_line(cat_center_x+70, cat_center_y-18, cat_center_x+110, cat_center_y-18, fill="#5D4037", width=2)
    cat_canvas.create_line(cat_center_x+70, cat_center_y-10, cat_center_x+110, cat_center_y-5, fill="#5D4037", width=2)

    
    # Задние лапки
    cat_canvas.create_oval(cat_center_x-75, cat_center_y+70, cat_center_x-45, cat_center_y+95, 
                           fill="#FFB74D", outline="#E65100", width=2)
    cat_canvas.create_oval(cat_center_x+45, cat_center_y+70, cat_center_x+75, cat_center_y+95, 
                           fill="#FFB74D", outline="#E65100", width=2)
    
    # Табличка с ответом 
    cat_items['sign'] = cat_canvas.create_rectangle(
        cat_center_x-70, cat_center_y+20,
        cat_center_x+70, cat_center_y+70,
        fill="white", outline="#5D4037", width=3, state='hidden'
    )
    
    cat_items['sign_text'] = cat_canvas.create_text(
        cat_center_x, cat_center_y+45,
        text="",
        font=("Segoe UI", 16, "bold"),
        fill="#5D4037",
        state='hidden'
    )
    

draw_cat()

def get_weighted_result(answers):
    rand_val = random.random()
    cumulative = 0.0
    for name, probability in answers:
        cumulative += probability
        if rand_val <= cumulative:
            return name
    return answers[-1][0]

def ask_yes_no():
    btn_yn.config(state="disabled", text="Думаю...")
    # Анимация "думания" - котик моргает
    for i in range(3):
        root.after(i*200, lambda: cat_canvas.itemconfig(cat_items['eye_left'], fill="#FFB74D"))
        root.after(i*200+100, lambda: cat_canvas.itemconfig(cat_items['eye_left'], fill="white"))
        root.after(i*200, lambda: cat_canvas.itemconfig(cat_items['eye_right'], fill="#FFB74D"))
        root.after(i*200+100, lambda: cat_canvas.itemconfig(cat_items['eye_right'], fill="white"))
    
    root.after(800, finish_yes_no)

def finish_yes_no():
    yes_no_answers = [("ДА", 0.5), ("НЕТ", 0.5)]
    result = get_weighted_result(yes_no_answers)
    
    # Показываем табличку
    cat_canvas.itemconfig(cat_items['sign'], state='normal')
    cat_canvas.itemconfig(cat_items['sign_text'], state='normal', text=result)
    cat_canvas.itemconfig('stick', state='normal')
    
    # Цвет таблички в зависимости от ответа
    sign_color = "#C8E6C9" if result == "ДА" else "#FFCDD2"
    text_color = COLOR_ACCENT_YES if result == "ДА" else COLOR_ACCENT_NO
    cat_canvas.itemconfig(cat_items['sign'], fill=sign_color, outline=text_color)
    cat_canvas.itemconfig(cat_items['sign_text'], fill=text_color)
    
    btn_yn.config(state="normal", text="✨ СПРОСИТЬ ЕЩЁ ✨")

btn_yn = tk.Button(frame_yesno, text="✨ СПРОСИТЬ ✨", command=ask_yes_no,
                   font=("Segoe UI", 12, "bold"), bg=COLOR_PRIMARY, fg="white",
                   activebackground="#FF7043", relief="flat", padx=30, pady=10, cursor="hand2")
btn_yn.pack(pady=15)

# =============================
# ВКЛАДКА 2: MAGIC 8-BALL С БЛЕСТКАМИ
# =============================
frame_magic = tk.Frame(notebook, bg=COLOR_BG)
notebook.add(frame_magic, text="  🔮 Magic Ball  ")

magic_title = tk.Label(frame_magic, 
                       text="🔮 Волшебная сфера", 
                       font=("Segoe UI", 20, "bold"), 
                       bg=COLOR_BG, 
                       fg=COLOR_TEXT)
magic_title.pack(pady=10)

q_entry_magic = tk.Entry(frame_magic, font=("Segoe UI", 12), bg=COLOR_SURFACE, fg=COLOR_TEXT, 
                         insertbackground=COLOR_PRIMARY, relief="flat", justify="center")
q_entry_magic.pack(pady=10, ipadx=150, ipady=8)

magic_canvas = tk.Canvas(frame_magic, width=400, height=400, bg=COLOR_BG, highlightthickness=0)
magic_canvas.pack(pady=10)

magic_center = 200
magic_radius = 150

# Рисуем волшебный шар с градиентом
for i in range(30, 0, -1):
    alpha = i / 30
    r = int(100 * alpha + 255 * (1-alpha))
    g = int(50 * alpha + 200 * (1-alpha))
    b = int(150 * alpha + 255 * (1-alpha))
    color = f"#{r:02x}{g:02x}{b:02x}"
    size = i * 5
    magic_canvas.create_oval(
        magic_center-size, magic_center-size,
        magic_center+size, magic_center+size,
        fill=color, outline=""
    )

# Основной шар
magic_canvas.create_oval(
    magic_center-magic_radius, magic_center-magic_radius,
    magic_center+magic_radius, magic_center+magic_radius,
    fill="#1A237E", outline="#7E57C2", width=4
)

# Внутренний круг (окошко)
inner_circle = magic_canvas.create_oval(
    magic_center-90, magic_center-90,
    magic_center+90, magic_center+90,
    fill="#283593", outline="#9FA8DA", width=3
)

# Текст ответа
magic_text = magic_canvas.create_text(
    magic_center, magic_center,
    text="",
    fill="white",
    font=("Segoe UI", 14, "bold"),
    justify="center"
)

# Блик на шаре
magic_canvas.create_oval(
    magic_center-100, magic_center-100,
    magic_center-40, magic_center-40,
    fill="white", stipple="gray50", outline=""
)

# Система частиц (блестки)
particles = []

class Particle:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = random.randint(3, 8)
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(3, 8)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = 1.0
        self.decay = random.uniform(0.02, 0.04)
        colors = ["#FFD700", "#FFA500", "#FF69B4", "#00CED1", "#FFFFFF", "#FFD700"]
        self.color = random.choice(colors)
        self.item = canvas.create_oval(
            x-self.size, y-self.size,
            x+self.size, y+self.size,
            fill=self.color, outline=""
        )
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1  # гравитация
        self.life -= self.decay
        self.vx *= 0.98  # сопротивление воздуха
        self.vy *= 0.98
        
        alpha = int(255 * self.life)
        size = int(self.size * self.life)
        
        if size > 0:
            self.canvas.coords(
                self.item,
                self.x-size, self.y-size,
                self.x+size, self.y+size
            )
            self.canvas.itemconfig(self.item, fill=self.color)
        
        return self.life > 0
    
    def destroy(self):
        self.canvas.delete(self.item)

def create_sparkles():
    """Создаем взрыв блесток"""
    global particles
    for _ in range(50):  # 50 частиц
        particle = Particle(magic_canvas, magic_center, magic_center)
        particles.append(particle)

def animate_sparkles():
    """Анимация блесток"""
    global particles
    particles = [p for p in particles if p.update()]
    if particles:
        magic_canvas.after(30, animate_sparkles)

magic_answers = [
    ("Да", 0.15), ("Нет", 0.15), ("Скорее всего", 0.1), ("Сомнительно", 0.1),
    ("Без сомнений", 0.1), ("Спроси позже", 0.15), ("Определенно да", 0.1), ("Маловероятно", 0.15)
]

spinning = False
current_angle = 0

def spin_animation(step=0, total_steps=40):
    global current_angle, spinning
    if step < total_steps:
        angle_step = (2 * math.pi / total_steps) * (1 - step/total_steps)
        current_angle += angle_step
        # Поворот внутреннего круга (визуальный эффект)
        magic_canvas.coords(inner_circle,
            magic_center-90*math.cos(current_angle), magic_center-90*math.sin(current_angle),
            magic_center+90*math.cos(current_angle), magic_center+90*math.sin(current_angle)
        )
        magic_canvas.itemconfig(magic_text, text="")
        root.after(20, spin_animation, step+1, total_steps)
    else:
        spinning = False
        show_prediction()

def fade_in_text(text, alpha=0.0):
    if alpha <= 1.0:
        brightness = int(255 * alpha)
        color = f"#{brightness:02x}{brightness:02x}{brightness:02x}"
        magic_canvas.itemconfig(magic_text, text=text, fill=color)
        if alpha < 1.0:
            root.after(40, fade_in_text, text, alpha+0.1)

def show_prediction():
    result = get_weighted_result(magic_answers)
    fade_in_text(result)
    create_sparkles()  
    animate_sparkles()  

def click_ball(event):
    global spinning
    if spinning: return
    spinning = True
    spin_animation()

magic_canvas.bind("<Button-1>", click_ball)

btn_magic = tk.Button(frame_magic, text="🔮 ПОЛУЧИТЬ ОТВЕТ 🔮", command=lambda: click_ball(None),
                      font=("Segoe UI", 12, "bold"), bg=COLOR_PRIMARY, fg="white",
                      activebackground="#FF7043", relief="flat", padx=30, pady=10, cursor="hand2")
btn_magic.pack(pady=15)

hint_label = tk.Label(frame_magic, text="(нажми на шар или кнопку)", 
                      bg=COLOR_BG, fg="#8D6E63", font=("Segoe UI", 9))
hint_label.pack(pady=5)

root.mainloop()