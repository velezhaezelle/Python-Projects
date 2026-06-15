from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit
)

from PyQt5.QtGui import QFont

import io
import contextlib


class CodeLabWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SkillForge Code Lab")
        self.setGeometry(300, 100, 1000, 700)

        self.setStyleSheet("""
            QWidget{
                background-color:#050816;
                color:white;
                font-family:Segoe UI;
            }

            QTextEdit{
                background-color:#111827;
                border:2px solid #22c55e;
                border-radius:15px;
                color:white;
                font-size:15px;
                padding:10px;
            }

            QPushButton{
                background-color:#111827;
                border:2px solid #22c55e;
                border-radius:15px;
                padding:12px;
                font-size:16px;
                font-weight:bold;
            }

            QPushButton:hover{
                border:2px solid #4ade80;
            }
        """)

        layout = QVBoxLayout()

        title = QLabel("💻 Python Code Lab")
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))

        self.editor = QTextEdit()

        self.editor.setPlainText(
            'print("Welcome to SkillForge Code Lab!")'
        )

        self.run_btn = QPushButton("▶ Run Code")

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.run_btn.clicked.connect(self.run_code)

        layout.addWidget(title)
        layout.addWidget(self.editor)
        layout.addWidget(self.run_btn)

        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output)

        self.setLayout(layout)

    def run_code(self):

        code = self.editor.toPlainText()

        buffer = io.StringIO()

        try:

            with contextlib.redirect_stdout(buffer):
                exec(code)

            result = buffer.getvalue()

            self.output.setPlainText(result)

        except Exception as e:

            self.output.setPlainText(
                f"Error:\n{str(e)}"
            )