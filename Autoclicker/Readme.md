# 🖱️ Auto Clicker

Auto Clicker is an application that automatically clicks at a specified mouse position. The application allows you to set various parameters such as the interval between clicks, mouse buttons, click order, and click location. The application supports multiple languages.

## 📋 Features

- Set the interval between clicks in microseconds (1 μs to 1,000,000 μs).
- Choose mouse buttons (left, right, or both).
- Select the order of clicks (left then right, right then left, both at the same time).
- Choose the click location (current mouse position, mouse position when the application starts).
- Multi-language support: English, Czech, Spanish, Croatian, Italian, Russian.

## 🛠️ Installation

### Requirements

- Python 3.x
- Libraries: `tkinter`, `pyautogui`, `threading`

### Installing Libraries

pip install pyautogui

`tkinter` and `threading` are part of Python's standard library and do not need to be installed separately.

## 🚀 Usage

1. Download or clone this repository.
2. Run the `autoclicker.py` script in visual studio code or other python ide:
    ```
    Autoclicker.py
    ```
3. Set the desired parameters in the application's graphical interface.
4. Click `Start` to begin the auto clicker. You will have 3 seconds to position your mouse cursor where you want the clicking to occur.
5. You can stop the clicking by pressing the `Stop` button or the `ESC` key. but its not working perfect

## 📄 Code

The main part of the code is located in the `autoclicker.py` file. It includes the creation of the user interface using the `tkinter` library and the implementation of the auto-clicking functionality using the `pyautogui` library.
 Includes imports, definition of the AutoClickerApp class, and implementation of functions
## 🌐 Language Support
The application supports the following languages:

English
Czech (Čeština)
Spanish (Español)
Croatian (Hrvatski)
Italian (Italiano)
Russian (Русский)
The default language when the application starts is English.
