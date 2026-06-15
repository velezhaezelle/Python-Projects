from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QFrame
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from ui.lesson_window import LessonWindow


class CoursesWindow(QWidget):

    def __init__(self, username=None):
        super().__init__()

        self.username = username

        self.setWindowTitle("Courses")
        self.setGeometry(350, 150, 1000, 650)

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
                font-size: 17px;
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

        # TITLE
        title = QLabel("📚 Learning Courses")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 28, QFont.Bold))

        title.setStyleSheet("""
            color: #22c55e;
            margin-bottom: 20px;
        """)

        main_layout.addWidget(title)

        # COURSE CARD
        card = QFrame()

        card_layout = QVBoxLayout()
        card_layout.setSpacing(20)

        # =====================================================
        # LESSON BUTTONS
        # =====================================================

        lesson1 = QPushButton("📘 Python Basics")
        lesson2 = QPushButton("🌐 HTML & CSS")
        lesson3 = QPushButton("💻 Computer Fundamentals")

        lesson1.clicked.connect(self.open_python)
        lesson2.clicked.connect(self.open_html)
        lesson3.clicked.connect(self.open_computer)

        card_layout.addWidget(lesson1)
        card_layout.addWidget(lesson2)
        card_layout.addWidget(lesson3)

        card.setLayout(card_layout)

        main_layout.addWidget(card)

        self.setLayout(main_layout)

    # =====================================================
    # LESSONS
    # =====================================================

    def open_python(self):

        content = (
            "PYTHON BASICS\n\n"
            "Python is a powerful programming language.\n\n"
            "It is beginner-friendly and widely used in:\n"
            "- Web development\n"
            "- Artificial Intelligence\n"
            "- Data Science\n"
            "- Automation\n\n"
            "Python uses simple syntax that is easy to read."
        )

        self.lesson = LessonWindow(
            "📘 Python Basics",
            content,
            "assets/pdfs/python_module.pdf"
        )

        self.lesson.show()

    # =====================================================

    def open_html(self):

        content = (
            "HTML & CSS\n\n"
            "HTML creates the structure of webpages.\n\n"
            "CSS designs the webpage appearance.\n\n"
            "Together they build modern websites."
        )

        self.lesson = LessonWindow(
            "🌐 HTML & CSS",
            content,
            "assets/pdfs/html_notes.pdf"
        )

        self.lesson.show()

    # =====================================================

    def open_computer(self):

        content = (
            "COMPUTER FUNDAMENTALS\n\n"
            "A computer consists of:\n"
            "- CPU\n"
            "- RAM\n"
            "- Storage\n"
            "- Input Devices\n"
            "- Output Devices\n\n"
            "These components work together to process data."
        )

        self.lesson = LessonWindow(
            "💻 Computer Fundamentals",
            content
        )

        self.lesson.show()