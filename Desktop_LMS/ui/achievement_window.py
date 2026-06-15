from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from database import get_xp


class AchievementWindow(QWidget):

    def __init__(self, username):
        super().__init__()

        self.username = username

        self.setWindowTitle("Achievements")
        self.setGeometry(400, 120, 900, 650)

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
                border: 2px solid #22c55e;
                border-radius: 20px;
                padding: 20px;
            }

        """)

        # =====================================================
        # MAIN LAYOUT
        # =====================================================

        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)

        # =====================================================
        # TITLE
        # =====================================================

        title = QLabel("🏅 Achievements")
        title.setAlignment(Qt.AlignCenter)

        title.setFont(QFont("Segoe UI", 28, QFont.Bold))

        title.setStyleSheet("""
            color: #22c55e;
            margin-bottom: 20px;
        """)

        main_layout.addWidget(title)

        # =====================================================
        # GET XP
        # =====================================================

        xp = get_xp(self.username)

        # =====================================================
        # ACHIEVEMENTS
        # =====================================================

        achievements = []

        if xp >= 0:
            achievements.append(
                ("🥉 Beginner Learner",
                 "Started learning in Skillforge.")
            )

        if xp >= 50:
            achievements.append(
                ("🥈 Quiz Explorer",
                 "Earned 50 XP.")
            )

        if xp >= 100:
            achievements.append(
                ("🥇 Quiz Master",
                 "Reached 100 XP.")
            )

        if xp >= 200:
            achievements.append(
                ("🔥 Dedicated Student",
                 "Reached 200 XP.")
            )

        if xp >= 500:
            achievements.append(
                ("👑 XP Champion",
                 "Reached 500 XP.")
            )

        # =====================================================
        # CREATE ACHIEVEMENT CARDS
        # =====================================================

        for badge, description in achievements:

            card = QFrame()

            card_layout = QVBoxLayout()

            badge_label = QLabel(badge)

            badge_label.setStyleSheet("""
                font-size: 22px;
                font-weight: bold;
                color: #22c55e;
            """)

            description_label = QLabel(description)

            description_label.setStyleSheet("""
                font-size: 16px;
                color: white;
                margin-top: 10px;
            """)

            description_label.setWordWrap(True)

            card_layout.addWidget(badge_label)
            card_layout.addWidget(description_label)

            card.setLayout(card_layout)

            main_layout.addWidget(card)

        self.setLayout(main_layout)