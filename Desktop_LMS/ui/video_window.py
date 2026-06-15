import webbrowser

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFrame
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class VideoWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Lessons")
        self.setGeometry(400, 120, 900, 600)

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
                padding: 25px;
            }

            QPushButton {
                background-color: #111827;
                border: 2px solid #22c55e;
                border-radius: 15px;
                padding: 18px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                text-align: left;
            }

            QPushButton:hover {
                background-color: #1e293b;
                border: 2px solid #4ade80;
            }
        """)

        # =====================================================
        # MAIN LAYOUT
        # =====================================================

        main_layout = QVBoxLayout()

        title = QLabel("🎥 Video Lessons")
        title.setAlignment(Qt.AlignCenter)

        title.setFont(QFont("Segoe UI", 28, QFont.Bold))

        title.setStyleSheet("""
            color: #22c55e;
            margin-bottom: 20px;
        """)

        main_layout.addWidget(title)

        # =====================================================
        # VIDEO CARD
        # =====================================================

        card = QFrame()

        card_layout = QVBoxLayout()
        card_layout.setSpacing(20)

        # =====================================================
        # VIDEO BUTTONS
        # =====================================================

        python_btn = QPushButton(
            "📘 Python Full Course"
        )

        html_btn = QPushButton(
            "🌐 HTML & CSS Tutorial"
        )

        pyqt_btn = QPushButton(
            "🖥 PyQt5 GUI Tutorial"
        )

        sql_btn = QPushButton(
            "🗄 SQLite Database Tutorial"
        )

        # =====================================================
        # BUTTON CONNECTIONS
        # =====================================================

        python_btn.clicked.connect(
            lambda: self.open_video(
                "https://www.youtube.com/watch?v=_uQrJ0TkZlc"
            )
        )

        html_btn.clicked.connect(
            lambda: self.open_video(
                "https://www.youtube.com/watch?v=G3e-cpL7ofc"
            )
        )

        pyqt_btn.clicked.connect(
            lambda: self.open_video(
                "https://www.youtube.com/watch?v=Vde5SH8e1OQ"
            )
        )

        sql_btn.clicked.connect(
            lambda: self.open_video(
                "https://www.youtube.com/watch?v=byHcYRpMgI4"
            )
        )

        # =====================================================
        # ADD BUTTONS
        # =====================================================

        card_layout.addWidget(python_btn)
        card_layout.addWidget(html_btn)
        card_layout.addWidget(pyqt_btn)
        card_layout.addWidget(sql_btn)

        card.setLayout(card_layout)

        main_layout.addWidget(card)

        self.setLayout(main_layout)

    # =====================================================
    # OPEN VIDEO
    # =====================================================

    def open_video(self, url):

        webbrowser.open(url)