import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except:
        if language_choice.get() == "English":
            result.set("Error")
        elif language_choice.get() == "Czech":
            result.set("Chyba")
        elif language_choice.get() == "Polish":
            result.set("Błąd")
        elif language_choice.get() == "Slovak":
            result.set("Chyba")

def clear_entry():
    entry.delete(0, tk.END)

def delete_last_char():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

def change_language(language):
    if language == "English":
        window.title("Calculator")
        messagebox.showinfo("Language Changed", "Language changed to English")
    elif language == "Czech":
        window.title("Kalkulačka")
        messagebox.showinfo("Změna jazyka", "Jazyk byl změněn na češtinu")
    elif language == "Polish":
        window.title("Kalkulator")
        messagebox.showinfo("Zmiana języka", "Zmieniono język na polski")
    elif language == "Slovak":
        window.title("Kalkulačka")
        messagebox.showinfo("Zmena jazyka", "Jazyk zmenený na slovenčinu")

# Vytvoření okna
window = tk.Tk()
window.title("Calculator")

# Výběr jazyka při spuštění
language_choice = tk.StringVar()
language_choice.set("English")

language_label = tk.Label(window, text="Choose Language:")
language_label.grid(row=0, column=0, columnspan=2)

language_menu = tk.OptionMenu(window, language_choice, "English", "Czech", "Polish", "Slovak", command=change_language)
language_menu.grid(row=0, column=2, columnspan=2)

# Vytvoření vstupního pole
entry = tk.Entry(window, width=30, font=("Arial", 14))
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Vytvoření tlačítek pro čísla a operace
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 2
col = 0
for button in buttons:
    tk.Button(window, text=button, width=5, font=("Arial", 14), command=lambda b=button: entry.insert(tk.END, b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Vytvoření tlačítka pro výpočet
tk.Button(window, text="=", width=5, font=("Arial", 14), command=evaluate_expression).grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Vytvoření tlačítka pro vynulování
tk.Button(window, text="C", width=5, font=("Arial", 14), command=clear_entry).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Vytvoření tlačítka pro vymazání posledního znaku
tk.Button(window, text="C1", width=5, font=("Arial", 14), command=delete_last_char).grid(row=7, column=2, columnspan=2, padx=10, pady=10)

# Vytvoření proměnné pro výsledek
result = tk.StringVar()
result.set("")

# Vytvoření pole pro zobrazení výsledku
result_label = tk.Label(window, textvariable=result, font=("Arial", 14))
result_label.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

window.mainloop()
