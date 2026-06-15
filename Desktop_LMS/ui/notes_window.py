from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QFrame,
    QMessageBox
)

from styles import MAIN_STYLE


class NotesWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notes")

        self.setGeometry(400, 180, 800, 600)

        self.setStyleSheet(MAIN_STYLE)

        self.setup_ui()

    def setup_ui(self):

        main_layout = QVBoxLayout()

        title = QLabel("Your Study Notes")

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

        self.notes_box = QTextEdit()

        self.notes_box.setPlaceholderText(
            "Write your notes here..."
        )

        save_button = QPushButton(
            "Save Notes"
        )

        save_button.setMinimumHeight(50)

        save_button.clicked.connect(
            self.save_notes
        )

        layout.addWidget(self.notes_box)

        layout.addWidget(save_button)

        card.setLayout(layout)

        main_layout.addWidget(title)

        main_layout.addWidget(card)

        self.setLayout(main_layout)

    def save_notes(self):

        QMessageBox.information(
            self,
            "Saved",
            "Notes saved successfully!"
        )