from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QFrame
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from database import register_user


class RegisterWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Skillforge Register")
        self.setGeometry(450, 120, 500, 650)

        # =====================================================
        # MAIN STYLE
        # =====================================================

        self.setStyleSheet("""
            QWidget {
                background-color: #050816;
                font-family: Segoe UI;
                color: white;
            }

            QFrame {
                background-color: #0f172a;
                border: 2px solid #13213d;
                border-radius: 25px;
            }

            QLabel {
                color: white;
            }

            QLineEdit {
                background-color: #111827;
                border: 2px solid #1e293b;
                border-radius: 12px;
                padding: 15px;
                color: white;
                font-size: 15px;
            }

            QLineEdit:focus {
                border: 2px solid #22c55e;
            }

            QPushButton {
                background-color: #22c55e;
                border: none;
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
        main_layout.setContentsMargins(40, 40, 40, 40)

        # =====================================================
        # REGISTER CARD
        # =====================================================

        card = QFrame()

        card_layout = QVBoxLayout()
        card_layout.setSpacing(20)

        # =====================================================
        # TITLE
        # =====================================================

        title = QLabel("Skillforge")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 30, QFont.Bold))

        title.setStyleSheet("""
            color: #22c55e;
            margin-top: 20px;
        """)

        subtitle = QLabel("Create Your Learning Account")
        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""
            color: #94a3b8;
            font-size: 15px;
            margin-bottom: 20px;
        """)

        # =====================================================
        # INPUTS
        # =====================================================

        username_label = QLabel("Username")
        username_label.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
        """)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")

        password_label = QLabel("Password")
        password_label.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
        """)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)

        # =====================================================
        # BUTTON
        # =====================================================

        register_btn = QPushButton("Create Account")
        register_btn.clicked.connect(self.register)

        # =====================================================
        # ADD WIDGETS
        # =====================================================

        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)

        card_layout.addWidget(username_label)
        card_layout.addWidget(self.username_input)

        card_layout.addWidget(password_label)
        card_layout.addWidget(self.password_input)

        card_layout.addSpacing(10)
        card_layout.addWidget(register_btn)

        card_layout.addStretch()

        card.setLayout(card_layout)

        main_layout.addWidget(card)

        self.setLayout(main_layout)

    # =====================================================
    # REGISTER USER
    # =====================================================

    def register(self):

        username = self.username_input.text()
        password = self.password_input.text()

        if username == "" or password == "":

            QMessageBox.warning(
                self,
                "Error",
                "Please fill in all fields."
            )

            return

        success = register_user(username, password)

        if success:

            QMessageBox.information(
                self,
                "Success",
                "Account created successfully!"
            )

            self.close()

        else:

            QMessageBox.warning(
                self,
                "Error",
                "Username already exists."
            )