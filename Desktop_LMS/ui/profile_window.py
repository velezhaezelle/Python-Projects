from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ProfileWindow(QWidget):

    def __init__(self, username=None):
        super().__init__()

        self.username = username

        self.setWindowTitle("Profile")
        self.setGeometry(350, 150, 1000, 600)

        self.setStyleSheet("""
            QWidget {
                background-color: #050816;
                color: white;
                font-family: Segoe UI;
            }

            QFrame {
                background-color: #0f172a;
                border: 2px solid #13213d;
                border-radius: 25px;
                padding: 30px;
            }
        """)

        main_layout = QVBoxLayout()

        title = QLabel("👤 Student Profile")
        title.setFont(QFont("Segoe UI", 28, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #22c55e;")

        card = QFrame()

        card_layout = QVBoxLayout()

        profile = QLabel(
            f"Username: {self.username}\n\n"
            "Role: Student\n\n"
            "Level: Beginner\n\n"
            "School Status: Active\n\n"
            "Skillforge Member"
        )

        profile.setStyleSheet("""
            font-size: 18px;
            line-height: 35px;
        """)

        card_layout.addWidget(profile)

        card.setLayout(card_layout)

        main_layout.addWidget(title)
        main_layout.addWidget(card)

        self.setLayout(main_layout)