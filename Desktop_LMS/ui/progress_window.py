from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from database import get_xp


class ProgressWindow(QWidget):

    def __init__(self, username=None):
        super().__init__()

        self.username = username

        self.setWindowTitle("Progress")
        self.setGeometry(350, 150, 1000, 650)

        # =====================================================
        # GET XP
        # =====================================================

        xp = get_xp(self.username)

        # =====================================================
        # LEVEL SYSTEM
        # =====================================================

        if xp >= 200:
            level = "Advanced"

        elif xp >= 100:
            level = "Intermediate"

        else:
            level = "Beginner"

        # =====================================================
        # LEARNING RANK
        # =====================================================

        if xp >= 300:
            rank = "Skill Master"

        elif xp >= 150:
            rank = "Rising Learner"

        else:
            rank = "New Student"

        # =====================================================
        # STYLE
        # =====================================================

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

        # =====================================================
        # MAIN LAYOUT
        # =====================================================

        main_layout = QVBoxLayout()

        # TITLE
        title = QLabel("📈 Learning Progress")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 28, QFont.Bold))

        title.setStyleSheet("""
            color: #22c55e;
            margin-bottom: 20px;
        """)

        main_layout.addWidget(title)

        # =====================================================
        # CARD
        # =====================================================

        card = QFrame()

        card_layout = QVBoxLayout()

        progress = QLabel(
            f"""
Student Name: {self.username}

XP Earned: {xp}

Current Level: {level}

Learning Rank: {rank}

Status: Active Learner

Skillforge Progress System Active
            """
        )

        progress.setStyleSheet("""
            font-size: 20px;
            line-height: 40px;
            padding: 20px;
        """)

        card_layout.addWidget(progress)

        card.setLayout(card_layout)

        main_layout.addWidget(card)

        self.setLayout(main_layout)