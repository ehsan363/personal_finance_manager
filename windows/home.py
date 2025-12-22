# Importing modules from PySide6 library
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QToolBar, QFrame
from PySide6.QtGui import QAction, QFont, QIcon
from PySide6.QtCore import Qt
from data.database import DBmanager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('FundTrack') # Title of the window
        # Window size
        self.resize(1920, 1080)
        self.setMinimumSize(1170, 650)

        # Window icon
        self.setWindowIcon(QIcon('img/iconOrange#141414bgR.png'))

        # Font elements
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)

        # Layout
        pageLayout = QVBoxLayout()
        pageLayout.setAlignment(Qt.AlignTop)
        pageLayout.setSpacing(15)

        topRow = QHBoxLayout()
        topRow.setAlignment(Qt.AlignLeft)
        topRow.setSpacing(20)

        # Create UI elements
        self.heading = QLabel("HomePage")
        self.heading.setAlignment(Qt.AlignLeft)
        self.heading.setStyleSheet("""
            font-size: 36px;
            padding-top: 15px;
            padding-left: 10px;
            font-weight: bold;""")

        summaryCard = QFrame() # Summary card
        summaryCard.setFixedWidth(300)
        summaryCard.setStyleSheet("""
            background-color: #222222;
            padding: 10px;
            border-radius: 25px;
            margin-left: 20px;""")

        self.summaryLabel = QLabel('Summary')
        self.summaryLabel.setStyleSheet("""
            font-size: 28px;
            color: White;
            font-weight: bold;
            margin-left: 30px;
            padding-top: 5px;
            margin-top: 20px;
            background-color: #242424;""")

        budgetFile = open('data/budget.txt','r')
        self.budgetRead = budgetFile.readline()
        budgetFile.close()

        self.budget = f'Budget: {int(self.budgetRead):,}AED'
        summaryLayout = QVBoxLayout(summaryCard)
        summaryLayout.addWidget(self.summaryLabel)
        budgetLabel = QLabel(self.budget)
        budgetLabel.setAlignment(Qt.AlignTop)
        summaryLayout.addWidget(budgetLabel)

        db = DBmanager()
        totalExpense = db.Expense()
        totalExpenseLabel = QLabel(f"Expense: {totalExpense}")
        summaryLayout.addWidget(totalExpenseLabel)

        topRow.addWidget(summaryCard)



        #aaaaaaaaaaaaaaaaaaa
        graphCard = QFrame()
        graphCard.setStyleSheet("""
            background-color: #1f3b14;
            border-radius: 20px;
        """)

        graphLayout = QVBoxLayout(graphCard)
        graphLayout.addWidget(QLabel("Graph", alignment=Qt.AlignCenter))

        topRow.addWidget(graphCard, stretch=2)
        #aaaaaaaaaaaaaaaaaaa

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
        # #self.button.clicked.connect(self.increase_count)

        pageLayout.addWidget(self.heading)
        pageLayout.addLayout(topRow)

        pageLayout.addStretch() # <-- Should be last! To make everything in layout align to the left

        centralWidget = QWidget()
        centralWidget.setLayout(pageLayout)
        centralWidget.setStyleSheet('background-color: #141414; color: #e78c4d;')
        self.setCentralWidget(centralWidget) # <-- Stuff into Central Widget