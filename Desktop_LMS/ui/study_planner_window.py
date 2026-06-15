from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QFrame,
    QMessageBox
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class StudyPlannerWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Study Planner")
        self.setGeometry(420, 120, 950, 700)

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

        title = QLabel("📅 Study Planner")
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

        instruction = QLabel(
            "Create your daily study plan below."
        )

        instruction.setStyleSheet("""
            font-size: 17px;
            color: white;
        """)

        self.plan_input = QTextEdit()

        self.plan_input.setPlaceholderText(
            "Example:\n"
            "- Study Python loops\n"
            "- Finish HTML assignment\n"
            "- Watch CSS tutorial"
        )

        save_btn = QPushButton("💾 Save Study Plan")
        save_btn.clicked.connect(self.save_plan)

        card_layout.addWidget(instruction)
        card_layout.addWidget(self.plan_input)
        card_layout.addWidget(save_btn)

        card.setLayout(card_layout)

        main_layout.addWidget(card)

        self.setLayout(main_layout)

    # =====================================================
    # SAVE PLAN
    # =====================================================

    def save_plan(self):

        plan = self.plan_input.toPlainText()

        if not plan.strip():

            QMessageBox.warning(
                self,
                "Empty Plan",
                "Please write a study plan first."
            )

            return

        QMessageBox.information(
            self,
            "Saved",
            "Study plan saved successfully!"
        )