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


class QuizWindow(QWidget):

    def __init__(self, username=None):
        super().__init__()

        self.username = username

        self.setWindowTitle("Skillforge Quiz")
        self.setGeometry(300, 120, 1100, 650)

        # =====================================================
        # QUESTIONS
        # =====================================================

        self.questions = [

            {
                "question": "What does RAM stand for?",
                "choices": [
                    "Random Access Memory",
                    "Read Access Memory",
                    "Rapid Access Monitor",
                    "Run Access Memory"
                ],
                "answer": "Random Access Memory"
            },

            {
                "question": "Which device is used for input?",
                "choices": [
                    "Monitor",
                    "Printer",
                    "Keyboard",
                    "Speaker"
                ],
                "answer": "Keyboard"
            },

            {
                "question": "Which language is mainly used for Python development?",
                "choices": [
                    "Python",
                    "HTML",
                    "CSS",
                    "SQL"
                ],
                "answer": "Python"
            },

            {
                "question": "Which part stores files permanently?",
                "choices": [
                    "RAM",
                    "CPU",
                    "Hard Drive",
                    "Keyboard"
                ],
                "answer": "Hard Drive"
            },

            {
                "question": "What does URL stand for?",
                "choices": [
                    "Uniform Resource Locator",
                    "Universal Read Link",
                    "Uniform Read Location",
                    "User Resource Link"
                ],
                "answer": "Uniform Resource Locator"
            },

            {
                "question": "Which company created Windows?",
                "choices": [
                    "Apple",
                    "Google",
                    "Microsoft",
                    "Linux"
                ],
                "answer": "Microsoft"
            },

            {
                "question": "Which HTML tag creates a paragraph?",
                "choices": [
                    "<h1>",
                    "<p>",
                    "<div>",
                    "<br>"
                ],
                "answer": "<p>"
            },

            {
                "question": "Which symbol is used for comments in Python?",
                "choices": [
                    "//",
                    "#",
                    "/*",
                    "--"
                ],
                "answer": "#"
            },

            {
                "question": "Which is an operating system?",
                "choices": [
                    "Windows",
                    "Python",
                    "CPU",
                    "RAM"
                ],
                "answer": "Windows"
            },

            {
                "question": "What is used to style web pages?",
                "choices": [
                    "Python",
                    "CSS",
                    "SQL",
                    "C++"
                ],
                "answer": "CSS"
            },

            {
                "question": "Which device shows visual output?",
                "choices": [
                    "Keyboard",
                    "Mouse",
                    "Monitor",
                    "Microphone"
                ],
                "answer": "Monitor"
            },

            {
                "question": "Which storage is temporary?",
                "choices": [
                    "SSD",
                    "Hard Drive",
                    "RAM",
                    "USB"
                ],
                "answer": "RAM"
            },

            {
                "question": "Which language structures webpages?",
                "choices": [
                    "CSS",
                    "Python",
                    "HTML",
                    "Java"
                ],
                "answer": "HTML"
            },

            {
                "question": "Which company makes iPhones?",
                "choices": [
                    "Samsung",
                    "Apple",
                    "Google",
                    "Microsoft"
                ],
                "answer": "Apple"
            },

            {
                "question": "What does GPU stand for?",
                "choices": [
                    "Graphics Processing Unit",
                    "General Processing Unit",
                    "Graphical Program Utility",
                    "Graphics Program User"
                ],
                "answer": "Graphics Processing Unit"
            }

        ]

        self.current_question = 0
        self.score = 0

        # =====================================================
        # MAIN STYLE
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
                padding: 15px;
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

        # =====================================================
        # TITLE
        # =====================================================

        title = QLabel("📝 Quiz Challenge")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 30, QFont.Bold))

        title.setStyleSheet("""
            color: #22c55e;
            margin-bottom: 20px;
        """)

        main_layout.addWidget(title)

        # =====================================================
        # QUIZ CARD
        # =====================================================

        self.card = QFrame()

        card_layout = QVBoxLayout()
        card_layout.setSpacing(20)

        # QUESTION COUNT
        self.question_number = QLabel()
        self.question_number.setStyleSheet("""
            color: #94a3b8;
            font-size: 15px;
        """)

        # QUESTION
        self.question_label = QLabel()
        self.question_label.setWordWrap(True)

        self.question_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        """)

        # CHOICE BUTTONS
        self.choice1 = QPushButton()
        self.choice2 = QPushButton()
        self.choice3 = QPushButton()
        self.choice4 = QPushButton()

        self.choice1.clicked.connect(lambda: self.check_answer(self.choice1.text()))
        self.choice2.clicked.connect(lambda: self.check_answer(self.choice2.text()))
        self.choice3.clicked.connect(lambda: self.check_answer(self.choice3.text()))
        self.choice4.clicked.connect(lambda: self.check_answer(self.choice4.text()))

        # ADD TO CARD
        card_layout.addWidget(self.question_number)
        card_layout.addWidget(self.question_label)
        card_layout.addWidget(self.choice1)
        card_layout.addWidget(self.choice2)
        card_layout.addWidget(self.choice3)
        card_layout.addWidget(self.choice4)

        self.card.setLayout(card_layout)

        main_layout.addWidget(self.card)

        self.setLayout(main_layout)

        # LOAD FIRST QUESTION
        self.load_question()

    # =====================================================
    # LOAD QUESTION
    # =====================================================

    def load_question(self):

        if self.current_question < len(self.questions):

            question_data = self.questions[self.current_question]

            self.question_number.setText(
                f"Question {self.current_question + 1} of {len(self.questions)}"
            )

            self.question_label.setText(question_data["question"])

            self.choice1.setText(question_data["choices"][0])
            self.choice2.setText(question_data["choices"][1])
            self.choice3.setText(question_data["choices"][2])
            self.choice4.setText(question_data["choices"][3])

        else:
            self.pythonshow_result()

    # =====================================================
    # CHECK ANSWER
    # =====================================================

    def check_answer(self, selected_answer):

        correct_answer = self.questions[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        self.load_question()

    # =====================================================
    # SHOW RESULT
    # =====================================================

    def show_result(self):

        QMessageBox.information(
            self,
            "Quiz Finished",
            f"You scored {self.score} out of {len(self.questions)}"
        )

        self.close()