import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time

class AutoClickerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.languages = {
            "English": {
                "title": "Auto Clicker",
                "interval_label": "Interval between clicks (μs)",
                "duration_label": "Duration (s)",
                "left_click": "Left button",
                "right_click": "Right button",
                "order_label": "Click order",
                "order_lr": "Left then Right",
                "order_rl": "Right then Left",
                "order_both": "Both at the same time",
                "start_button": "Start",
                "stop_button": "Stop"
            },
            "Čeština": {
                "title": "Auto Kliker",
                "interval_label": "Interval mezi kliknutími (μs)",
                "duration_label": "Doba trvání (s)",
                "left_click": "Levé tlačítko",
                "right_click": "Pravé tlačítko",
                "order_label": "Pořadí kliknutí",
                "order_lr": "Nejprve levé, pak pravé",
                "order_rl": "Nejprve pravé, pak levé",
                "order_both": "Obě najednou",
                "start_button": "Start",
                "stop_button": "Stop"
            },
            "Español": {
                "title": "Auto Clicker",
                "interval_label": "Intervalo entre clics (μs)",
                "duration_label": "Duración (s)",
                "left_click": "Botón izquierdo",
                "right_click": "Botón derecho",
                "order_label": "Orden de clic",
                "order_lr": "Primero izquierdo, luego derecho",
                "order_rl": "Primero derecho, luego izquierdo",
                "order_both": "Ambos al mismo tiempo",
                "start_button": "Iniciar",
                "stop_button": "Detener"
            },
            "Hrvatski": {
                "title": "Auto Kliker",
                "interval_label": "Interval između klikova (μs)",
                "duration_label": "Trajanje (s)",
                "left_click": "Lijeva tipka",
                "right_click": "Desna tipka",
                "order_label": "Redoslijed klikova",
                "order_lr": "Prvo lijeva, zatim desna",
                "order_rl": "Prvo desna, zatim lijeva",
                "order_both": "Oboje u isto vrijeme",
                "start_button": "Početak",
                "stop_button": "Zaustavi"
            },
            "Italiano": {
                "title": "Auto Clicker",
                "interval_label": "Intervallo tra i clic (μs)",
                "duration_label": "Durata (s)",
                "left_click": "Pulsante sinistro",
                "right_click": "Pulsante destro",
                "order_label": "Ordine di clic",
                "order_lr": "Prima sinistra, poi destra",
                "order_rl": "Prima destra, poi sinistra",
                "order_both": "Entrambi contemporaneamente",
                "start_button": "Inizia",
                "stop_button": "Ferma"
            },
            "Русский": {
                "title": "Авто Кликер",
                "interval_label": "Интервал между кликами (μs)",
                "duration_label": "Длительность (с)",
                "left_click": "Левая кнопка",
                "right_click": "Правая кнопка",
                "order_label": "Порядок кликов",
                "order_lr": "Сначала левая, потом правая",
                "order_rl": "Сначала правая, потом левая",
                "order_both": "Обе одновременно",
                "start_button": "Начать",
                "stop_button": "Остановить"
            }
        }

        self.selected_language = tk.StringVar(value="English")

        self.create_widgets()
        self.update_texts()

    def create_widgets(self):
        self.language_menu = ttk.Combobox(self, values=list(self.languages.keys()), textvariable=self.selected_language)
        self.language_menu.pack()
        self.language_menu.bind("<<ComboboxSelected>>", self.update_texts)

        self.interval_label = ttk.Label(self)
        self.interval_label.pack()

        self.interval_scale = ttk.Scale(self, from_=1, to=250000, orient="horizontal")
        self.interval_scale.set(250000)  # Výchozí interval je 100000 μs (100 ms)
        self.interval_scale.pack()

        self.duration_label = ttk.Label(self)
        self.duration_label.pack()

        self.duration_entry = ttk.Entry(self)
        self.duration_entry.pack()

        self.left_click_var = tk.BooleanVar()
        self.right_click_var = tk.BooleanVar()

        self.left_click_check = ttk.Checkbutton(self, variable=self.left_click_var, command=self.check_buttons)
        self.left_click_check.pack()

        self.right_click_check = ttk.Checkbutton(self, variable=self.right_click_var, command=self.check_buttons)
        self.right_click_check.pack()

        self.order_label = ttk.Label(self)
        self.order_var = tk.StringVar(value="LR")
        self.order_frame = ttk.Frame(self)

        self.lr_radio = ttk.Radiobutton(self.order_frame, variable=self.order_var, value="LR")
        self.rl_radio = ttk.Radiobutton(self.order_frame, variable=self.order_var, value="RL")
        self.both_radio = ttk.Radiobutton(self.order_frame, variable=self.order_var, value="BOTH")

        self.start_button = ttk.Button(self, command=self.start_auto_clicker)
        self.start_button.pack()

        self.stop_button = ttk.Button(self, command=self.stop_auto_clicker)
        self.stop_button.pack()

        self.auto_clicker_thread = None
        self.stop_event = threading.Event()

        self.bind("<Escape>", self.quit_application)

    def update_texts(self, event=None):
        lang = self.selected_language.get()
        texts = self.languages[lang]

        self.title(texts["title"])
        self.interval_label.config(text=texts["interval_label"])
        self.duration_label.config(text=texts["duration_label"])
        self.left_click_check.config(text=texts["left_click"])
        self.right_click_check.config(text=texts["right_click"])
        self.order_label.config(text=texts["order_label"])
        self.lr_radio.config(text=texts["order_lr"])
        self.rl_radio.config(text=texts["order_rl"])
        self.both_radio.config(text=texts["order_both"])
        self.start_button.config(text=texts["start_button"])
        self.stop_button.config(text=texts["stop_button"])

    def check_buttons(self):
        if self.left_click_var.get() and self.right_click_var.get():
            self.order_label.pack()
            self.order_frame.pack()
            self.lr_radio.pack(side="left")
            self.rl_radio.pack(side="left")
            self.both_radio.pack(side="left")
        else:
            self.order_label.pack_forget()
            self.order_frame.pack_forget()

    def start_auto_clicker(self):
        try:
            interval = float(self.interval_scale.get()) / 1_000_000  # Převod na sekundy
            duration = float(self.duration_entry.get())
            left_click = self.left_click_var.get()
            right_click = self.right_click_var.get()
            order = self.order_var.get()

            self.stop_event.clear()

            # Zpoždění 3 sekundy pro umístění kurzoru myši
            self.after(3000, lambda: self.run_auto_clicker(interval, duration, left_click, right_click, order))
        except ValueError:
            pass

    def run_auto_clicker(self, interval, duration, left_click, right_click, order):
        self.auto_clicker_thread = threading.Thread(target=self.auto_clicker, args=(interval, duration, left_click, right_click, order))
        self.auto_clicker_thread.start()

    def auto_clicker(self, interval, duration, left_click, right_click, order):
        start_time = time.time()

        while time.time() - start_time < duration:
            if self.stop_event.is_set():
                break

            if left_click and right_click:
                if order == "LR":
                    pyautogui.click(button='left')
                    time.sleep(interval)
                    pyautogui.click(button='right')
                elif order == "RL":
                    pyautogui.click(button='right')
                    time.sleep(interval)
                    pyautogui.click(button='left')
                elif order == "BOTH":
                    pyautogui.click(button='left')
                    pyautogui.click(button='right')
            elif left_click:
                pyautogui.click(button='left')
            elif right_click:
                pyautogui.click(button='right')

            time.sleep(interval)

    def stop_auto_clicker(self, event=None):
        if self.auto_clicker_thread and self.auto_clicker_thread.is_alive():
            self.stop_event.set()
            self.auto_clicker_thread.join()

    def quit_application(self, event=None):
        self.stop_auto_clicker()
        self.destroy()

if __name__ == "__main__":
    app = AutoClickerApp()
    app.mainloop()
