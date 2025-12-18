from PySide6.QtWidgets import QApplication
import sys
from windows.home import MainWindow # Homepage window imported


def main():
    app = QApplication(sys.argv)

    window = MainWindow() # Main window
    window.show()

    app.exec()


if __name__ == "__main__":
    main()