import sys
import PyQt5.QtWidgets as PyQt
from PyQt5 import uic
from controller.Main import principal

def main():
    app = PyQt.QApplication([])
    window = principal()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
