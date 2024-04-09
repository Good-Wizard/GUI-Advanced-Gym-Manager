from data_processing.modules import QDialog, Qt, QCoreApplication, QPixmap, QPushButton, QLabel, QVBoxLayout
from gui.add_user import AddUser
from gui.show_users import Show_Users
from gui.check_users import CheckUsers


class Menu(QDialog):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Gym Management")
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)  # Remove window frame

        # Get screen resolution
        desktop = QCoreApplication.instance().desktop()
        screen_rect = desktop.availableGeometry()
        screen_width, screen_height = screen_rect.width(), screen_rect.height()

        # Create a QVBoxLayout to arrange the widgets vertically
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)  # Align widgets to the center

        # Create a label widget and set its pixmap to the background image
        background_label = QLabel(self)
        pixmap = QPixmap(r"resources\main.jpg")
        pixmap = pixmap.scaled(screen_width, screen_height)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, screen_width, screen_height)

        # Set window size and show full screen
        self.setGeometry(0, 0, screen_width, screen_height)

        # Define button style
        button_style = """
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px 24px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """

        # Add buttons to the layout
        self.add_user_button = QPushButton("💪🏻 New Membership 💪🏻", self)
        self.add_user_button.setStyleSheet(button_style)
        self.add_user_button.clicked.connect(self.add_user)
        layout.addWidget(self.add_user_button)

        self.edit_info_button = QPushButton("📝 Edit Users 📝", self)
        self.edit_info_button.setStyleSheet(button_style)
        self.edit_info_button.clicked.connect(self.edit_user)
        layout.addWidget(self.edit_info_button)

        self.check_users_button = QPushButton("📚 Check Users 📚", self)
        self.check_users_button.setStyleSheet(button_style)
        self.check_users_button.clicked.connect(self.check_users)
        layout.addWidget(self.check_users_button)

        self.exit_button = QPushButton("💠 Exit 💠", self)
        self.exit_button.setStyleSheet(button_style)
        self.exit_button.clicked.connect(self.Exit)
        layout.addWidget(self.exit_button)


    def Exit(self):
        exit()

    def add_user(self):
        adduser = AddUser()
        adduser.exec_()

    def edit_user(self):
        edit_user = Show_Users()
        edit_user.exec_()

    def check_users(self):
        check_users = CheckUsers()
        check_users.exec_()