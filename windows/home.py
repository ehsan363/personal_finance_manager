# Importing modules from PySide6 library
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QToolBar
from PySide6.QtGui import QAction, QFont, QIcon
from PySide6.QtCore import Qt
# Homepage window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('FundTrack') # Title of the window

        # Window size
        self.resize(1920, 1080)
        self.setMinimumSize(1170, 650)

        # Window icon
        self.setWindowIcon(QIcon('../img/icon.png'))

        # Font elements
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)

        # Create UI elements

        self.heading = QLabel("HomePage")
        self.heading.setAlignment(Qt.AlignLeft)
        self.heading.setStyleSheet("""
        font-size: 36px;
        padding-top: 15px;
        padding-left: 10px;
        font-weight: bold;""")

        # Toolbar options
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)
        toolbar.setStyleSheet('Background-color: #e78c4d; font-size: 20px;')

        action_add = QAction("Add Expense", self)
        toolbar.addAction(action_add)

        action_add = QAction("Edit Expense", self)
        toolbar.addAction(action_add)

        action_add = QAction("Edit Income", self)
        toolbar.addAction(action_add)

        action_add = QAction("History", self)
        toolbar.addAction(action_add)

        action_add = QAction("User", self)
        toolbar.addAction(action_add)

        action_add = QAction("Settings", self)
        toolbar.addAction(action_add)

        # Connect button click to function
        #self.button.clicked.connect(self.increase_count)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.heading)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        centralWidget.setStyleSheet('background-color: #141414; color: #e78c4d;')
        self.setCentralWidget(centralWidget)
        self.setCentralWidget(centralWidget)
