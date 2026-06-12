import psutil
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication, QStyle
from PySide6.QtCore import QObject, QTimer, Slot
from PySide6.QtGui import QPixmap


class SystemWatcher(QObject):
    def __init__(self):
        super().__init__()
        self.tray_icon = QSystemTrayIcon(self)
        std_icon = QPixmap('cpu.png')  
        self.tray_icon.setIcon(std_icon)

        self.setup_menu()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)
        
        self.tray_icon.show()
        
    def setup_menu(self):
        self.menu = QMenu()
        exit_action = self.menu.addAction('exit')
        exit_action.triggered.connect(QApplication.quit)
        self.tray_icon.setContextMenu(self.menu)
    
    @Slot()
    def update_status(self):
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        text = f'CPU: {cpu_usage}% | RAM: {ram_usage}%'
        self.tray_icon.setToolTip(text)

    