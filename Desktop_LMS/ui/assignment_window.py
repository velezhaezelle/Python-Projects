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


class AssignmentWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Assignments")
        self.setGeometry(400, 120, 950, 650)

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
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
                color: white;
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
        title = QLabel("📝 Assignments")
        title.setAlignment(Qt.AlignCenter)

        title.setFont(QFont("Segoe UI", 28, QFont.Bold))

        title.setStyleSheet("""
            color: #22c55e;
            margin-bottom: 20px;
        """)

        main_layout.addWidget(title)

        # =====================================================
        # ASSIGNMENT CARD
        # =====================================================

        card = QFrame()

        card_layout = QVBoxLayout()
        card_layout.setSpacing(20)

        assignment1 = QLabel(
            "📘 Python Assignment\n\n"
            "Create a Python calculator using variables and input.\n\n"
            "Deadline: Friday"
        )

        assignment1.setStyleSheet("""
            font-size: 17px;
            line-height: 28px;
        """)

        submit_btn1 = QPushButton("Submit Assignment")

        submit_btn1.clicked.connect(
            lambda: self.submit_assignment(
                "Python Assignment"
            )
        )

        assignment2 = QLabel(
            "🌐 HTML Assignment\n\n"
            "Create a simple webpage using headings and paragraphs.\n\n"
            "Deadline: Monday"
        )

        assignment2.setStyleSheet("""
            font-size: 17px;
            line-height: 28px;
        """)

        submit_btn2 = QPushButton("Submit Assignment")

        submit_btn2.clicked.connect(
            lambda: self.submit_assignment(
                "HTML Assignment"
            )
        )

        card_layout.addWidget(assignment1)
        card_layout.addWidget(submit_btn1)

        card_layout.addSpacing(20)

        card_layout.addWidget(assignment2)
        card_layout.addWidget(submit_btn2)

        card.setLayout(card_layout)

        main_layout.addWidget(card)

        self.setLayout(main_layout)

    # =====================================================
    # SUBMIT ASSIGNMENT
    # =====================================================

    def submit_assignment(self, assignment_name):

        QMessageBox.information(
            self,
            "Assignment Submitted",
            f"You submitted:\n\n{assignment_name}"
        )