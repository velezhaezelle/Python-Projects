# styles.py

from PyQt5.QtWidgets import QApplication

DARK_STYLE = """
QWidget {
    background-color: #0b1220;
    color: #e5e7eb;
    font-family: Arial;
    font-size: 14px;
}

QLabel {
    color: #e5e7eb;
}

QLineEdit {
    background-color: #111827;
    border: 1px solid #1f2937;
    padding: 10px;
    border-radius: 8px;
    color: white;
}

QPushButton {
    background-color: #2563eb;
    color: white;
    padding: 10px;
    border-radius: 8px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #1d4ed8;
}

QPushButton:pressed {
    background-color: #1e40af;
}

QFrame {
    background-color: #111827;
    border-radius: 12px;
    border: 1px solid #1f2937;
}
"""

LIGHT_STYLE = """
QWidget {
    background-color: #f8fafc;
    color: #0f172a;
    font-family: Arial;
    font-size: 14px;
}

QLabel {
    color: #0f172a;
}

QLineEdit {
    background-color: white;
    border: 1px solid #cbd5e1;
    padding: 10px;
    border-radius: 8px;
    color: black;
}

QPushButton {
    background-color: #3b82f6;
    color: white;
    padding: 10px;
    border-radius: 8px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #2563eb;
}

QPushButton:pressed {
    background-color: #1d4ed8;
}

QFrame {
    background-color: white;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
}
"""

CURRENT_THEME = "dark"


def get_theme():
    return DARK_STYLE if CURRENT_THEME == "dark" else LIGHT_STYLE


def toggle_theme():
    global CURRENT_THEME
    CURRENT_THEME = "light" if CURRENT_THEME == "dark" else "dark"
    return get_theme()


def apply_theme_to_app():
    """🔥 THIS APPLIES THE THEME TO THE ENTIRE APP"""
    app = QApplication.instance()
    if app:
        app.setStyleSheet(get_theme())