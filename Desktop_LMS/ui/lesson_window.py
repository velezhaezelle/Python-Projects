import os
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QTextEdit,
    QFrame
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QPushButton


class LessonWindow(QWidget):

    def __init__(self, lesson_title, lesson_content, pdf_file=None):
        super().__init__()

        self.setWindowTitle(lesson_title)
        self.setGeometry(300, 120, 1100, 700)

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

            QTextEdit {
                background-color: #111827;
                border: 2px solid #1e293b;
                border-radius: 15px;
                padding: 20px;
                font-size: 17px;
                color: white;
            }
        """)

        # =====================================================
        # MAIN LAYOUT
        # =====================================================

        main_layout = QVBoxLayout()

        # TITLE
        title = QLabel(lesson_title)
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 28, QFont.Bold))

        title.setStyleSheet("""
            color: #22c55e;
            margin-bottom: 20px;
        """)

        # LESSON CARD
        card = QFrame()

        card_layout = QVBoxLayout()

        # LESSON CONTENT
        lesson_text = QTextEdit()
        lesson_text.setReadOnly(True)
        lesson_text.setText(lesson_content)

        # =====================================================
        # PDF BUTTON
        # =====================================================

        if pdf_file:
            pdf_button = QPushButton("📄 Open PDF Module")

            pdf_button.setStyleSheet("""
                QPushButton {
                    background-color: #22c55e;
                    border-radius: 12px;
                    padding: 15px;
                    font-size: 16px;
                    font-weight: bold;
                    color: black;
                }

                QPushButton:hover {
                    background-color: #4ade80;
                }
            """)

            pdf_button.clicked.connect(
                lambda: os.startfile(pdf_file)
            )

            card_layout.addWidget(pdf_button)

        card_layout.addWidget(lesson_text)

        card.setLayout(card_layout)

        main_layout.addWidget(title)
        main_layout.addWidget(card)

        self.setLayout(main_layout)