from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QListWidget
)


class AdminWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admin Dashboard")

        self.setGeometry(300, 150, 800, 600)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        title = QLabel("Manage Users")

        users_list = QListWidget()

        users_list.addItem("student1")

        users_list.addItem("student2")

        users_list.addItem("teacher1")

        delete_button = QPushButton(
            "Delete User"
        )

        layout.addWidget(title)

        layout.addWidget(users_list)

        layout.addWidget(delete_button)

        self.setLayout(layout)