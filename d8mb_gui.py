from pystray import Icon, MenuItem, Menu
from PIL import Image
import sys
import os
import d8mb


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class TaskTray:

    def __init__(self):
        self.status = False
        menu = Menu(
                    MenuItem('Exit', self.stop),
                )
        self.icon = Icon(name='Discord_8MB', title='Discord_8MB', icon=Image.open(resource_path("icon.ico")), menu=menu)
        self.hook()

    def run(self):
        self.icon.run()

    def stop(self):
        self.icon.stop()

    def hook(self):
        d8mb.begin_hook()
