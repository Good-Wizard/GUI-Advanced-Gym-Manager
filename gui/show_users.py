from data_processing.modules import QDialog, Qt, QMessageBox, QListWidget, QVBoxLayout, QListWidgetItem, connect, Error
from data_processing.saving_errors import save_error
from css_styles.styles import user_info_style
from gui.edit_users import Edit_User

class Show_Users(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("کاربران")
        self.setGeometry(500, 200, 300, 300)

        layout = QVBoxLayout(self)

        self.user_info = QListWidget(self)
        self.user_info.setStyleSheet(user_info_style)
        self.user_info.itemClicked.connect(self.show_user_details)

        # Simulated user data
        self.populate_user_info()

        layout.addWidget(self.user_info)
        self.setLayout(layout)
        self.details_window = None

    def populate_user_info(self):
        users_data = self.get_users_data()
        for user in users_data:
            item = QListWidgetItem(f"{user[0]} - {user[1]}", self.user_info)
            item.setData(Qt.UserRole, user)  # Store user data in item
            self.user_info.addItem(item)

    def show_user_details(self, item):
        user_data = item.data(Qt.UserRole)  # Retrieve user data from item
        if user_data:  # Ensure user_data is not None
            user_dict = {
                'id': user_data[0],  # Assuming user ID is the first element
                'name': user_data[1],
                'email': user_data[2],
                'phone': user_data[3],
                'gender': user_data[4],
                'birth_date': user_data[5],
                'address': user_data[6],
                'height': user_data[7],
                'weight': user_data[8],
                'duration': user_data[9],
                'date': user_data[10]
            }
            self.details_window = Edit_User(user_dict)
            self.close()  # Close class one window
            self.details_window.exec_()

    def get_users_data(self):
        try:
            with connect('gym.db') as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users")
                users_data = cursor.fetchall()
            return users_data
        except Error as e:
            QMessageBox.warning(self, "❌", "Unknown Error ❌, Please Try Again  OR Contact Developer 👨🏻‍💻")
            save_error(f"Get Users Data: {e}")
            return []