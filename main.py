import keyboard
from win32gui import GetWindowText, GetForegroundWindow
import win32clipboard
from PIL import ImageGrab, Image
from io import BytesIO


IMAGE_SIZE_MAX = 8000000


def is_in_discord():
    # todo  other os
    window_name = GetWindowText(GetForegroundWindow())
    app_name = window_name.split()[-1]
    return app_name == "Discord"


def is_clip_image():
    return isinstance(ImageGrab.grabclipboard(), Image.Image)


def copy_image_to_clipboard(data):
    # todo  other os
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def resize_image_clip():
    image = ImageGrab.grabclipboard()
    image_io = BytesIO()
    resize_level = 1
    while True:
        image = image.resize((image.width // resize_level, image.height // resize_level))
        image.save(image_io, "BMP")
        if image_io.getbuffer().nbytes < IMAGE_SIZE_MAX:
            break
        resize_level += 1
        image_io.seek(0)
        image_io.truncate(0)
    copy_image_to_clipboard(image_io.getvalue()[14:])
    image_io.close()


def on_paste():
    if is_in_discord() and is_clip_image():
        resize_image_clip()
    keyboard.press("ctrl+v")
    keyboard.release("ctrl+v")  # Discord側でvだけがキャンセルされてctrlが押しっぱなしになる現象の回避


keyboard.add_hotkey("ctrl+v", on_paste, (), True)


keyboard.wait()
