from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFrame,
    QMessageBox
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# ✅ IMPORT GLOBAL THEME SYSTEM
from styles import toggle_theme, apply_theme_to_app, get_theme


class SettingsWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Settings")
        self.setGeometry(450, 120, 850, 650)

        # ✅ APPLY GLOBAL THEME
        apply_theme_to_app()

        main_layout = QVBoxLayout()

        title = QLabel("⚙ Skillforge Settings")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 28, QFont.Bold))
        title.setStyleSheet("color: #22c55e; margin-bottom: 20px;")

        main_layout.addWidget(title)

        card = QFrame()
        card_layout = QVBoxLayout()
        card_layout.setSpacing(20)

        # THEME TOGGLE BUTTON
        theme_btn = QPushButton("🌙 Toggle Theme")
        theme_btn.clicked.connect(self.change_theme)

        about = QLabel(
            "Skillforge Desktop LMS\n\n"
            "Version: 1.0\n"
            "Developed with Python + PyQt5\n\n"
            "A modern desktop learning system."
        )

        about.setStyleSheet("""
            font-size: 17px;
            line-height: 28px;
        """)

        card_layout.addWidget(theme_btn)
        card_layout.addWidget(about)

        card.setLayout(card_layout)
        main_layout.addWidget(card)

        self.setLayout(main_layout)

    # =====================================================
    # GLOBAL THEME TOGGLE
    # =====================================================
    def change_theme(self):
        new_style = toggle_theme()

        # 🔥 APPLY TO ENTIRE APP (IMPORTANT PART)
        apply_theme_to_app()

        if "0b1220" in new_style:
            mode = "Dark Mode Enabled 🌙"
        else:
            mode = "Light Mode Enabled ☀️"

        QMessageBox.information(
            self,
            "Theme Changed",
            mode
        )