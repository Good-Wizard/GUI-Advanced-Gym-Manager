from PyQt5.QtWidgets import QApplication
from gui.login import Login
from data_processing.control_DataBase import Data_Base
from css_styles.styles import dark_theme

if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(dark_theme)
    login_screen = Login()  # Instantiate the Login class
    Data_Base()
    login_screen.show()
    app.exec_()