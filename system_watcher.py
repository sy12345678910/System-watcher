import sys
from PySide6.QtWidgets import QApplication
from my_system_watcher import SystemWatcher

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    watcher = SystemWatcher()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()