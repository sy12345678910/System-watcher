import psutil
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication, QWidget
from PySide6.QtCore import QObject, QTimer


class SystemWatcher(QWidget):
    def __init__(self):
        super().__init__()
        self.tray_icon = QSystemTrayIcon(self)
        self.setup_menu()
        self.setup_timer(self.update_status)
        
    def setup_menu(self):
        self.menu = QMenu(self)
        self.exit_action = self.menu.addAction('exit')
        self.exit_action.triggered.connect(QApplication.quit)
        self.tray_icon.setContextMenu(self.menu)
        
    def setup_timer(self, func):
        self.timer = QTimer(self)
        self.timer.timeout.connect(func)
        self.timer.start(1000)
        
    def update_status(self):
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        text = f'CPU: {cpu_usage}% | RAM: {ram_usage}%'
        self.tray_icon.setToolTip(text)

    