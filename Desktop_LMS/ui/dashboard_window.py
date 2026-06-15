from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout,
    QFrame, QScrollArea, QHBoxLayout
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from ui.quiz_window import QuizWindow
from ui.courses_window import CoursesWindow
from ui.progress_window import ProgressWindow
from ui.profile_window import ProfileWindow
from ui.certificate_window import CertificateWindow
from ui.video_window import VideoWindow
from ui.assignment_window import AssignmentWindow
from ui.settings_window import SettingsWindow
from ui.ai_tutor_window import AITutorWindow
from ui.study_planner_window import StudyPlannerWindow
from ui.achievement_window import AchievementWindow
from ui.code_lab_window import CodeLabWindow
from styles import get_theme, toggle_theme


class DashboardWindow(QWidget):

    def __init__(self, username):
        super().__init__()

        self.username = username

        self.setWindowTitle("Skillforge Dashboard")
        self.setGeometry(250, 80, 1400, 850)
        self.setStyleSheet(get_theme())

        # =========================
        # GLOBAL STYLE
        # =========================

        self.setStyleSheet("""
            QWidget {
                background-color: #050816;
                color: white;
                font-family: Segoe UI;
            }

            QScrollArea {
                border: none;
            }

            QFrame {
                background-color: #0f172a;
                border-radius: 20px;
            }
        """)

        # =========================
        # SIDEBAR
        # =========================

        sidebar = QFrame()
        sidebar.setFixedWidth(260)

        sidebar.setStyleSheet("""
            QFrame {
                background-color: #0b1120;
                border-right: 3px solid #22c55e;
                border-radius: 0px;
            }
        """)

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(20, 30, 20, 20)
        sidebar_layout.setSpacing(12)

        # =========================
        # LOGO
        # =========================

        logo = QLabel("Skillforge")
        logo.setFont(QFont("Segoe UI", 26, QFont.Bold))
        logo.setStyleSheet("""
            color: #22c55e;
            margin-bottom: 20px;
        """)

        sidebar_layout.addWidget(logo)

        # =========================
        # SECTION LABELS
        # =========================

        learning_label = QLabel("LEARNING")
        learning_label.setStyleSheet("""
            color: #94a3b8;
            font-size: 13px;
            font-weight: bold;
            margin-top: 10px;
        """)

        progress_label = QLabel("PROGRESS")
        progress_label.setStyleSheet("""
            color: #94a3b8;
            font-size: 13px;
            font-weight: bold;
            margin-top: 15px;
        """)

        account_label = QLabel("ACCOUNT")
        account_label.setStyleSheet("""
            color: #94a3b8;
            font-size: 13px;
            font-weight: bold;
            margin-top: 15px;
        """)

        # =========================
        # BUTTONS
        # =========================

        self.quiz_btn = QPushButton("📝 Quiz System")
        self.course_btn = QPushButton("📚 Courses")
        self.progress_btn = QPushButton("📈 Progress")
        self.profile_btn = QPushButton("👤 Profile")
        self.certificate_btn = QPushButton("🎓 Certificates")
        self.video_btn = QPushButton("🎥 Video Lessons")
        self.assignment_btn = QPushButton("📝 Assignments")
        self.settings_btn = QPushButton("⚙ Settings")
        self.ai_btn = QPushButton("🤖 AI Tutor")
        self.study_btn = QPushButton("📅 Study Planner")
        self.achievement_btn = QPushButton("🏅 Achievements")
        self.codelab_btn = QPushButton("💻 Code Lab")

        button_style = """
        QPushButton {
            background-color: #111827;
            border: none;
            border-radius: 14px;
            min-height: 55px;
            text-align: left;
            padding-left: 20px;
            font-size: 15px;
            font-weight: bold;
            color: white;
        }

        QPushButton:hover {
            background-color: #1e293b;
            border-left: 5px solid #22c55e;
        }
        """

        buttons = [
            self.quiz_btn,
            self.course_btn,
            self.progress_btn,
            self.profile_btn,
            self.certificate_btn,
            self.video_btn,
            self.assignment_btn,
            self.settings_btn,
            self.ai_btn,
            self.study_btn,
            self.achievement_btn,
            self.codelab_btn
        ]

        for btn in buttons:
            btn.setStyleSheet(button_style)

        # =========================
        # SIDEBAR BUTTONS
        # =========================

        sidebar_layout.addWidget(learning_label)

        sidebar_layout.addWidget(self.course_btn)
        sidebar_layout.addWidget(self.video_btn)
        sidebar_layout.addWidget(self.quiz_btn)
        sidebar_layout.addWidget(self.assignment_btn)
        sidebar_layout.addWidget(self.ai_btn)
        sidebar_layout.addWidget(self.codelab_btn)

        sidebar_layout.addWidget(progress_label)

        sidebar_layout.addWidget(self.progress_btn)
        sidebar_layout.addWidget(self.achievement_btn)
        sidebar_layout.addWidget(self.certificate_btn)

        sidebar_layout.addWidget(account_label)

        sidebar_layout.addWidget(self.profile_btn)
        sidebar_layout.addWidget(self.study_btn)
        sidebar_layout.addWidget(self.settings_btn)

        sidebar_layout.addStretch()

        sidebar.setLayout(sidebar_layout)

        # =========================
        # CONNECTIONS
        # =========================

        self.quiz_btn.clicked.connect(self.open_quiz)
        self.course_btn.clicked.connect(self.open_courses)
        self.progress_btn.clicked.connect(self.open_progress)
        self.profile_btn.clicked.connect(self.open_profile)
        self.certificate_btn.clicked.connect(self.open_certificate)
        self.video_btn.clicked.connect(self.open_videos)
        self.assignment_btn.clicked.connect(self.open_assignments)
        self.settings_btn.clicked.connect(self.open_settings)
        self.ai_btn.clicked.connect(self.open_ai_tutor)
        self.study_btn.clicked.connect(self.open_study_planner)
        self.achievement_btn.clicked.connect(self.open_achievements)
        self.codelab_btn.clicked.connect(self.open_codelab)

        # =========================
        # MAIN CONTENT
        # =========================

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(30, 30, 30, 30)
        content_layout.setSpacing(25)

        # =========================
        # TITLE
        # =========================

        title = QLabel(f"Welcome back, {self.username} 👋")
        title.setFont(QFont("Segoe UI", 30, QFont.Bold))
        title.setStyleSheet("color: white;")

        subtitle = QLabel(
            "Continue learning and track your progress with Skillforge LMS."
        )

        subtitle.setStyleSheet("""
            color: #94a3b8;
            font-size: 17px;
        """)

        content_layout.addWidget(title)
        content_layout.addWidget(subtitle)

        # =========================
        # QUICK ACCESS CARD
        # =========================

        quick_card = QFrame()

        quick_card.setStyleSheet("""
            QFrame {
                background-color: #0f172a;
                border: 2px solid #22c55e;
                border-radius: 20px;
            }
        """)

        quick_layout = QVBoxLayout()
        quick_layout.setContentsMargins(25, 25, 25, 25)
        quick_layout.setSpacing(15)

        quick_title = QLabel("🚀 Quick Access")
        quick_title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        quick_title.setStyleSheet("color: #22c55e;")

        quick_layout.addWidget(quick_title)

        # =========================
        # QUICK BUTTONS
        # =========================

        top_row = QHBoxLayout()
        bottom_row = QHBoxLayout()

        card_style = """
        QPushButton {
            background-color: #111827;
            border: 2px solid #1e293b;
            border-radius: 18px;
            min-height: 110px;
            font-size: 17px;
            font-weight: bold;
            color: white;
        }

        QPushButton:hover {
            border: 2px solid #22c55e;
            background-color: #1e293b;
        }
        """

        self.quick_course = QPushButton("📚\nCourses")
        self.quick_video = QPushButton("🎥\nVideos")
        self.quick_ai = QPushButton("🤖\nAI Tutor")
        self.quick_quiz = QPushButton("📝\nQuiz")

        quick_buttons = [
            self.quick_course,
            self.quick_video,
            self.quick_ai,
            self.quick_quiz
        ]

        for btn in quick_buttons:
            btn.setStyleSheet(card_style)

        self.quick_course.clicked.connect(self.open_courses)
        self.quick_video.clicked.connect(self.open_videos)
        self.quick_ai.clicked.connect(self.open_ai_tutor)
        self.quick_quiz.clicked.connect(self.open_quiz)

        top_row.addWidget(self.quick_course)
        top_row.addWidget(self.quick_video)

        bottom_row.addWidget(self.quick_ai)
        bottom_row.addWidget(self.quick_quiz)

        quick_layout.addLayout(top_row)
        quick_layout.addLayout(bottom_row)

        quick_card.setLayout(quick_layout)

        # =========================
        # ANNOUNCEMENTS
        # =========================

        announcement_card = QFrame()
        announcement_card.setMaximumHeight(220)

        announcement_card.setStyleSheet("""
            QFrame {
                background-color: #111827;
                border: none;
                border-radius: 20px;
            }
        """)

        announcement_layout = QVBoxLayout()
        announcement_layout.setContentsMargins(25, 25, 25, 25)

        announce_title = QLabel("📢 Announcements")
        announce_title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        announce_title.setStyleSheet("color: #22c55e;")

        announce_text = QLabel(
            "• Welcome to Skillforge LMS\n\n"
            "• New lessons available\n\n"
            "• Complete quizzes to earn XP\n\n"
            "• More features coming soon"
        )

        announce_text.setWordWrap(True)

        announce_text.setStyleSheet("""
            font-size: 16px;
            color: white;
        """)

        announcement_layout.addWidget(announce_title)
        announcement_layout.addWidget(announce_text)

        announcement_card.setLayout(announcement_layout)

        # =========================
        # ADD TO CONTENT
        # =========================

        content_layout.addWidget(quick_card)
        content_layout.addWidget(announcement_card)
        content_layout.addStretch()

        # =========================
        # SCROLL AREA
        # =========================

        content_widget = QWidget()
        content_widget.setLayout(content_layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(content_widget)

        # =========================
        # MAIN LAYOUT
        # =========================

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(scroll)

        self.setLayout(main_layout)

    # =========================
    # FUNCTIONS
    # =========================

    def open_quiz(self):
        self.quiz = QuizWindow(self.username)
        self.quiz.show()

    def open_courses(self):
        self.courses = CoursesWindow(self.username)
        self.courses.show()

    def open_progress(self):
        self.progress = ProgressWindow(self.username)
        self.progress.show()

    def open_profile(self):
        self.profile = ProfileWindow(self.username)
        self.profile.show()

    def open_certificate(self):
        self.certificate = CertificateWindow(self.username)
        self.certificate.show()

    def open_videos(self):
        self.videos = VideoWindow()
        self.videos.show()

    def open_assignments(self):
        self.assignments = AssignmentWindow()
        self.assignments.show()

    def open_settings(self):
        self.settings = SettingsWindow()
        self.settings.show()

    def open_ai_tutor(self):
        self.ai = AITutorWindow()
        self.ai.show()

    def open_study_planner(self):
        self.study = StudyPlannerWindow()
        self.study.show()

    def open_achievements(self):
        self.achievements = AchievementWindow(self.username)
        self.achievements.show()

    def open_codelab(self):
        self.codelab = CodeLabWindow()
        self.codelab.show()

