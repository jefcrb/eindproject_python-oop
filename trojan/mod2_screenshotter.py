import os
import asyncio
import pyautogui as pg

class Screenshotter:
    def __init__(self, host_id):
        self.should_run = True
        self.host_id = host_id
    
    async def start(self):
        while self.should_run:
            await self.take_ss()
            await asyncio.sleep(30)
    
    async def take_ss(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        ss_path = os.path.join(script_dir, "..", "logs", self.host_id, 'screenshots')
        pg.screenshot().save(ss_path)

    def stop(self):
        self.should_run = False
