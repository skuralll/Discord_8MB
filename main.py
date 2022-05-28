from d8mb_gui import run_gui
from keyboard_handler import run_handler
import time

if __name__ == '__main__':
    gui_thread = run_gui()
    handler_thread = run_handler()
    while gui_thread.is_alive() and handler_thread.is_alive():
        time.sleep(1)

