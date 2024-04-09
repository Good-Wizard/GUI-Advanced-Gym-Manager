from data_processing.modules import QDialog, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QComboBox, QTextEdit, QDateEdit, QDate, QHBoxLayout, QFormLayout, date, connect
from css_styles.styles import date_edit_style, combo_box_style

class AddUser(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Membership")
        self.setGeometry(400, 80, 500, 500)

        layout = QVBoxLayout(self)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter Full Name")

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter Email (Optional)")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Enter Phone Number")

        self.gender_input = QComboBox(self)
        self.gender_input.addItems(["Male", "Female"])
        self.gender_input.setStyleSheet(combo_box_style)

        self.birth_input = QDateEdit(self)
        self.birth_input.setDisplayFormat("yyyy/MM/dd")
        self.birth_input.setCalendarPopup(True)
        self.birth_input.setStyleSheet(date_edit_style)

        self.address_input = QTextEdit(self)
        self.address_input.setPlaceholderText("Enter Address (Optional)")

        self.height_input = QLineEdit(self)
        self.height_input.setPlaceholderText("Enter Height (Optional)")

        self.weight_input = QLineEdit(self)
        self.weight_input.setPlaceholderText("Enter Weight (Optional)")

        self.duration_input = QLineEdit(self)
        self.duration_input.setPlaceholderText("Enter Duration (1 = 30 Days)")

        self.save_button = QPushButton("Add It", self)
        self.cancel_button = QPushButton("Cancel", self)

        form_layout = QFormLayout()
        form_layout.addRow(self.name_input)
        form_layout.addRow(self.email_input)
        form_layout.addRow(self.phone_input)
        form_layout.addRow(self.gender_input)
        form_layout.addRow(self.birth_input)
        form_layout.addRow(self.address_input)
        form_layout.addRow(self.height_input)
        form_layout.addRow(self.weight_input)
        form_layout.addRow(self.duration_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)

        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        self.save_button.clicked.connect(self.save_user)
        self.cancel_button.clicked.connect(self.close)

        self.setLayout(layout)

    def save_user(self):
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        gender = self.gender_input.currentText()
        birth = self.birth_input.date().toString("yyyy/MM/dd")
        address = self.address_input.toPlainText()
        height = self.height_input.text()
        weight = self.weight_input.text()
        duration = self.duration_input.text()

        # Validation for required fields
        if not name or not phone or not duration:
            QMessageBox.warning(self, "Error", "Name, Phone Number, and Duration are required fields.")
            return

        # Additional validation for numeric fields
        if height and not height.replace(".", "", 1).isdigit():
            QMessageBox.warning(self, "Error", "Please enter a valid height.")
            return

        if weight and not weight.replace(".", "", 1).isdigit():
            QMessageBox.warning(self, "Error", "Please enter a valid weight.")
            return

        if duration and not duration.isdigit():
            QMessageBox.warning(self, "Error", "Duration should be a number.")
            return

        # Database connection and data insertion
        current_date = date.today().strftime("%Y-%m-%d")
        conn = connect('gym.db')
        c = conn.cursor()

        c.execute('''
            INSERT INTO users (name, email, phone, gender, birth_date, address, height, weight, duration, date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, email, phone, gender, birth, address, height, weight, duration, current_date))

        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success", "User information saved successfully.")
        self.clear_input_fields()

    def clear_input_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()
        self.gender_input.setCurrentIndex(0)
        self.birth_input.setDate(QDate.currentDate())
        self.address_input.clear()
        self.height_input.clear()
        self.weight_input.clear()
        self.duration_input.clear()
