import app
import time

from events.input import Buttons, BUTTON_TYPES
from tildagonos import tildagonos



class Bling(app.App):
    def __init__(self):
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()
        for i in range(0,12):
                time.sleep(0.05)
                tildagonos.leds[i+1] = (255, 215, 0)
        

    def draw(self, ctx):
        ctx.save()
        ctx.font_size = 90
        ctx.rgb(250, 250, 210).rectangle(-120,-120,240,240).fill()
        ctx.rgb(255, 215, 0).move_to(-100,20).text("Bling!")
        ctx.restore()

__app_export__ = Bling 
