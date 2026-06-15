from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QFrame
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.colors import HexColor

import os
import webbrowser


class CertificateWindow(QWidget):



    def __init__(self, username=None):
        super().__init__()

        # ✅ FIX: ensure username is always a string
        self.username = str(username) if username else "Unknown User"

        self.setWindowTitle("Certificates")
        self.setGeometry(450, 150, 700, 500)

        self.setStyleSheet("""
            QWidget {
                background-color: #050816;
                color: white;
                font-family: Segoe UI;
            }

            QFrame {
                background-color: #0f172a;
                border-radius: 25px;
                padding: 30px;
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

        main_layout = QVBoxLayout()

        card = QFrame()
        card_layout = QVBoxLayout()
        card_layout.setSpacing(20)

        title = QLabel("🎓 Skillforge Certificates")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 28, QFont.Bold))
        title.setStyleSheet("color: #22c55e; margin-bottom: 10px;")

        info = QLabel(
            "Generate your official Skillforge certificate\n"
            "after completing learning activities."
        )
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("""
            font-size: 18px;
            color: #94a3b8;
            margin-bottom: 20px;
        """)

        self.generate_btn = QPushButton("Generate Certificate")
        self.generate_btn.clicked.connect(self.generate_certificate)

        card_layout.addWidget(title)
        card_layout.addWidget(info)
        card_layout.addWidget(self.generate_btn)

        card.setLayout(card_layout)
        main_layout.addWidget(card)
        self.setLayout(main_layout)

    def generate_certificate(self):

        try:

            print("USERNAME:", self.username)
            print("TYPE:", type(self.username))

            # SAFE username usage
            username = str(self.username) if self.username else "Unknown_User"

            os.makedirs("assets/certificates", exist_ok=True)

            filename = f"assets/certificates/{username}_certificate.pdf"

            self.generate_btn.setText("Generating Certificate...")
            self.generate_btn.setEnabled(False)

            pdf = canvas.Canvas(
                filename,
                pagesize=landscape(A4)
            )

            width, height = landscape(A4)

            # BACKGROUND
            pdf.setFillColor(HexColor("#0f172a"))
            pdf.rect(
                0,
                0,
                width,
                height,
                fill=1
            )

            # BORDER
            pdf.setStrokeColor(HexColor("#22c55e"))
            pdf.setLineWidth(8)

            pdf.rect(
                30,
                30,
                width - 60,
                height - 60
            )

            # TITLE
            pdf.setFillColor(HexColor("#22c55e"))
            pdf.setFont(
                "Helvetica-Bold",
                34
            )

            pdf.drawCentredString(
                width / 2,
                500,
                "CERTIFICATE OF ACHIEVEMENT"
            )

            # SUBTITLE
            pdf.setFillColor(HexColor("#FFFFFF"))
            pdf.setFont(
                "Helvetica",
                20
            )

            pdf.drawCentredString(
                width / 2,
                440,
                "This certificate is proudly presented to"
            )

            # USERNAME
            pdf.setFont(
                "Helvetica-Bold",
                32
            )

            pdf.drawCentredString(
                width / 2,
                370,
                str(username)
            )

            # DESCRIPTION
            pdf.setFont(
                "Helvetica",
                18
            )

            pdf.drawCentredString(
                width / 2,
                300,
                "For successfully completing"
            )

            pdf.drawCentredString(
                width / 2,
                270,
                "Skillforge learning activities"
            )

            # FOOTER
            pdf.setFillColor(HexColor("#94a3b8"))
            pdf.setFont(
                "Helvetica-Oblique",
                16
            )

            pdf.drawCentredString(
                width / 2,
                120,
                "Skillforge Learning Management System"
            )

            pdf.save()

            QMessageBox.information(
                self,
                "Certificate Generated",
                f"Certificate saved successfully:\n\n{filename}"
            )

            webbrowser.open(
                os.path.abspath(filename)
            )

            self.generate_btn.setText(
                "Certificate Ready ✅"
            )

            self.generate_btn.setEnabled(True)

        except Exception as e:

            print("CERTIFICATE ERROR:", e)

            QMessageBox.critical(
                self,
                "Certificate Error",
                str(e)
            )

            self.generate_btn.setText(
                "Generate Certificate"
            )

            self.generate_btn.setEnabled(True)