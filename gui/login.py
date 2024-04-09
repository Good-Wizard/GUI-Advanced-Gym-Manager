from data_processing.modules import QDialog, Qt, QCoreApplication, QPixmap, QLineEdit, QPushButton, QLabel, QMessageBox
from gui.menu import Menu

class Login(QDialog):
    def __init__(self):
        super().__init__()

        # Set Window Title
        self.setWindowTitle("Login")
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)  # Remove window frame

        # Get screen resolution
        desktop = QCoreApplication.instance().desktop()
        screen_rect = desktop.availableGeometry()
        screen_width, screen_height = screen_rect.width(), screen_rect.height()
        # Create a label widget and set its pixmap to the background image
        background_label = QLabel(self)
        pixmap = QPixmap(r"resources\login.jpg")
        pixmap = pixmap.scaled(screen_width, screen_height)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, screen_width, screen_height)

        # Password Input Field
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter Password 🔒")
        self.password_input.setStyleSheet("QLineEdit { padding: 10px; border: 2px solid #0078d4; border-radius: 5px; }")
        self.password_input.setGeometry(screen_width//2 - 100, 150, 200, 50)

        # Submit Button
        self.submit_button = QPushButton("Login 👨🏻‍💻", self)
        self.submit_button.setStyleSheet("QPushButton { background-color: #0078d4; color: white; border: none; padding: 10px 20px; border-radius: 5px; } QPushButton:hover { background-color: #005a9e; }")
        self.submit_button.setGeometry(screen_width//2 - 100, 210, 200, 50)
        self.submit_button.clicked.connect(self.check_password)

        # Exit Button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setStyleSheet("QPushButton { background-color: #0078d4; color: white; border: none; padding: 10px 20px; border-radius: 5px; } QPushButton:hover { background-color: #005a9e; }")
        self.exit_button.setGeometry(screen_width//2 - 100, 270, 200, 50)
        self.exit_button.clicked.connect(self.Exit)

        # Set the Master Password
        self.master_password = "qw"

    def Exit(self):
        exit()

    def check_password(self):
        if self.password_input.text() == self.master_password:
            # If the password is correct, close the login window and open the Menu window
            self.close()
            self.menu_window = Menu()
            self.menu_window.show()
        else:
            # If the password is incorrect, display an error message
            QMessageBox.warning(self, "❌", "Invalid Password ❌")
            self.password_input.clear()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.check_password()