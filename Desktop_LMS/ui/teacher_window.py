from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QTextEdit
)


class TeacherWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Teacher Dashboard")

        self.setGeometry(300, 150, 800, 600)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        title = QLabel("Teacher Dashboard")

        lesson_input = QTextEdit()

        lesson_input.setPlaceholderText(
            "Write lesson content here..."
        )

        add_button = QPushButton(
            "Add Lesson"
        )

        layout.addWidget(title)

        layout.addWidget(lesson_input)

        layout.addWidget(add_button)

        self.setLayout(layout)