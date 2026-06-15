import requests

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QFrame
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from config import OPENROUTER_API_KEY


class AITutorWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Skillforge AI Tutor")
        self.setGeometry(400, 100, 1000, 750)

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
                border: 2px solid #22c55e;
                border-radius: 15px;
                padding: 15px;
                color: white;
                font-size: 15px;
            }

            QPushButton {
                background-color: #22c55e;
                border-radius: 15px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
                color: black;
            }

            QPushButton:hover {
                background-color: #4ade80;
            }

        """)

        # =====================================================
        # MAIN LAYOUT
        # =====================================================

        main_layout = QVBoxLayout()

        title = QLabel("🤖 Skillforge AI Tutor")
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
        card_layout.setSpacing(20)

        self.question_input = QTextEdit()

        self.question_input.setPlaceholderText(
            "Ask anything..."
        )

        self.question_input.setFixedHeight(140)

        ask_btn = QPushButton("Ask AI Tutor")
        ask_btn.clicked.connect(self.ask_ai)

        self.response_box = QTextEdit()
        self.response_box.setReadOnly(True)

        card_layout.addWidget(self.question_input)
        card_layout.addWidget(ask_btn)
        card_layout.addWidget(self.response_box)

        card.setLayout(card_layout)

        main_layout.addWidget(card)

        self.setLayout(main_layout)

    # =====================================================
    # ASK AI
    # =====================================================

    def ask_ai(self):

        question = self.question_input.toPlainText()

        if not question.strip():
            return

        self.response_box.setText("Thinking...")

        try:

            response = requests.post(

                url="https://openrouter.ai/api/v1/chat/completions",

                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                },

                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                }
            )

            data = response.json()

            answer = data["choices"][0]["message"]["content"]

            self.response_box.setText(answer)

        except Exception as e:

            self.response_box.setText(
                f"Error:\\n\\n{str(e)}"
            )