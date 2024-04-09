user_info_style = ("""
    QListWidget {
        font-family: "Comic Sans MS", IranNastaliq;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        padding: 10px;
    }
    
    QListWidget::item {
        color: #333;
        padding: 5px;
    }
    
    QListWidget::item:hover {
        background-color: #e0e0e0;
        border-radius: 5px;
    }
""")
combo_box_style = ("""
QComboBox {
    background-color: #333333; /* Background color for dark mode */
    border: 2px solid #B2302D; /* Red border */
    border-radius: 5px; /* Border radius */
    padding: 5px; /* Padding */
    font-size: 14px; /* Font size */
    color: #ffffff; /* White text color */
}

QComboBox:hover {
    border-color: #3A8E3E; /* Green border on hover */
}

QComboBox::drop-down {
    width: 20px; /* Width of the drop-down button */
    border-left: 2px solid #B2302D; /* Red border for the drop-down button */
    border-top-right-radius: 5px; /* Border radius for the drop-down button */
    border-bottom-right-radius: 5px; /* Border radius for the drop-down button */
    background-color: #333333; /* Background color for the drop-down button */
}

QComboBox::down-arrow {
    image: url(down_arrow.png); /* Image for the drop-down arrow */
}

QComboBox::item {
    background-color: #333333; /* Background color for items */
    color: #ffffff; /* Text color for items */
}

QComboBox::item:selected {
    background-color: #4a4a4a; /* Background color for selected item */
    color: #ffffff; /* Text color for selected item */
}
""")

date_edit_style = ("""
QDateEdit {
    background-color: #333333; /* Background color for dark mode */
    border: 2px solid #B2302D; /* Red border */
    border-radius: 5px; /* Border radius */
    padding: 5px; /* Padding */
    font-size: 14px; /* Font size */
    color: #ffffff; /* White text color */
}

QDateEdit::drop-down {
    width: 20px; /* Width of the drop-down button */
    border-left: 2px solid #B2302D; /* Red border for the drop-down button */
    border-top-right-radius: 5px; /* Border radius for the drop-down button */
    border-bottom-right-radius: 5px; /* Border radius for the drop-down button */
    background-color: #333333; /* Background color for the drop-down button */
}

QDateEdit::down-arrow {
    image: url(down_arrow.png); /* Image for the drop-down arrow */
}

QDateEdit:hover {
    border-color: #3A8E3E; /* Green border on hover */
}

QCalendarWidget {
    background-color: #333333; /* Background color for the calendar pop-up in dark mode */
    border: 2px solid #3A8E3E; /* Red border for the calendar pop-up */
    border-radius: 5px; /* Border radius for the calendar pop-up */
}

QCalendarWidget QToolButton {
    background-color: transparent; /* Transparent background for calendar buttons */
    color: #ffffff; /* White text color for calendar buttons */
    font-size: 12px; /* Font size for calendar buttons */
}

QCalendarWidget QToolButton:hover {
    background-color: #3A8E3E; /* Green background for hovered calendar buttons */
}
""")

entry_style = ("""
    QLineEdit {
        font-family: "Comic Sans MS", IranNastaliq;
        width: 200px;
        height: 40px;
        border-radius: 5px;
        border: 2px solid #B2302D;
        background-color: #111111;
        font-size: 15px;
        font-weight: 600;
        color: #fefefe;
        padding: 5px 10px;
        outline: none;
    }
    QLineEdit:placeholder-text {
        color: #7e7e7e;
        opacity: 0.8;
    }
              
    QLineEdit:hover {
        border: 2px solid #3A8E3E;
    }
    QLineEdit:focus {
        border: 2px solid #3A8E3E;
    }
""")

dark_theme = ("""
    QWidget {
        background-color: #2b2b2b;
        font-family: "Comic Sans MS", IranNastaliq;
        color: #e0e0e0;
    }

    QLabel {
        color: #e0e0e0;
    }

    QLineEdit {
        width: 200px;
        height: 20px;
        border-radius: 5px;
        border: 2px solid #B2302D;
        background-color: #111111;
        font-size: 15px;
        font-weight: 600;
        color: #fefefe;
        padding: 5px 10px;
        outline: none;
    }
    QLineEdit:placeholder-text {
        color: #7e7e7e;
        opacity: 0.8;
    }
    QLineEdit:focus {
        border: 2px solid #3A8E3E;
    }

    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }

    QPushButton:hover {
        background-color: #45a049;
    }

    QPushButton:pressed {
        background-color: #093300;
    }
    QTextEdit {
        background-color: #2b2b2b; /* Background color */
        border: 2px solid #B2302D; /* Border color */
        border-radius: 5px; /* Border radius */
        padding: 5px; /* Padding */
        font-size: 14px; /* Font size */
        color: #e0e0e0; /* Text color */
    }

    QTextEdit:hover {
        border: 2px solid #3A8E3E;
    }
      
    QTextEdit:focus {
        border: 2px solid #3A8E3E;
    }
""")