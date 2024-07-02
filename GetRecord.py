import sys
import requests
import subprocess
import tempfile
import os
from PyQt5 import QtCore, QtWidgets, QtGui
from datetime import datetime, time, timedelta
import mysql.connector
import time as time_module

import win32print
import win32ui
from PIL import Image, ImageWin, ImageDraw, ImageFont
import win32con
import tempfile

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime, timedelta
import sys
from PyQt5.QtCore import pyqtSignal, QTime
import json

import pandas as pd
import mysql.connector
from datetime import datetime

from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtCore import QDate

import mysql.connector
from mysql.connector import Error

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDateEdit, QPushButton, QApplication, QWidget

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Ui_Dialog(QtCore.QObject):
    mealTimesUpdated = QtCore.pyqtSignal(dict)
    specialEmployeeUpdated = QtCore.pyqtSignal(str, int)  # Add this signal

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setWindowTitle("Employee Meal Token System Dashboard")

        self.widget_5 = QtWidgets.QWidget(Dialog)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.widget_5.setObjectName("widget_5")
        # self.widget_5.setStyleSheet("background-color: #FBFAFA;")  # Sets a dark grey background color



        # # Image Label replacing Title Label
        # self.imageLabel = QtWidgets.QLabel(self.widget_5)
        # self.imageLabel.setGeometry(QtCore.QRect(20, 30, 250, 50))  # Adjust size as necessary
        # self.imageLabel.setObjectName("imageLabel")
        # self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

        # # Load an image
        # pixmap = QtGui.QPixmap(r"images\logo.png")
        # pixmap = pixmap.scaled(600, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)  # Resize image to fit label
        # self.imageLabel.setPixmap(pixmap)

                # Image Label for Logo
        self.imageLabel = QtWidgets.QLabel(self.widget_5)
        self.imageLabel.setGeometry(QtCore.QRect(10, 15, 200, 50))
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        logo_pixmap = QtGui.QPixmap(resource_path('images/logo.png')).scaled(400, 40, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.imageLabel.setPixmap(logo_pixmap)

        
         # Common setup for image loading
        def setup_card_image(card_widget, image_path):
            image_label = QtWidgets.QLabel(card_widget)
            image_label.setGeometry(QtCore.QRect(10, 60, 180, 120))  # Adjust size and position as needed
            pixmap = QtGui.QPixmap(image_path)
            pixmap = pixmap.scaled(180, 120, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            image_label.setPixmap(pixmap)
            return image_label
        
        # Breakfast Card Setup
        self.breakfastCard = QtWidgets.QWidget(self.widget_5)
        self.breakfastCard.setGeometry(QtCore.QRect(20, 80, 400, 150))
        self.breakfastCard.setStyleSheet("background-color: #f7faf9; border-radius: 10px;")
        self.applyShadow(self.breakfastCard)
        
        self.breakfastImageLabel = QtWidgets.QLabel(self.breakfastCard)
        self.breakfastImageLabel.setGeometry(QtCore.QRect(20, 50, 140, 80))
        pixmap = QtGui.QPixmap(resource_path('images/breakfast.png'))
        pixmap = pixmap.scaled(120, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.breakfastImageLabel.setPixmap(pixmap)

        self.breakfastLabel = QtWidgets.QLabel(self.breakfastCard)
        self.breakfastLabel.setGeometry(QtCore.QRect(10, 10, 120, 20))
        self.breakfastLabel.setText("Breakfast")
        self.breakfastLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.breakfastLabel.setStyleSheet("color: black; font-size: 24px; font-weight: bold;")

        
        # # Meal Type Label for Breakfast
        # self.breakfastLabel = QtWidgets.QLabel(self.breakfastCard)
        # self.breakfastLabel.setGeometry(QtCore.QRect(10, 10, 180, 40))  # Top-left corner
        # self.breakfastLabel.setText("Breakfast")
        # self.breakfastLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.breakfastLabel.setStyleSheet("color: black; font-size: 24px; font-weight: bold;")

        # Breakfast Label inside the card
        self.breakfastCountLabel = QtWidgets.QLabel(self.breakfastCard)
        self.breakfastCountLabel.setGeometry(QtCore.QRect(180, 30, 190, 100))  # Adjusted to bottom-right
        self.breakfastCountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.breakfastCountLabel.setStyleSheet("color: #8B4513; font-size: 60px;")
        # self.breakfastCountLabel.setText("Breakfast: 0")

        # Lunch Card Setup
        self.lunchCard = QtWidgets.QWidget(self.widget_5)
        self.lunchCard.setGeometry(QtCore.QRect(435, 80, 400, 150))
        self.lunchCard.setStyleSheet("background-color: #f7faf9; border-radius: 10px;")
        self.applyShadow(self.lunchCard)
        
        self.lunchImageLabel = QtWidgets.QLabel(self.lunchCard)
        self.lunchImageLabel.setGeometry(QtCore.QRect(20, 50, 140, 80))
        pixmap = QtGui.QPixmap(resource_path('images/lunch.png'))
        pixmap = pixmap.scaled(140, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.lunchImageLabel.setPixmap(pixmap)

        self.lunchLabel = QtWidgets.QLabel(self.lunchCard)
        self.lunchLabel.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.lunchLabel.setText("Lunch")
        self.lunchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lunchLabel.setStyleSheet("color: black; font-size: 24px; font-weight: bold;")

        #  # Meal Type Label for Lunch
        # self.lunchLabel = QtWidgets.QLabel(self.lunchCard)
        # self.lunchLabel.setGeometry(QtCore.QRect(10, 10, 180, 40))  # Top-left corner
        # self.lunchLabel.setText("Lunch")
        # self.lunchLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.lunchLabel.setStyleSheet("color: black; font-size: 24px; font-weight: bold;")

       # Lunch Label inside the card
        self.lunchCountLabel = QtWidgets.QLabel(self.lunchCard)
        self.lunchCountLabel.setGeometry(QtCore.QRect(180, 30, 190, 100))  # Adjusted to bottom-right
        self.lunchCountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.lunchCountLabel.setStyleSheet("color: #8B4513; font-size: 60px;")
        # self.lunchCountLabel.setText("Lunch: 0")

        # Dinner Card Setup
        self.dinnerCard = QtWidgets.QWidget(self.widget_5)
        self.dinnerCard.setGeometry(QtCore.QRect(850, 80, 400, 150))
        self.dinnerCard.setStyleSheet("background-color: #f7faf9; border-radius: 10px;")
        self.applyShadow(self.dinnerCard)
        
        self.dinnerImageLabel = QtWidgets.QLabel(self.dinnerCard)
        self.dinnerImageLabel.setGeometry(QtCore.QRect(20, 50, 140, 80))
        pixmap = QtGui.QPixmap(resource_path('images/dinner.png'))
        pixmap = pixmap.scaled(120, 80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.dinnerImageLabel.setPixmap(pixmap)

        self.dinnerLabel = QtWidgets.QLabel(self.dinnerCard)
        self.dinnerLabel.setGeometry(QtCore.QRect(10, 10, 100, 20))
        self.dinnerLabel.setText("Dinner")
        self.dinnerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dinnerLabel.setStyleSheet("color: black; font-size: 24px; font-weight: bold;")

        # # Meal Type Label for Dinner
        # self.dinnerLabel = QtWidgets.QLabel(self.dinnerCard)
        # self.dinnerLabel.setGeometry(QtCore.QRect(10, 10, 180, 40))  # Top-left corner
        # self.dinnerLabel.setText("Dinner")
        # self.dinnerLabel.setAlignment(QtCore.Qt.AlignCenter)
        # self.dinnerLabel.setStyleSheet("color: black; font-size: 24px; font-weight: bold;")
        
        # Dinner Label inside the card
        self.dinnerCountLabel = QtWidgets.QLabel(self.dinnerCard)
        self.dinnerCountLabel.setGeometry(QtCore.QRect(180, 30, 190, 100))  # Adjusted to bottom-right
        self.dinnerCountLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.dinnerCountLabel.setStyleSheet("color: #8B4513; font-size: 60px;")
        # self.dinnerCountLabel.setText("Dinner: 0")
    
                       # Card for bottum  backgrond 
        self.manualPrintCard = QtWidgets.QWidget(self.widget_5)
        self.manualPrintCard.setGeometry(QtCore.QRect(20, 250, 1240, 450))
        self.manualPrintCard.setStyleSheet("background-color: #f7faf9; border-radius: 10px;")
        self.applyShadowBig(self.manualPrintCard)

        self.recentPrintsText = QtWidgets.QTextEdit(self.widget_5)
        self.recentPrintsText.setGeometry(QtCore.QRect(50, 270, 350, 250))  # Adjust as necessary
        self.recentPrintsText.setReadOnly(True)  # Make it read-only
        self.recentPrintsText.setStyleSheet("font-family: 'Courier New'; font-size: 10pt;  ")


        # Card for Manual print backgrond 
        self.manualPrintCard = QtWidgets.QWidget(self.widget_5)
        self.manualPrintCard.setGeometry(QtCore.QRect(420, 263, 420, 420))
        self.manualPrintCard.setStyleSheet("background-color: #f7faf9; border-radius: 10px;")
        self.applyShadowAll(self.manualPrintCard)

        # Card for bulk employee backgrond 
        self.manualPrintCard = QtWidgets.QWidget(self.widget_5)
        self.manualPrintCard.setGeometry(QtCore.QRect(860, 263, 380, 420))
        self.manualPrintCard.setStyleSheet("background-color: #f7faf9; border-radius: 10px;")
        self.applyShadowAll(self.manualPrintCard)
        
        
        # Entry field and buttons
        self.lineEdit = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit.setGeometry(QtCore.QRect(535, 320, 180, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Enter EPFNO")
        self.lineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #a3ccac; /* Soft green border */
                border-radius: 10px; /* Rounded corners */
                padding: 10px;  
                font-size: 18px;
                color: #2c3e50; /* Dark blue-grey text */
            }
            QLineEdit:focus {
                border: 2px solid #88a097; /* Darker green border for focus */
                background-color: #f0f8f0; /* Slightly different green for focus background */
            }
        """)

        # Adding print button
        self.printButton = QtWidgets.QPushButton(self.widget_5)
        self.printButton.setGeometry(QtCore.QRect(650, 390, 150, 40))
        self.printButton.setObjectName("printButton")
        self.printButton.setText("Print Record")
        self.printButton.setStyleSheet("""
            background-color: #2196f3;
            color: white;
            padding: 10px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: bold;
        """)
        
        self.printButton.setText("Print Record")
        
        self.checkButton = QtWidgets.QPushButton(self.widget_5)
        self.checkButton.setGeometry(QtCore.QRect(460, 390, 150, 40))
        self.checkButton.setObjectName("checkButton")
        self.checkButton.setStyleSheet("""
            background-color: #4caf50;
            color: white;
            padding: 10px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: bold;
        """)
        
        self.checkButton.setText("Check Records")

        # Result Table
        self.resultTable = QtWidgets.QTableWidget(self.widget_5)
        self.resultTable.setGeometry(QtCore.QRect(430, 465, 400, 200))
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(7)
        self.resultTable.setHorizontalHeaderLabels(['Token No', 'Emp Name', 'EPF No', 'Meal Type','Department', 'Print Time', 'Created At'])
        self.resultTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.resultTable.setColumnWidth(0, 80)
        self.resultTable.setColumnWidth(1, 100)
        self.resultTable.setColumnWidth(2, 100)
        self.resultTable.setColumnWidth(3, 100)
        self.resultTable.setColumnWidth(4, 100)
        self.resultTable.setColumnWidth(5, 100)
        self.resultTable.setColumnWidth(6, 100)


        self.resultTable.setStyleSheet("""
                QTableWidget {
                    border-radius: 5px;
                    gridline-color: white;
                }
                QTableWidget::item {
                    border-bottom: 1px solid #c7e0c3; /* Light green border for items */
                    padding-left: 3px; /* Padding for text alignment */
                    background-color: #edf7ed; /* Light green background for items */
                }
                QHeaderView::section {
                    background-color: #c7e0c3; /* Light green header background */
                    padding: 0px;
                    border-left: px solid transparent; /* No border for the left side */
                    border-bottom: 1px solid #c7e0c3; /* Light green bottom border */
                    border-top: 0px solid transparent; /* No border for the top */
                    border-radius: 5px; /* Rounded corners for the header */
                    font-size: 14px;
                    font-weight: bold;
                    text-align: left;
                }
                QHeaderView {
                    background-color: #c7e0c3; /* Light green header */
                    border-radius: 5px; /* Rounded corners for the header container */
                }
                QTableWidget::item:selected {
                    background-color: #a3ccac; /* A darker green color for selection */
                }
                QTableWidget::item:hover {
                    background-color: #d1e7d3; /* A different green color for hover */
                }
            """)
            

        # Save Button for time changes
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(1210, 90, 30, 25))
        self.saveButton.setText("Save")
        self.saveButton.setStyleSheet("""
    QPushButton {
        background-color: #4caf50;  /* Material Green */
        color: white;
        border: none;
        font-size: 12px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #45A049;
    }
    QPushButton:pressed {
        background-color: #397D39;
    }
""")
        self.saveButton.clicked.connect(self.update_meal_times) 
        
        # Save Button for time changes
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(790, 90, 30, 25))
        self.saveButton.setText("Save")
        self.saveButton.setStyleSheet("""
    QPushButton {
        background-color: #4caf50;  /* Material Green */
        color: white;
        border: none;
        font-size: 12px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #45A049;
    }
    QPushButton:pressed {
        background-color: #397D39;
    }
""")
        self.saveButton.clicked.connect(self.update_meal_times)
        
        # Save Button for time changes
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(370, 90, 30, 25))
        self.saveButton.setText("Save")
        self.saveButton.setStyleSheet("""
    QPushButton {
        background-color: #4caf50;  /* Material Green */
        color: white;
        border: none;
        font-size: 12px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: #45A049;
    }
    QPushButton:pressed {
        background-color: #397D39;
    }
""")
        self.saveButton.clicked.connect(self.update_meal_times)   

        # Common stylesheet for all QTimeEdit widgets
        time_edit_stylesheet = """
            QTimeEdit {
                border: none;
                padding: 5px;
                background-color: #f7faf9;  
                color: black;
            }
            QTimeEdit:focus {
                outline: none;
                border: none;
            }
        """

        # Breakfast Start Time
        self.breakfastStartEdit = QtWidgets.QTimeEdit(Dialog)
        self.breakfastStartEdit.setGeometry(QtCore.QRect(160, 90, 100, 25))
        self.breakfastStartEdit.setTime(QtCore.QTime(6, 30))
        self.breakfastStartEdit.setStyleSheet(time_edit_stylesheet)

        # Breakfast End Time
        self.breakfastEndEdit = QtWidgets.QTimeEdit(Dialog)
        self.breakfastEndEdit.setGeometry(QtCore.QRect(260, 90, 100, 25))
        self.breakfastEndEdit.setTime(QtCore.QTime(10, 00))
        self.breakfastEndEdit.setStyleSheet(time_edit_stylesheet)

        # Lunch Start Time
        self.lunchStartEdit = QtWidgets.QTimeEdit(Dialog)
        self.lunchStartEdit.setGeometry(QtCore.QRect(580, 90, 100, 25))
        self.lunchStartEdit.setTime(QtCore.QTime(11, 45))
        self.lunchStartEdit.setStyleSheet(time_edit_stylesheet)

        # Lunch End Time
        self.lunchEndEdit = QtWidgets.QTimeEdit(Dialog)
        self.lunchEndEdit.setGeometry(QtCore.QRect(680, 90, 100, 25))
        self.lunchEndEdit.setTime(QtCore.QTime(14, 30))
        self.lunchEndEdit.setStyleSheet(time_edit_stylesheet)

        # Dinner Start Time
        self.dinnerStartEdit = QtWidgets.QTimeEdit(Dialog)
        self.dinnerStartEdit.setGeometry(QtCore.QRect(1000, 90, 100, 25))
        self.dinnerStartEdit.setTime(QtCore.QTime(20, 00))
        self.dinnerStartEdit.setStyleSheet(time_edit_stylesheet)

        # Dinner End Time
        self.dinnerEndEdit = QtWidgets.QTimeEdit(Dialog)
        self.dinnerEndEdit.setGeometry(QtCore.QRect(1100, 90, 100, 25))
        self.dinnerEndEdit.setTime(QtCore.QTime(21, 30))
        self.dinnerEndEdit.setStyleSheet(time_edit_stylesheet)

        # Make sure to call the special employee UI setup method here
        self.setupSpecialEmployeesUI(Dialog)
        self.special_employees = {}  # This dictionary will store the special employees

        # Special Employees Table Setup
        self.specialEmployeesTable = QtWidgets.QTableWidget(Dialog)
        self.specialEmployeesTable.setGeometry(QtCore.QRect(870, 520, 350, 150))  # Adjust size and position as needed
        self.specialEmployeesTable.setColumnCount(2)
        self.specialEmployeesTable.setHorizontalHeaderLabels(['EPF Number', 'Token Count'])
        self.specialEmployeesTable.setColumnWidth(0, 164)
        self.specialEmployeesTable.setColumnWidth(1, 164)
        self.specialEmployeesTable.setStyleSheet("""
                QTableWidget {
                    border-radius: 5px;
                    gridline-color: white;
                }
             
                QHeaderView::section {
                    background-color: #c7e0c3; /* Light green header background */
                    padding: 2px;
                    border-left: 0px solid transparent; /* No border for the left side */
                    border-bottom: 1px solid #c7e0c3; /* Light green bottom border */
                    border-top: 0px solid transparent; /* No border for the top */
                    border-radius: 5px; /* Rounded corners for the header */
                    font-size: 14px;
                    font-weight: bold;
                    text-align: left;
                }
                QHeaderView {
                    background-color: #c7e0c3; /* Light green header */
                    border-radius: 5px; /* Rounded corners for the header container */
                }
                
                QTableWidget::item:hover {
                    background-color: #d1e7d3; /* A different green color for hover */
                }
            """)


        # Load and display special employees
        self.load_and_display_special_employees()
        self.addButton.clicked.connect(self.emitSpecialEmployeeUpdated)
        
#         self.excelButton = QtWidgets.QPushButton("Export Today's Records", self.widget_5)
#         self.excelButton.setGeometry(QtCore.QRect(70, 600, 300, 60))  # Adjust position and size as necessary
#         self.excelButton.clicked.connect(self.export_to_excel)
#         self.excelButton.setStyleSheet("""
#     QPushButton {
#         background-color: #4CAF50; /* Green background */
#         color: white; /* White text */
#         font-size: 16px; /* Set the font-size */
#         border: none; /* No border */
#         padding: 10px 20px; /* Padding around the text */
#         border-radius: 8px; /* Rounded corners */
#     }
#     QPushButton:hover {
#         background-color: #45a049; /* Darker shade of green */
#     }
# """)

        # Date selection widget styled like a calendar
        self.dateEdit = QDateEdit(self.widget_5)
        self.dateEdit.setGeometry(QtCore.QRect(70, 530, 120, 90))
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setStyleSheet("""
            QDateEdit {
                background-color: white; /* White background for the date field */
                color: black; /* Black text color */
                border: 1px solid #4CAF50; /* Green border */
                border-radius: 8px; /* Rounded corners */
                padding: 5px; /* Padding inside the date edit */
                font-size: 14px; /* Font size */
            }
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right; /* Position the dropdown arrow to the right */
                width: 30px; /* Width of the dropdown button */
                border-left-width: 1px; /* Border width to the left of the dropdown button */
                border-left-color: darkgrey; /* Color of the border to the left of the dropdown */
                border-left-style: solid; /* Style of the border to the left of the dropdown */
                border-top-right-radius: 7px; /* Rounded top right corner */
                border-bottom-right-radius: 7px; /* Rounded bottom right corner */
            }
            QDateEdit::down-arrow {
                image: url('images/dropdowncalander.png'); /* Here you can optionally set an arrow icon */
            }
            QDateEdit QAbstractItemView {
                selection-background-color: #4CAF50; /* Color for selected date */
                background: white; /* Background color for the dropdown calendar */
                color: black; /* Text color for the dropdown calendar */
                border-radius: 8px; /* Border radius for the calendar popup */
            }
        """)

       


       


        # daily record Button setup
        self.excelButton = QtWidgets.QPushButton("Daily Records", self.widget_5)
        self.excelButton.setGeometry(QtCore.QRect(200, 530, 160, 40))
        self.excelButton.clicked.connect(self.export_to_excel)
        self.excelButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green background */
                color: white; /* White text */
                font-size: 16px; /* Set the font-size */
                border: none; /* No border */
                padding: 10px 20px; /* Padding around the text */
                border-radius: 8px; /* Rounded corners */
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker shade of green */
            }
        """)

        # Weekly record Button setup
        self.weeklyExcelButton = QtWidgets.QPushButton("Weekly Summary", self.widget_5)
        self.weeklyExcelButton.setGeometry(QtCore.QRect(200, 580, 160, 40))
        self.weeklyExcelButton.clicked.connect(self.export_weekly_to_excel)
        self.weeklyExcelButton.setStyleSheet("""
        QPushButton {
            background-color: #3E64FF; /* Blue background */
            color: white; /* White text */
            font-size: 16px; /* Set the font-size */
            border: none; /* No border */
            padding: 10px 20px; /* Padding around the text */
            border-radius: 8px; /* Rounded corners */
        }
        QPushButton:hover {
            background-color: #354BFF; /* Darker shade of blue */
        }
        """)



        # Start Date selection
        self.startDateEdit = QDateEdit(Dialog)
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setDate(QtCore.QDate.currentDate())
        self.startDateEdit.setGeometry(QtCore.QRect(50, 650, 75, 30))
        self.startDateEdit.setStyleSheet("""
            QDateEdit {
                background-color: white;  /* White background */
                color: #333;  /* Dark grey text */
                border: 1px solid #ccc;  /* Light grey border */
                border-radius: 5px;  /* Rounded corners */
                padding: 5px;  /* Padding inside the date edit */
                font-size: 14px;  /* Font size */
            }
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;  /* Position the dropdown arrow to the right */
                width: 32px;  /* Width of the dropdown button */
                border-left-width: 1px;  /* Border width to the left of the dropdown button */
                border-left-color: #ccc;  /* Color of the border to the left of the dropdown */
                border-left-style: solid;  /* Style of the border to the left of the dropdown */
                border-top-right-radius: 4px;  /* Rounded top right corner */
                border-bottom-right-radius: 4px;  /* Rounded bottom right corner */
            }
            QDateEdit::down-arrow {
                image: url('images/dropdowncalander.png');  /* Use your path to the calendar icon image */
            }
        """)

        # End Date selection
        self.endDateEdit = QDateEdit(Dialog)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDate(QtCore.QDate.currentDate())
        self.endDateEdit.setGeometry(QtCore.QRect(140, 650, 75, 30))
        self.endDateEdit.setStyleSheet("""
            QDateEdit {
                background-color: white;  /* White background */
                color: #333;  /* Dark grey text */
                border: 1px solid #ccc;  /* Light grey border */
                border-radius: 5px;  /* Rounded corners */
                padding: 5px;  /* Padding inside the date edit */
                font-size: 14px;  /* Font size */
            }
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;  /* Position the dropdown arrow to the right */
                width: 32px;  /* Width of the dropdown button */
                border-left-width: 1px;  /* Border width to the left of the dropdown button */
                border-left-color: #ccc;  /* Color of the border to the left of the dropdown */
                border-left-style: solid;  /* Style of the border to the left of the dropdown */
                border-top-right-radius: 4px;  /* Rounded top right corner */
                border-bottom-right-radius: 4px;  /* Rounded bottom right corner */
            }
            QDateEdit::down-arrow {
                image: url('images/dropdowncalander.png');  /* Use your path to the calendar icon image */
            }
        """)

        # Button to trigger report generation
        self.generateReportButton = QPushButton("Generate Report", Dialog)
        self.generateReportButton.setGeometry(QtCore.QRect(240, 645, 130, 40))
        self.generateReportButton.clicked.connect(self.export_date_range_to_excel)
        self.generateReportButton.setStyleSheet("""
            QPushButton {
                background-color: #6c2bb3;  /* Green background */
                color: white;  /* White text */
                font-size: 14px;  /* Font size */
                border: none;  /* No border */
                padding: 6px 12px;  /* Padding around the text */
                border-radius: 5px;  /* Rounded corners */
            }
            QPushButton:hover {
                background-color: #6919bf;  /* Darker shade of green */
            }
        """)




        # Dynamic Button Setup
        self.dynamicButton = QtWidgets.QPushButton("Deactivated", self.widget_5)
        self.dynamicButton.setGeometry(QtCore.QRect(1130, 10, 120, 60))
        self.dynamicButton.setStyleSheet("""
            QPushButton {
                background-color: red; 
                color: white; 
                font-size: 16px; 
                font-weight: bold; 
                border-radius: 15px; 
                border: 1px solid white;
            }
        """)
        self.dynamicButton.clicked.connect(self.on_dynamicButtonClick)
        self.dynamicButton.clicked.connect(self.update_meal_times) 


    import os
    import pandas as pd
    import mysql.connector
    from datetime import datetime

    def export_date_range_to_excel(self):
        start_date = self.startDateEdit.date().toPyDate()
        end_date = self.endDateEdit.date().toPyDate()

        connection = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='jbcanteen'
        )

        # Query to select records by date and meal type
        daily_query = """
        SELECT DATE(print_time) as Date, DAYNAME(print_time) as Day, meal_type, COUNT(*) as Total
        FROM printed_records
        WHERE print_time BETWEEN %s AND %s
        GROUP BY DATE(print_time), DAYNAME(print_time), meal_type
        ORDER BY DATE(print_time), meal_type
        """
        df_daily = pd.read_sql(daily_query, connection, params=[start_date, end_date])

        # Query to select records by department and meal type
        dept_query = """
        SELECT department, meal_type, COUNT(*) as Total_Meals
        FROM printed_records
        WHERE print_time BETWEEN %s AND %s
        GROUP BY department, meal_type
        ORDER BY department, meal_type
        """
        df_dept = pd.read_sql(dept_query, connection, params=[start_date, end_date])

        # Processing summaries
        summary_df = df_daily.pivot_table(index=['Date', 'Day'], columns='meal_type', values='Total', fill_value=0)
        summary_df['Total'] = summary_df.sum(axis=1)

        # Define prices for meals
        prices = {'BREAKFAST': 125.00, 'LUNCH': 175.00, 'DINNER': 175.00}
        for meal, price in prices.items():
            summary_df[f'{meal} Cost'] = summary_df.get(meal, 0) * price
        summary_df['Total Cost'] = summary_df[[f'{meal} Cost' for meal in prices]].sum(axis=1)

        totals = summary_df.sum().rename(('Total', ''))
        summary_df = pd.concat([summary_df, pd.DataFrame([totals], index=[('Total', '')])])

        dept_summary_df = df_dept.pivot_table(index='department', columns='meal_type', values='Total_Meals', fill_value=0)
        dept_summary_df['Total'] = dept_summary_df.sum(axis=1)

        # Output directory and file path
        download_directory = "C:/Canteen_Meal_Token_Reports"
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
        file_path = os.path.join(download_directory, f"DateRange_MealRecords_{start_date}_to_{end_date}.xlsx")

        # Writing to Excel
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            summary_df.to_excel(writer, sheet_name='Summary', index=True)
            dept_summary_df.to_excel(writer, sheet_name='Department Summary', index=True)

        os.startfile(file_path)
        connection.close()
        print("Report generated for the selected date range:", file_path)
    


    # def export_to_excel(self):
    #     import os
    #     import pandas as pd
    #     import mysql.connector

    #     # Get the selected date from the dateEdit widget
    #     selected_date = self.dateEdit.date().toString('yyyy-MM-dd')

    #     # Connect to the database
    #     connection = mysql.connector.connect(
    #         user='root', password='', host='127.0.0.1', database='jbcanteen', raise_on_warnings=True
    #     )

    #     # SQL query to select records
    #     query = "SELECT * FROM printed_records WHERE DATE(print_time) = %s"
        
    #     # Execute query
    #     df = pd.read_sql(query, connection, params=[selected_date])

    #     # Calculate meal counts
    #     meal_counts = df['meal_type'].value_counts()

    #     # Create summary rows for each meal type
    #     summary_rows = [
    #         {'meal_type': 'BREAKFAST', 'Count': meal_counts.get('BREAKFAST', 0)},
    #         {'meal_type': 'LUNCH', 'Count': meal_counts.get('LUNCH', 0)},
    #         {'meal_type': 'DINNER', 'Count': meal_counts.get('DINNER', 0)}
    #     ]

    #     # Convert summary data to DataFrame          
    #     summary_df = pd.DataFrame(summary_rows)

    #     # # Group by department and meal type, then explode names to separate rows
    #     # df['emp_name'] = df['emp_name'].apply(lambda x: x.split(', '))
    #     # department_details = df.explode('emp_name').groupby(['department', 'meal_type', 'emp_name']).size().reset_index(name='Total_Meals')

    #     # Assume df['emp_name'] already contains names that might be grouped together, and df['emp_code'] contains corresponding codes
    #     df['emp_name'] = df['emp_name'].str.split(', ')
    #     df['emp_code'] = df['emp_code'].str.split(', ')
    #     df = df.explode(['emp_name', 'emp_code'])

    #     # Group by department, meal_type, emp_name, and emp_code, then count occurrences
    #     department_details = df.groupby(['department', 'meal_type', 'emp_name', 'emp_code']).size().reset_index(name='Total_Meals')


    #     # Pivot table for department-wise summary
    #     department_wise_summary = department_details.pivot_table(index='department', columns='meal_type', values='Total_Meals', aggfunc='sum').fillna(0)
    #     department_wise_summary['Total'] = department_wise_summary.sum(axis=1)
    #     department_wise_summary = department_wise_summary[['BREAKFAST', 'LUNCH', 'DINNER', 'Total']]

    #     # Specify the directory and file path
    #     download_directory = "C:/Canteen_Meal_Token_Reports"
    #     if not os.path.exists(download_directory):
    #         os.makedirs(download_directory)
    #     file_path = os.path.join(download_directory, f"Canteen_MealRecords_{selected_date}.xlsx")

    #     # Write to an Excel file and open it
    #     with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    #         df.to_excel(writer, sheet_name='Records', index=False)
    #         summary_df.to_excel(writer, sheet_name='Meal Totals', index=False)
    #         department_details.to_excel(writer, sheet_name='Department Details', index=False)
    #         department_wise_summary.to_excel(writer, sheet_name='Department Summary', index=True)  # New tab for department summary

    #     os.startfile(file_path)

    #     print("Excel file has been created and saved to:", file_path)

    def export_to_excel(self):
        import os
        import pandas as pd
        import mysql.connector

        # Get the selected date from the dateEdit widget
        selected_date = self.dateEdit.date().toString('yyyy-MM-dd')

        # Connect to the database
        connection = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='jbcanteen', raise_on_warnings=True
        )

        # SQL query to select records
        query = "SELECT * FROM printed_records WHERE DATE(print_time) = %s"
        
        # Execute query
        df = pd.read_sql(query, connection, params=[selected_date])

        # Calculate meal counts
        meal_types = ['BREAKFAST', 'LUNCH', 'DINNER']
        meal_counts = df['meal_type'].value_counts().reindex(meal_types, fill_value=0)

        # Create summary rows for each meal type
        summary_rows = [{'meal_type': meal, 'Count': meal_counts[meal]} for meal in meal_types]
        summary_df = pd.DataFrame(summary_rows)

        # Assuming df['emp_name'] already contains names that might be grouped together, and df['emp_code'] contains corresponding codes
        if not df.empty:
            df['emp_name'] = df['emp_name'].str.split(', ')
            df['emp_code'] = df['emp_code'].str.split(', ')
            df = df.explode(['emp_name', 'emp_code'])

            # Group by department, meal_type, emp_name, and emp_code, then count occurrences
            department_details = df.groupby(['department', 'meal_type', 'emp_name', 'emp_code']).size().reset_index(name='Total_Meals')
        else:
            # Handle case where no records are found
            department_details = pd.DataFrame(columns=['department', 'meal_type', 'emp_name', 'emp_code', 'Total_Meals'])

        # Pivot table for department-wise summary
        department_wise_summary = department_details.pivot_table(index='department', columns='meal_type', values='Total_Meals', aggfunc='sum').fillna(0)
        department_wise_summary['Total'] = department_wise_summary.sum(axis=1)

        # Specify the directory and file path
        download_directory = "C:/Canteen_Meal_Token_Reports"
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
        file_path = os.path.join(download_directory, f"Canteen_MealRecords_{selected_date}.xlsx")

        # Write to an Excel file and open it
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Records', index=False)
            summary_df.to_excel(writer, sheet_name='Meal Totals', index=False)
            department_details.to_excel(writer, sheet_name='Department Details', index=False)
            department_wise_summary.to_excel(writer, sheet_name='Department Summary', index=True)  # New tab for department summary

        os.startfile(file_path)
        connection.close()
        print("Excel file has been created and saved to:", file_path)







    import os
    import pandas as pd
    import mysql.connector
    from datetime import timedelta

    def export_weekly_to_excel(self):
        selected_date = self.dateEdit.date().toPyDate()
        start_of_week = selected_date - timedelta(days=selected_date.weekday())
        end_of_week = start_of_week + timedelta(days=7)

        connection = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='jbcanteen'
        )

        # Query to select records by date and meal type
        daily_query = """
        SELECT DATE(print_time) as Date, DAYNAME(print_time) as Day, meal_type, COUNT(*) as Total
        FROM printed_records
        WHERE print_time BETWEEN %s AND %s
        GROUP BY DATE(print_time), DAYNAME(print_time), meal_type
        ORDER BY DATE(print_time), meal_type
        """
        df_daily = pd.read_sql(daily_query, connection, params=[start_of_week, end_of_week])

        # Query to select records by department and meal type
        dept_query = """
        SELECT department, meal_type, COUNT(*) as Total_Meals
        FROM printed_records
        WHERE print_time BETWEEN %s AND %s
        GROUP BY department, meal_type
        ORDER BY department, meal_type
        """
        df_dept = pd.read_sql(dept_query, connection, params=[start_of_week, end_of_week])

        # Processing daily summary
        summary_df = df_daily.pivot_table(index=['Date', 'Day'], columns='meal_type', values='Total', fill_value=0)
        summary_df['Total'] = summary_df.sum(axis=1)

        prices = {'BREAKFAST': 125.00, 'LUNCH': 175.00, 'DINNER': 175.00}
        for meal, price in prices.items():
            summary_df[f'{meal} Cost'] = summary_df.get(meal, 0) * price
        summary_df['Total Cost'] = summary_df[[f'{meal} Cost' for meal in prices]].sum(axis=1)

        # Adding totals row
        totals = summary_df.sum().rename(('Total', ''))
        summary_df = pd.concat([summary_df, pd.DataFrame([totals], index=[('Total', '')])])

        # Processing department summary
        dept_summary_df = df_dept.pivot_table(index='department', columns='meal_type', values='Total_Meals', fill_value=0)
        dept_summary_df['Total'] = dept_summary_df.sum(axis=1)

        # Specify the directory and file path
        download_directory = "C:/Canteen_Meal_Token_Reports"
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
        file_path = os.path.join(download_directory, f"Weekly_MealRecords_{start_of_week}_to_{end_of_week}.xlsx")

        # Writing to Excel
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            summary_df.to_excel(writer, sheet_name='Weekly Summary', index=True)
            dept_summary_df.to_excel(writer, sheet_name='Department Summary', index=True)

        os.startfile(file_path)
        connection.close()
        print("Weekly report generated:", file_path)






    def on_dynamicButtonClick(self):
        # Change the button's color, text, and style upon click
        self.dynamicButton.setStyleSheet("""
            QPushButton {
                background-color: blue; 
                color: white; 
                font-size: 16px; 
                font-weight: bold; 
                border-radius: 15px; 
                border: 1px solid white;
            }
        """)
        self.dynamicButton.setText("Activated")

    def load_and_display_special_employees(self):
        self.specialEmployeesTable.setRowCount(0)  # Clear existing rows
        try:
            with open("special_employees.json", "r") as file:
                special_employees = json.load(file)
                for row_number, (emp_code, token_count) in enumerate(special_employees.items()):
                    self.specialEmployeesTable.insertRow(row_number)
                    self.specialEmployeesTable.setItem(row_number, 0, QtWidgets.QTableWidgetItem(emp_code))
                    self.specialEmployeesTable.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(token_count)))
        except FileNotFoundError:
            print("Special employees file not found.")

    def update_meal_times(self):
        updated_times = {
            'breakfast_start': self.breakfastStartEdit.time().toPyTime(),
            'breakfast_end': self.breakfastEndEdit.time().toPyTime(),
            'lunch_start': self.lunchStartEdit.time().toPyTime(),
            'lunch_end': self.lunchEndEdit.time().toPyTime(),
            'dinner_start': self.dinnerStartEdit.time().toPyTime(),
            'dinner_end': self.dinnerEndEdit.time().toPyTime()
        }
        self.mealTimesUpdated.emit(updated_times)
        
    def applyShadow(self, widget):
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        widget.setGraphicsEffect(shadow)

    def applyShadowAll(self, widget):
        """
        Applies a balanced drop shadow effect to the given widget.
        """
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)  # Adjust the blur radius as needed for a softer shadow
        shadow.setXOffset(0)  # No horizontal offset
        shadow.setYOffset(0)  # No vertical offset
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))  # Shadow color with some transparency
        widget.setGraphicsEffect(shadow)

    def applyShadowBig(self, widget):
        """
        Applies a balanced drop shadow effect to the given widget.
        """
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)  # Adjust the blur radius as needed for a softer shadow
        shadow.setXOffset(0)  # No horizontal offset
        shadow.setYOffset(0)  # No vertical 
        shadow.setColor(QtGui.QColor(0, 0, 0, 100))  # Shadow color with some transparency
        widget.setGraphicsEffect(shadow)

    def setupSpecialEmployeesUI(self, Dialog):
        # Special employees management setup
        self.specialEmployeeGroup = QtWidgets.QGroupBox(Dialog)
        self.specialEmployeeGroup.setGeometry(QtCore.QRect(875, 260, 350, 260))

        layout = QtWidgets.QVBoxLayout()

        self.empCodeLabel = QtWidgets.QLabel("Contract Employee Code:")
        self.empCodeInput = QtWidgets.QLineEdit()
        self.tokenCountLabel = QtWidgets.QLabel("Number of Tokens:")
        self.tokenCountInput = QtWidgets.QSpinBox()
        self.tokenCountInput.setMinimum(1)
        self.tokenCountInput.setMaximum(100)
        self.addButton = QtWidgets.QPushButton("Add/Update Employee")
        self.clearButton = QtWidgets.QPushButton("Clear All Employees", Dialog)
        # Group Box style
        self.specialEmployeeGroup.setStyleSheet("""
            QGroupBox {
                font-size: 12px;
                color: #2c3e50; /* Dark blue-grey text */
                border: 0px solid #a3ccac; /* Soft green border */
                border-radius: 10px;
                margin-top: 10px; /* Space at the top inside the border */
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center; /* position at the top center */
                padding: 0 10px;
                background-color: #edf7ed; /* Light green background */
            }
        """)

        # Labels style
        label_stylesheet = """
            QLabel {
                color: #2c3e50; /* Dark blue-grey text */
                font-size: 16px;
                padding: 5px;
            }
        """

        self.empCodeLabel.setStyleSheet(label_stylesheet)
        self.tokenCountLabel.setStyleSheet(label_stylesheet)

        # Line Edit style
        self.empCodeInput.setStyleSheet("""
            QLineEdit {
                border: 1px solid #a3ccac; /* Soft green border */
                border-radius: 5px;
                padding: 10px; /* Increased padding for more height */
                font-size: 14px; /* Slightly larger text */
                background-color: white;
            }
            QLineEdit:focus {
                border: 1px solid #88a097; /* Darker green border for focus */
            }
        """)

        # Spin Box style
        self.tokenCountInput.setStyleSheet("""
            QSpinBox {
                padding: 5px;
                border: 1px solid #a3ccac; /* Soft green border */
                border-radius: 5px;
                font-size: 14px;
            }
            """)

        # Adjusted Buttons style with increased height
        button_stylesheet = """
            QPushButton {
                color: white;   
                background-color: #bd7644; /* Material Design Green */
                border-radius: 5px;
                padding: 35px 10px; /* Increased vertical padding for more height */
                font-size: 12px; /* Slightly larger text */
                border: none;
                margin: 5px; /* Optional: adds space between buttons and other elements */
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QPushButton:pressed {
                background-color: #397D39;
            }
        """

        self.addButton.setStyleSheet(button_stylesheet)
        self.clearButton.setStyleSheet(button_stylesheet)

        layout.addWidget(self.empCodeLabel)
        layout.addWidget(self.empCodeInput)
        layout.addWidget(self.tokenCountLabel)
        layout.addWidget(self.tokenCountInput)
        layout.addWidget(self.addButton)
        layout.addWidget(self.clearButton)

        self.specialEmployeeGroup.setLayout(layout)

        self.addButton.clicked.connect(self.emitSpecialEmployeeUpdated)

    def emitSpecialEmployeeUpdated(self):
        emp_code = self.empCodeInput.text().strip()
        token_count = self.tokenCountInput.value()
        if emp_code:
            self.specialEmployeeUpdated.emit(emp_code, token_count)  # Emit the signal
            self.empCodeInput.clear()

        ###############################

class MyDialog(QtWidgets.QDialog):
    def __init__(self,):
        super(MyDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db_connection = self.connect_to_database()
        self.second_db_connection = self.connect_to_second_database()
        self.meal_tokens_issued = {'BREAKFAST': set(), 'LUNCH': set(), 'DINNER': set()}
        self.last_record_id = None
        self.truncate_table_if_needed()
        self.first_run = True  # Initialize to True to prevent initial actions
        self.last_meal_type = None  # Added to track the last meal type
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.retrieve_and_display)
        self.timer.start(2000)
        self.reset_timer = QtCore.QTimer(self)
        self.reset_timer.timeout.connect(self.reset_availability)
        self.set_reset_timer()
        self.ui.printButton.clicked.connect(self.manual_print)
        self.ui.checkButton.clicked.connect(self.check_and_display_record)
        self.update_meal_counts()        # Call this method whenever you need to refresh the dashboard, e.g., after printing
        self.printer_name = win32print.GetDefaultPrinter()
        # Default meal times initialized directly in the dialog
        self.meal_times = {}
        
        # Connect the signal to the slot
        self.ui.mealTimesUpdated.connect(self.update_meal_times)   
        self.ui.update_meal_times()
        
        # Initialize special_employees here, not in Ui_Dialog
        self.special_employees = {}
        self.load_special_employees()

        self.ui.specialEmployeeUpdated.connect(self.addOrUpdateSpecialEmployee)         # Connect the signal to a method
        self.ui.clearButton.clicked.connect(self.clearSpecialEmployees)

        # Optionally, initialize these variables
        self.breakfast_start = None
        self.breakfast_end = None
        self.lunch_start = None
        self.lunch_end = None
        self.dinner_start = None
        self.dinner_end = None


    import mysql.connector
    from mysql.connector import Error

    def truncate_table_if_needed(self):
        try:
            connection = mysql.connector.connect(
                host='localhost', user='root', password='', database='zkbiotime')
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM iclock_transaction")
            (record_count,) = cursor.fetchone()
            if record_count >= 20:
                cursor.execute("TRUNCATE TABLE iclock_transaction")
                connection.commit()
                print("Table truncated successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    def addOrUpdateSpecialEmployee(self, emp_code, token_count):
        # Create a password input dialog
        password, ok = QtWidgets.QInputDialog.getText(self, 'Password Confirmation',
                                                    'Enter Admin password to update the employee:',
                                                    QtWidgets.QLineEdit.Password)

        # Define the correct password
        correct_password = "JBR@7221"

        # Check if the OK button was clicked and the correct password was entered
        if ok and password == correct_password:
            # Update the special employee data if the password is correct
            self.special_employees[emp_code] = token_count
            self.save_special_employees()
            QtWidgets.QMessageBox.information(self, 'Updated',
                                            f'Special employee {emp_code} updated with {token_count} tokens.')
            self.refreshSpecialEmployeesTable()  # Refresh the table after update
        else:
            # Show an error message if the password is incorrect
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect password!')

       
    def save_special_employees(self):
        # Save the special_employees dict to a JSON file
        try:
            with open("special_employees.json", "w") as file:
                json.dump(self.special_employees, file)
        except Exception as e:
            print(f"Error saving special employees: {e}")

    def load_special_employees(self):
        # Load special employees from the JSON file
        try:
            with open("special_employees.json", "r") as file:
                self.special_employees = json.load(file)
        except FileNotFoundError:
            self.special_employees = {}


    def clearSpecialEmployees(self):
        # Create a password input dialog
        password, ok = QtWidgets.QInputDialog.getText(self, 'Password Confirmation',
                                                    'Enter Admin password to clear all employee settings:',
                                                    QtWidgets.QLineEdit.Password)

        # Define the correct password
        correct_password = "JBR@7221"

        # Check if the OK button was clicked and the correct password was entered
        if ok and password == correct_password:
            # Ask for confirmation to clear all data if the password is correct
            reply = QtWidgets.QMessageBox.question(
                self,
                'Clear All',
                'Are you sure you want to clear all special employee settings?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No
            )

            if reply == QtWidgets.QMessageBox.Yes:
                self.special_employees.clear()  # Clear the dictionary
                self.save_special_employees()  # Save the now-empty dictionary to JSON
                QtWidgets.QMessageBox.information(self, 'Cleared', 'All special employee settings have been cleared.')
                self.refreshSpecialEmployeesTable()  # Refresh the table after update
        else:
            # Show an error message if the password is incorrect
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect password!')


    def save_special_employees(self):
        try:
            with open("special_employees.json", "w") as file:
                json.dump(self.special_employees, file)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Failed to save changes: ' + str(e))


    def refreshSpecialEmployeesTable(self):
        self.ui.specialEmployeesTable.setRowCount(0)  # Clear the existing rows
        for row_number, (emp_code, token_count) in enumerate(self.special_employees.items()):
            self.ui.specialEmployeesTable.insertRow(row_number)
            self.ui.specialEmployeesTable.setItem(row_number, 0, QtWidgets.QTableWidgetItem(emp_code))
            self.ui.specialEmployeesTable.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(token_count)))


    def update_meal_times(self, times):
        # Update internal state with the new times
        self.breakfast_start = times['breakfast_start']
        self.breakfast_end = times['breakfast_end']
        self.lunch_start = times['lunch_start']
        self.lunch_end = times['lunch_end']
        self.dinner_start = times['dinner_start']
        self.dinner_end = times['dinner_end']
        print("Internal meal times updated!")
        
    def determine_meal(self, current_time):
        if (self.breakfast_start is not None and
            self.breakfast_end is not None and
            self.lunch_start is not None and
            self.lunch_end is not None and
            self.dinner_start is not None and
            self.dinner_end is not None):
            
            if self.breakfast_start <= current_time <= self.breakfast_end:
                return "BREAKFAST"
            elif self.lunch_start <= current_time <= self.lunch_end:
                return "LUNCH"
            elif self.dinner_start <= current_time <= self.dinner_end:
                return "DINNER"
        return "OUT OF MEAL TIME"

    def connect_to_database(self):
        config = {
            'user': 'root',
            'password': '',
            'host': '127.0.0.1',
            'database': 'zkbiotime',
            'raise_on_warnings': True
        }
        try:
            connection = mysql.connector.connect(**config)
            print("Database connection established.")
            return connection
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            return None

    def connect_to_second_database(self):
        config = {
            'user': 'root',
            'password': '',
            'host': '127.0.0.1',
            'database': 'jbcanteen',
            'raise_on_warnings': True
        }
        try:
            connection = mysql.connector.connect(**config)
            print("Second database connection established.")
            return connection
        except mysql.connector.Error as err:
            print(f"Error connecting to second MySQL database: {err}")
            return None


    def store_printed_record(self, record):
        if self.second_db_connection is None:
            print("Second database connection is not established.")
            return

        # Define the SQL insert query with an additional column for the department name
        insert_query = ("INSERT INTO printed_records "
                        "(token_no, emp_name, emp_code, meal_type, department, print_time, created_at) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        
        # Add the prefix 'T-' to the record['id']
        token_no = f"T-{record['id']}"

        values = (
            token_no,
            f"{record['first_name']}",
            record['emp_code'],
            self.determine_meal(datetime.now().time()),
            record['department'],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        # Insert record into the second database
        cursor = self.second_db_connection.cursor()
        cursor.execute(insert_query, values)
        self.second_db_connection.commit()
        self.update_meal_counts()  # Update meal counts right after inserting
        cursor.close()

        print("Record stored in the second database.")



    def get_jwt_token(self):
        url = "http://127.0.0.1:8081/jwt-api-token-auth/"
        headers = {'Content-Type': 'application/json'}
        body = {"username": "addpacks", "password": "JBR@7221"}
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            return response.json().get('token')
        else:
            print("Failed to fetch token:", response.text)
            return None


    def retrieve_and_display(self):
        current_time = datetime.now().time()
        meal_type = self.determine_meal(current_time)

        if meal_type == "OUT OF MEAL TIME":
            if self.first_run:
                self.first_run = False  # To prevent initialization actions
            return

        # Fetch the token
        token = self.get_jwt_token()
        if not token:
            print("No token available. Cannot fetch employee data.")
            return

        url = 'http://127.0.0.1:8081/iclock/api/transactions/'
        headers = {
                'Content-Type': 'application/json', 'Authorization': f'JWT {token}'
            }
        params = {'page_size': 50}  # Assuming we fetch a large number of entries; adjust accordingly

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data['data']:
                # Sort the records by ID in descending order to get the latest record at index 0
                latest_record = sorted(data['data'], key=lambda x: x['id'], reverse=True)[0]
                emp_code = latest_record['emp_code']

                # Print the details of the latest record
                # print(f"Latest Record: {latest_record}")

                if self.first_run:
                    self.last_record_id = latest_record['id']
                    self.first_run = False
                    return

                if meal_type != self.last_meal_type:
                    self.last_meal_type = meal_type
                    self.meal_tokens_issued[meal_type] = {}  # Reset or initialize as dictionary for the new meal type
                    self.last_record_id = latest_record['id']
                    return

                if latest_record['id'] != self.last_record_id:
                    # Check if employee is in special employees list
                    if emp_code in self.special_employees:
                        token_count = self.special_employees[emp_code]
                        issued_count = self.meal_tokens_issued[meal_type].get(emp_code, 0)
                        additional_tokens = token_count - issued_count
                        if additional_tokens > 0:
                            for _ in range(additional_tokens):
                                self.print_employee_record(latest_record, meal_type)
                            self.meal_tokens_issued[meal_type][emp_code] = issued_count + additional_tokens
                    else:
                        if emp_code not in self.meal_tokens_issued[meal_type]:
                            self.meal_tokens_issued[meal_type][emp_code] = 1
                            self.print_employee_record(latest_record, meal_type)

                    self.last_record_id = latest_record['id']

        except requests.exceptions.RequestException as e:
            print(f"Error retrieving latest record: {e}")


    def print_employee_record(self, record, meal_type):
        self.truncate_table_if_needed()
        token_no = record['id']
        current_datetime = datetime.now().strftime("%d/%m/%Y TIME: %I:%M:%S %p")
        record_text = self.format_bill_text_auto(record, current_datetime, meal_type, token_no)
        record_text = self.format_receipt_text(record, meal_type, token_no, current_datetime)
        self.store_printed_record(record)
        # Replace the existing text with the new record
        self.ui.recentPrintsText.setText(record_text)  # Set new record in the QTextEdit


    def format_receipt_text(self, record, meal_type, token_no, current_datetime):
        formatted_text = (
            "..................................\n"
            f"{meal_type} Token Receipt\n\n"
            f"DATE: {current_datetime}\n"
            f"TOKEN NO: {token_no}\n\n"
            f"EPF NO: {record['emp_code']}\n"
            f"NAME: {record['first_name']}\n"
            f"DEPARTMENT: {record['department']}\n"
            "..................................\n"
            "JB Rubber Exports\n"
            "Canteen Token System\n"
        )
        return formatted_text

    def load_special_employees(self):
        try:
            with open("special_employees.json", "r") as file:
                self.special_employees = json.load(file)
        except FileNotFoundError:
            self.special_employees = {}

    def format_bill_text_auto(self, record, current_datetime, meal_type, token_no):
        # Assuming current_datetime is passed correctly, it's used directly in text
        # Load the image
        file_name = r"images\og.jpg"
        image = Image.open(file_name)
        if image.mode != "1":  
            image = image.convert("1")  

            # Determine price based on meal type
            prices = {"BREAKFAST": "Rs.125.00", "LUNCH": "Rs.175.00", "DINNER": "Rs.175.00"}
            price = prices.get(meal_type, "Rs.0.00")

        # Lines of text to print
            text_lines = [
                    "--------------------------------------------------------------------------",
                    f"{meal_type} Token Receipt",  # This will be centered and bolded
                    "",
                    f"DATE: {current_datetime}",
                    f"TOKEN NO: {token_no}",
                    "",
                    f"EPF NO: {record['emp_code']}",
                    f"NAME: {record['first_name']}",
                    f"DEPARTMENT: {record['department']}"
                    "",
                    f"PRICE: {price}\n",

                    "--------------------------------------------------------------------------",
                    "JB Rubber Exports",
                    "Canteen Token System"
                ]
            
            
            # Printer setup
            printer_name = win32print.GetDefaultPrinter()
            hprinter = win32print.OpenPrinter(printer_name)
            printjob = win32print.StartDocPrinter(hprinter, 1, ("token and logo print job", None, "RAW"))
            win32print.StartPagePrinter(hprinter)

            # Create a device context
            dc = win32ui.CreateDC()
            dc.CreatePrinterDC(printer_name)
            dc.StartDoc("My Print Job")
            dc.StartPage()

            # Define fonts
            standard_font = win32ui.CreateFont({
                "name": "Arial",
                "height": 30,
                "weight": win32con.FW_NORMAL,
            })
            bold_font = win32ui.CreateFont({
                "name": "Arial",
                "height": 30,
                "weight": win32con.FW_BOLD,
            })
            receipt_font = win32ui.CreateFont({  # For receipt title, which is bold and centered
                "name": "Arial",
                "height": 38,
                "weight": win32con.FW_BOLD,
            })
            company_font = win32ui.CreateFont({
                "name": "Arial",
                "height": 30,  # Larger font for the company name
                "weight": win32con.FW_BOLD,
            })
            price_font = win32ui.CreateFont({
                "name": "Arial",
                "height": 36, 
                "weight": win32con.FW_BOLD,
                })  # Larger font for the price


            try:
                # Print the image
                dib = ImageWin.Dib(image)
                dib.draw(dc.GetHandleOutput(), (0, 0, image.width, image.height))

                # Starting position for text
                y_position = image.height + 20

                # Print each line with specific formatting
                for line in text_lines:
                    if line == f"{meal_type} Token Receipt":
                        dc.SelectObject(receipt_font)
                        text_width, text_height = dc.GetTextExtent(line)
                        dc.TextOut((image.width - text_width) // 2, y_position, line)
                    elif "PRICE:" in line:
                        dc.SelectObject(price_font)
                        dc.TextOut(10, y_position, line)
                    elif "JB Rubber Exports" in line or "Canteen Token System" in line:
                        dc.SelectObject(company_font)
                        text_width, text_height = dc.GetTextExtent(line)
                        dc.TextOut((image.width - text_width) // 2, y_position, line)
                    elif line.startswith('-'):  # Use bold font for lines with dashes
                        dc.SelectObject(bold_font)
                        dc.TextOut(10, y_position, line)
                    else:
                        dc.SelectObject(standard_font)
                        dc.TextOut(10, y_position, line)
                    y_position += 30  # Adjust line spacing based on the largest font height
                    
                dc.EndPage()
                dc.EndDoc()

            finally:
                dc.DeleteDC()
                win32print.EndPagePrinter(hprinter)
                win32print.EndDocPrinter(hprinter)
                win32print.ClosePrinter(hprinter)

            
    def format_bill_text(self, latest_record, current_datetime, meal_type):
        return (
            "------------------------------\n"
            f"DATE: {current_datetime}\n"
            f"MEAL TOKEN - {meal_type}\n"
            
            f"TOKEN NO: {latest_record['id']}\n"
            "------------------------------\n"
            f"EPF NO: {latest_record['emp_code']}\n"
            f"NAME: {latest_record['first_name']}\n"
            f"DEPARTMENT: {latest_record['department']}\n"

            "------------------------------\n"
                "JB Rubber Exports\n"
               "Canteen Token System\n"
        )
    
        
    def set_reset_timer(self):
        now = datetime.now()
        midnight = datetime(now.year, now.month, now.day, 23, 59, 59)
        if now >= midnight:
            midnight += timedelta(days=1)
        self.reset_timer.start((midnight - now).seconds * 1000)


    def reset_availability(self):
        self.meal_tokens_issued = {'BREAKFAST': set(), 'LUNCH': set(), 'DINNER': set()}
        self.set_reset_timer()
        

        # manual print functions

    def manual_print(self):
        emp_code = self.ui.lineEdit.text().strip()
        if emp_code:
            self.print_record_by_emp_code(emp_code)
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Please enter an EPF Number.')


    def print_record_by_emp_code(self, emp_code):
        if not self.db_connection:
            print("First database connection is not established.")
            return

        if not hasattr(self, 'second_db_connection'):
            self.second_db_connection = self.connect_to_second_database()

        if not self.second_db_connection:
            print("Second database connection is not established.")
            return

        cursor = self.db_connection.cursor(dictionary=True)
        try:
            # Fetch employee and department data
            cursor.execute("""
                SELECT pe.*, d.dept_name
                FROM personnel_employee pe
                LEFT JOIN personnel_department d ON pe.department_id = d.id
                WHERE pe.emp_code = %s
            """, (emp_code,))
            record = cursor.fetchone()

            if record:
                next_token_no = str(self.last_record_id) + "-Duplicate" if self.last_record_id else "1Duplicate"
                meal_type = self.determine_meal(datetime.now().time())
                record_text = self.format_bill_text_manual(record, meal_type, next_token_no)

                # Insert into the second database with department name
                insert_query = ("INSERT INTO printed_records "
                                "(token_no, emp_name, emp_code, meal_type, department, print_time, created_at) "
                                "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                values = (
                    next_token_no,
                    record['first_name'],
                    record['emp_code'],
                    meal_type,
                    record.get('dept_name', 'No Department Assigned'),  # Include department name
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                second_cursor = self.second_db_connection.cursor()
                second_cursor.execute(insert_query, values)
                self.second_db_connection.commit()
                second_cursor.close()

                self.update_meal_counts()  # Optionally update meal counts

            else:
                print("No record found for employee code:", emp_code)
        except Exception as e:
            print(f"Error fetching employee record or inserting into second database: {e}")
        finally:
            cursor.close()


    def close_connections(self):
        if self.db_connection is not None:
            self.db_connection.close()
        if hasattr(self, 'second_db_connection') and self.second_db_connection is not None:
            self.second_db_connection.close()


    def format_bill_text_manual(self, record, meal_type, next_token_no):
        current_datetime = datetime.now().strftime("%d/%m/%Y TIME: %I:%M:%S %p")
        # Handling potential absence of department name
        department_name = record.get('dept_name', 'No Department Assigned')

        # Price setup
        prices = {"BREAKFAST": "Rs.125.00", "LUNCH": "Rs.175.00", "DINNER": "Rs.175.00"}
        price = prices.get(meal_type, "Rs.0.00")

        # Load the image for printing
        file_name = r"images\og.jpg"
        image = Image.open(file_name).convert("1")

        # Text lines to print, now includes department name
        text_lines = [
            "--------------------------------------------------------------------------",
            f"{meal_type} Token Receipt",
            "",
            f"DATE: {current_datetime}",
            f"TOKEN NO: {next_token_no}",
            "",
            f"EPF NO: {record['emp_code']}",
            f"NAME: {record.get('first_name', 'Unknown')}",
            f"DEPARTMENT: {department_name}"
            "",
            f"PRICE: {price}\n",
            
            "--------------------------------------------------------------------------",
            "JB Rubber Exports",
            "Canteen Token System"
        ]

        # Printing setup
        printer_name = win32print.GetDefaultPrinter()
        hprinter = win32print.OpenPrinter(printer_name)
        printjob = win32print.StartDocPrinter(hprinter, 1, ("token and logo print job", None, "RAW"))
        win32print.StartPagePrinter(hprinter)

        dc = win32ui.CreateDC()
        dc.CreatePrinterDC(printer_name)
        dc.StartDoc("My Print Job")
        dc.StartPage()

        # Increased font sizes for better visibility
        standard_font = win32ui.CreateFont({"name": "Arial", "height": 30, "weight": win32con.FW_NORMAL})
        bold_font = win32ui.CreateFont({"name": "Arial", "height": 30, "weight": win32con.FW_BOLD})
        receipt_font = win32ui.CreateFont({"name": "Arial", "height": 38, "weight": win32con.FW_BOLD})
        company_font = win32ui.CreateFont({"name": "Arial", "height": 30, "weight": win32con.FW_BOLD})
        price_font = win32ui.CreateFont({"name": "Arial", "height": 36, "weight": win32con.FW_BOLD})  # Larger font for price


        # Print each line with specific formatting
        dib = ImageWin.Dib(image)
        dib.draw(dc.GetHandleOutput(), (0, 0, image.width, image.height))
        y_position = image.height + 20
        for line in text_lines:
            if line == f"{meal_type} Token Receipt":
                dc.SelectObject(receipt_font)
                text_width, text_height = dc.GetTextExtent(line)
                dc.TextOut((image.width - text_width) // 2, y_position, line)
            elif "JB Rubber Exports" in line or "Canteen Token System" in line:
                dc.SelectObject(company_font)
                text_width, text_height = dc.GetTextExtent(line)
                dc.TextOut((image.width - text_width) // 2, y_position, line)
            elif line.startswith("PRICE:"):
                dc.SelectObject(price_font)  # Use the larger font for price
                text_width, text_height = dc.GetTextExtent(line)
                dc.TextOut(10, y_position, line)
            elif line.startswith('-'):
                dc.SelectObject(bold_font)
                dc.TextOut(10, y_position, line)
            else:
                dc.SelectObject(standard_font)
                dc.TextOut(10, y_position, line)
            y_position += 30

        dc.EndPage()
        dc.EndDoc()

        dc.DeleteDC()
        win32print.EndPagePrinter(hprinter)
        win32print.EndDocPrinter(hprinter)
        win32print.ClosePrinter(hprinter)

        # print(record)


    def check_and_display_record(self):
        emp_code = self.ui.lineEdit.text().strip()
        if emp_code:
            if not self.second_db_connection:
                print("No database connection.")
                return

            today_date = datetime.now().strftime("%Y-%m-%d")  # Adjust the date format to match your database format
            cursor = self.second_db_connection.cursor(dictionary=True)
            try:
                query = """
                SELECT * FROM printed_records 
                WHERE emp_code = %s AND DATE(print_time) = %s
                """
                cursor.execute(query, (emp_code, today_date))
                records = cursor.fetchall()

                self.ui.resultTable.setRowCount(0)  # Clear existing rows
                for row_number, record in enumerate(records):
                    self.ui.resultTable.insertRow(row_number)
                    self.ui.resultTable.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(record['token_no'])))
                    self.ui.resultTable.setItem(row_number, 1, QtWidgets.QTableWidgetItem(record['emp_name']))
                    self.ui.resultTable.setItem(row_number, 2, QtWidgets.QTableWidgetItem(record['emp_code']))
                    self.ui.resultTable.setItem(row_number, 3, QtWidgets.QTableWidgetItem(record['meal_type']))
                    self.ui.resultTable.setItem(row_number, 4, QtWidgets.QTableWidgetItem(record['department']))
                    self.ui.resultTable.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(record['print_time'])))
                    self.ui.resultTable.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(record['created_at'])))

                if not records:
                    print("No record found for this employee code today.")
            except Exception as e:
                print(f"Error fetching employee records: {e}")
            finally:
                cursor.close()
        else:
            print("Please enter an employee code.")


        # Fetching Meal Counts
    def update_meal_counts(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        cursor = self.second_db_connection.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT meal_type, COUNT(*) as count
                FROM printed_records
                WHERE DATE(print_time) = %s
                GROUP BY meal_type
            """, (current_date,))
            results = cursor.fetchall()
            breakfast_count = 0
            lunch_count = 0
            dinner_count = 0
            
            for result in results:
                if result['meal_type'] == 'BREAKFAST':
                    breakfast_count = result['count']
                elif result['meal_type'] == 'LUNCH':
                    lunch_count = result['count']
                elif result['meal_type'] == 'DINNER':
                    dinner_count = result['count']
            
            self.ui.breakfastCountLabel.setText(f" {breakfast_count}")
            self.ui.lunchCountLabel.setText(f" {lunch_count}")
            self.ui.dinnerCountLabel.setText(f" {dinner_count}")
        except Exception as e:
            print(f"Error updating meal counts: {e}")
        finally:
            cursor.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_dialog = MyDialog()
    my_dialog.show()
    sys.exit(app.exec_())

    
