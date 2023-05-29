import os
import pyautogui as pg
from datetime import datetime

class Screenshotter:
    def __init__(self, host_id):
        self.host_id = host_id
    
    def take_ss(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        ss_path = os.path.join(script_dir, "..", "logs", self.host_id, 'screenshots')
        
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        
        screenshot_name = f"{timestamp}.png"
        screenshot_path = os.path.join(ss_path, screenshot_name)
        pg.screenshot().save(screenshot_path)
