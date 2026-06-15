from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame
)

from styles import MAIN_STYLE


class AnalyticsWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Analytics Dashboard")

        self.setGeometry(350, 150, 900, 600)

        self.setStyleSheet(MAIN_STYLE)

        self.setup_ui()

    def setup_ui(self):

        main_layout = QVBoxLayout()

        title = QLabel("Student Analytics")

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
                padding: 30px;
            }

        """)

        layout = QVBoxLayout()

        students = QLabel(
            "Total Students: 120"
        )

        courses = QLabel(
            "Total Courses: 10"
        )

        completed = QLabel(
            "Completed Lessons: 350"
        )

        xp = QLabel(
            "Total XP Earned: 5000"
        )

        students.setStyleSheet("font-size: 20px;")

        courses.setStyleSheet("font-size: 20px;")

        completed.setStyleSheet("font-size: 20px;")

        xp.setStyleSheet("font-size: 20px;")

        layout.addWidget(students)

        layout.addWidget(courses)

        layout.addWidget(completed)

        layout.addWidget(xp)

        card.setLayout(layout)

        main_layout.addWidget(title)

        main_layout.addWidget(card)

        self.setLayout(main_layout)