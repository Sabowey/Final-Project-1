from logic import *

def main() -> None:
    """
    Method to create window
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__=='__main__':
    main()