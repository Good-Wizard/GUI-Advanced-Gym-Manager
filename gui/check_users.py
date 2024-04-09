from data_processing.modules import QDialog, Qt, QLabel, QMessageBox, QVBoxLayout, QTableWidget, QAbstractItemView, QFont, QColor, QTableWidgetItem, Error, connect, datetime
from data_processing.saving_errors import save_error


class CheckUsers(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(470, 150, 439, 500)  # Set Size Screen
        self.setFixedSize(439, 500)

        self.layout = QVBoxLayout(self)

        self.user_info = QTableWidget(self)
        self.user_info.setColumnCount(4)
        self.user_info.setHorizontalHeaderLabels(["Name", "Duration", "Registration", "Time Remaining"])

        # Set alternating row colors for better readability
        self.user_info.setAlternatingRowColors(True)

        # Disable Edit Values
        self.user_info.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Simulated user data
        self.populate_user_info()

        # Set header style
        header_style = """
            QHeaderView::section {
                background-color: #2b2b2b;
                color: white;
            }
        """
        self.user_info.horizontalHeader().setStyleSheet(header_style)

        self.layout.addWidget(self.user_info)
        self.setLayout(self.layout)
        self.details_window = None

    def populate_user_info(self):
        font = QFont()
        font.setFamily("Comic Sans MS")

        users_data = self.get_users_data()

        total_users = len(users_data)
        expired_users = 0
        less_than_seven_days_users = 0

        for user in users_data:
            time_remaining = self.Time_remaining(user[10], user[9])

            if time_remaining <= 0:
                expired_users += 1
            elif time_remaining <= 7:
                less_than_seven_days_users += 1

        info_label = QLabel(f"<span style='color:#22FF00;font-size: 12pt;font-family: 'Comic Sans MS''>  Total Users: {total_users}</span> - <span style='color:#FF0000;font-size: 12pt;font-family: 'Comic Sans MS''>Expired Users: {expired_users}</span> - <span style='color:#FF4300;font-size: 12pt;font-family: 'Comic Sans MS''>Near Expiry: {less_than_seven_days_users}</span>")
        self.layout.addWidget(info_label)

        sorted_users_data = sorted(users_data, key=lambda user: self.Time_remaining(user[10], user[9]))

        self.user_info.setRowCount(len(sorted_users_data))
        for row, user in enumerate(sorted_users_data):
            time_remaining = self.Time_remaining(user[10], user[9])
            if time_remaining <= 0:
                time_text = "Expired"
                background_color = "#8C0000"
                text_color = "white"
            elif time_remaining <= 7:
                time_text = f"{time_remaining} Days Left"
                background_color = "#8C2500"
                text_color = "white"
            else:
                time_text = f"{time_remaining} Days Left"
                background_color = "#2b2b2b"
                text_color = "white"

            for col, data in enumerate([user[1], f"{user[9]} Month", user[10], time_text]):
                item = QTableWidgetItem(data)
                item.setBackground(QColor(background_color))
                item.setForeground(QColor(text_color))

                item.setFont(font)
                item.setTextAlignment(Qt.AlignCenter)

                self.user_info.setItem(row, col, item)

        self.user_info.setStyleSheet("QTableWidget {background-color: #333333; color: white;}")

    def Time_remaining(self, registration_date, duration):
        end_date = datetime.strptime(registration_date, "%Y-%m-%d") + datetime.timedelta(days=duration * 30)
        remaining_days = (end_date - datetime.now()).days
        return remaining_days

    def get_users_data(self):
        try:
            with connect('gym.db') as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users")
                users_data = cursor.fetchall()
            return users_data
        except Error as e:
            QMessageBox.warning(self, "Error", "An error occurred while fetching user data. Please try again or contact the developer.")
            save_error(f"Get Users Data: {e}")
            return []