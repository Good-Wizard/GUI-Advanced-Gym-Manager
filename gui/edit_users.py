from data_processing.modules import QDialog, Qt, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QFormLayout, QComboBox, QDateEdit, QDate, QTextEdit, QHBoxLayout, Error, connect
from data_processing.saving_errors import save_error
from css_styles.styles import date_edit_style, combo_box_style


class Edit_User(QDialog):
    def __init__(self, user_data):
        super().__init__()
        self.setWindowTitle("Edit User")
        self.setGeometry(400, 80, 500, 500)

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.user_data = user_data

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter Full Name")

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter Email (Optional)")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Enter Phone Number")

        self.gender_input = QComboBox(self)
        self.gender_input.addItems(["Male", "Female"])

        self.birth_input = QDateEdit(self)
        self.birth_input.setDisplayFormat("yyyy/MM/dd")
        self.birth_input.setCalendarPopup(True)

        self.address_input = QTextEdit(self)
        self.address_input.setPlaceholderText("Enter Address (Optional)")

        self.height_input = QLineEdit(self)
        self.height_input.setPlaceholderText("Enter Height (Optional)")

        self.weight_input = QLineEdit(self)
        self.weight_input.setPlaceholderText("Enter Weight (Optional)")

        self.duration_input = QLineEdit(self)
        self.duration_input.setPlaceholderText("Enter Duration (1 = 30 Days)")
        self.save_button = QPushButton("Save", self)
        self.delete_button = QPushButton("Remove User", self)
        self.cancel_button = QPushButton("Cancel", self)

        self.name_input.setText(self.user_data['name'])
        self.email_input.setText(self.user_data['email'])
        self.phone_input.setText(self.user_data['phone'])
        self.gender_input.setCurrentText(self.user_data['gender'])
        self.birth_input.setDate(QDate.fromString(self.user_data['birth_date'], Qt.ISODate))
        self.birth_input.setStyleSheet(date_edit_style)
        self.address_input.setPlainText(self.user_data['address'])
        self.height_input.setText(str(self.user_data['height']))
        self.weight_input.setText(str(self.user_data['weight']))
        self.duration_input.setText(str(self.user_data['duration']))

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
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.save_button)

        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        self.save_button.clicked.connect(self.save_changes)
        self.cancel_button.clicked.connect(self.close)
        self.delete_button.clicked.connect(self.delete_user)

        self.birth_input.setDisplayFormat("yyyy/MM/dd")
        self.gender_input.setStyleSheet(combo_box_style)
        self.birth_input.setStyleSheet(date_edit_style)
        self.setLayout(layout)

    def save_changes(self):
        # Validate required fields
        if not self.name_input.text():
            QMessageBox.warning(self, "Error", "Name field is required.")
            return

        self.user_data['name'] = self.name_input.text()
        self.user_data['email'] = self.email_input.text()
        self.user_data['phone'] = self.phone_input.text()
        self.user_data['gender'] = self.gender_input.currentText()
        self.user_data['birth_date'] = self.birth_input.date().toString(Qt.ISODate)
        self.user_data['address'] = self.address_input.toPlainText()

        try:
            if self.height_input.text():
                self.user_data['height'] = float(self.height_input.text())
            else:
                self.user_data['height'] = ""
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input for Height. Please enter a valid number.")
            return

        try:
            if self.weight_input.text():
                self.user_data['weight'] = float(self.weight_input.text())
            else:
                self.user_data['weight'] = ""
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input for Weight. Please enter a valid number.")
            return

        try:
            self.user_data['duration'] = int(self.duration_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input for Duration. Please enter a valid integer.")
            return

        try:
            with connect('gym.db') as connection:
                cursor = connection.cursor()
                cursor.execute("""UPDATE users 
                                  SET name=?, email=?, phone=?, gender=?, birth_date=?, 
                                      address=?, height=?, weight=?, duration=?
                                  WHERE id=?""",
                               (self.user_data['name'], self.user_data['email'],
                                self.user_data['phone'], self.user_data['gender'],
                                self.user_data['birth_date'], self.user_data['address'],
                                self.user_data['height'], self.user_data['weight'],
                                self.user_data['duration'], self.user_data['id']))
                connection.commit()
        except Error as e:
            QMessageBox.warning(self, "Error", "An error occurred while updating user data. Please try again or contact the developer.")
            save_error(f"Update User: {e}")
        finally:
            try:
                connection.close()
            except NameError:
                pass
            self.accept()
            QMessageBox.information(self, "", f"{self.user_data['name']} information was successfully changed.")

    def delete_user(self):
        confirm = QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to delete {self.user_data['name']}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                with connect('gym.db') as connection:
                    cursor = connection.cursor()
                    cursor.execute("DELETE FROM users WHERE id=?", (self.user_data['id'],))
                    connection.commit()
            except Error as e:
                QMessageBox.warning(self, "Error", "An error occurred while deleting user data. Please try again or contact the developer.")
                save_error(f"Delete User: {e}")
            finally:
                try:
                    connection.close()
                except NameError:
                    pass
                self.accept()
                QMessageBox.information(self, "", f"{self.user_data['name']} data was successfully deleted.")