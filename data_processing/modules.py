from sys import exit, argv
from PyQt5.QtGui import QColor, QFont, QPixmap
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QDialog, QFormLayout, QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QComboBox, QDateEdit, QTextEdit, QMessageBox, QWidget
from PyQt5.QtCore import QCoreApplication, Qt, QDate
from sqlite3 import connect, Error
from datetime import datetime, date
from os.path import exists, join
from os import getcwd