from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from database import login_user
from ui.dashboard_window import DashboardWindow
from ui.register_window import RegisterWindow


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Skillforge LMS")
        self.setGeometry(200, 100, 1200, 700)

        # ===== MAIN WINDOW STYLE =====
        self.setStyleSheet("""
            QWidget {
                background-color: #050816;
                color: white;
                font-family: Segoe UI;
            }
        """)

        # ===== MAIN LAYOUT =====
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        # =====================================================
        # LEFT SIDE PANEL
        # =====================================================

        left_panel = QFrame()
        left_panel.setStyleSheet("""
            background-color: #081020;
            border-right: 2px solid #13213d;
        """)

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignCenter)

        # MAIN TITLE
        logo = QLabel("Skillforge")
        logo.setAlignment(Qt.AlignCenter)
        logo.setFont(QFont("Segoe UI", 38, QFont.Bold))
        logo.setStyleSheet("""
            color: #22c55e;
            margin-bottom: 10px;
        """)

        # QUOTE
        quote = QLabel('"Knowledge is power, continue learning"')
        quote.setAlignment(Qt.AlignCenter)
        quote.setStyleSheet("""
            color: #94a3b8;
            font-size: 15px;
            font-style: italic;
            margin-bottom: 40px;
        """)

        # STUDENT EMOJI / ICON
        student_icon = QLabel("🎓")
        student_icon.setAlignment(Qt.AlignCenter)
        student_icon.setStyleSheet("""
            font-size: 120px;
            margin-bottom: 20px;
        """)

        # MOTIVATION TEXT
        motivation = QLabel(
            "Learn Every Day\n"
            "Grow Your Skills\n"
            "Achieve Your Goals"
        )

        motivation.setAlignment(Qt.AlignCenter)
        motivation.setStyleSheet("""
            font-size: 22px;
            color: white;
            line-height: 35px;
        """)

        left_layout.addWidget(logo)
        left_layout.addWidget(quote)
        left_layout.addWidget(student_icon)
        left_layout.addWidget(motivation)

        left_panel.setLayout(left_layout)

        # =====================================================
        # RIGHT SIDE LOGIN PANEL
        # =====================================================

        right_panel = QFrame()
        right_panel.setStyleSheet("""
            background-color: #0f172a;
        """)

        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignCenter)

        # LOGIN CARD
        login_card = QFrame()
        login_card.setFixedWidth(420)

        login_card.setStyleSheet("""
            QFrame {
                background-color: #111827;
                border: 2px solid #22c55e;
                border-radius: 25px;
                padding: 30px;
            }
        """)

        card_layout = QVBoxLayout()
        card_layout.setSpacing(20)

        # LOGIN TITLE
        login_title = QLabel("Login")
        login_title.setAlignment(Qt.AlignCenter)

        login_title.setStyleSheet("""
            font-size: 34px;
            font-weight: bold;
            color: white;
            margin-bottom: 20px;
        """)

        # USERNAME INPUT
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")

        self.username_input.setStyleSheet("""
            QLineEdit {
                background-color: #1e293b;
                border: 2px solid #334155;
                border-radius: 12px;
                padding: 15px;
                font-size: 16px;
                color: white;
            }

            QLineEdit:focus {
                border: 2px solid #22c55e;
            }
        """)

        # PASSWORD INPUT
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.password_input.setStyleSheet("""
            QLineEdit {
                background-color: #1e293b;
                border: 2px solid #334155;
                border-radius: 12px;
                padding: 15px;
                font-size: 16px;
                color: white;
            }

            QLineEdit:focus {
                border: 2px solid #22c55e;
            }
        """)

        # LOGIN BUTTON
        self.login_btn = QPushButton("LOGIN")

        self.login_btn.setCursor(Qt.PointingHandCursor)

        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: black;
                border-radius: 12px;
                padding: 15px;
                font-size: 18px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #4ade80;
            }
        """)

        self.login_btn.clicked.connect(self.login)

        # REGISTER BUTTON
        self.register_btn = QPushButton("Create New Account")

        self.register_btn.setCursor(Qt.PointingHandCursor)

        self.register_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #22c55e;
                border: none;
                font-size: 15px;
                margin-top: 10px;
            }

            QPushButton:hover {
                color: #4ade80;
            }
        """)

        self.register_btn.clicked.connect(self.open_register)

        # ADD TO CARD
        card_layout.addWidget(login_title)
        card_layout.addWidget(self.username_input)
        card_layout.addWidget(self.password_input)
        card_layout.addWidget(self.login_btn)
        card_layout.addWidget(self.register_btn)

        login_card.setLayout(card_layout)

        right_layout.addWidget(login_card)

        right_panel.setLayout(right_layout)

        # =====================================================
        # ADD PANELS TO MAIN LAYOUT
        # =====================================================

        main_layout.addWidget(left_panel, 1)
        main_layout.addWidget(right_panel, 1)

        self.setLayout(main_layout)

    # =====================================================
    # LOGIN FUNCTION
    # =====================================================

    def login(self):

        username = self.username_input.text()
        password = self.password_input.text()

        user = login_user(username, password)

        if user:
            self.dashboard = DashboardWindow(user[0])
            self.dashboard.show()
            self.close()

        else:
            QMessageBox.warning(
                self,
                "Login Failed",
                "Invalid username or password."
            )

    # =====================================================
    # OPEN REGISTER
    # =====================================================

    def open_register(self):

        self.register_window = RegisterWindow()
        self.register_window.show()