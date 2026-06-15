from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QListWidget,
    QVBoxLayout,
    QFrame
)

from styles import MAIN_STYLE


class LeaderboardWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Leaderboard")

        self.setGeometry(400, 180, 700, 550)

        self.setStyleSheet(MAIN_STYLE)

        self.setup_ui()

    def setup_ui(self):

        main_layout = QVBoxLayout()

        title = QLabel("Top Students")

        title.setStyleSheet("""

            font-size: 30px;
            font-weight: bold;
            padding-bottom: 20px;

        """)

        card = QFrame()

        card.setStyleSheet("""

            QFrame {
                background-color: #111827;
                border-radius: 20px;
                padding: 25px;
            }

        """)

        layout = QVBoxLayout()

        leaderboard = QListWidget()

        leaderboard.addItem(
            "🥇 John — 500 XP"
        )

        leaderboard.addItem(
            "🥈 Maria — 450 XP"
        )

        leaderboard.addItem(
            "🥉 Alex — 400 XP"
        )

        leaderboard.addItem(
            "4. Sophia — 350 XP"
        )

        leaderboard.addItem(
            "5. Daniel — 300 XP"
        )

        layout.addWidget(leaderboard)

        card.setLayout(layout)

        main_layout.addWidget(title)

        main_layout.addWidget(card)

        self.setLayout(main_layout)