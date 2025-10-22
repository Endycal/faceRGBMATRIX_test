#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
from colorama import Fore, Back, Style
import time
import random
import keyboard 

#LINE -> graphics.DrawLine(canvas, posA_x, posA_y, posB_x, posB_y, color)
#CIRCLE -> graphics.DrawCircle(canvas, pos_x, pos_y, radius, color)
#TEXT -> graphics.DrawText(canvas, font, pos_x, pos_y, color, str(text))

class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):

        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")

        main = graphics.Color(230, 0, 230)
        color2 = graphics.Color(0, 255, 0)

        updates = 0
        show = True

        def normale_faccia():
            #print(Style.DIM + Fore.GREEN + "                      | Rendering normale_faccia()", end="\r", flush=True)

            rint = random.randint(1,10)

            if rint <= 9:
                             graphics.DrawCircle(canvas, 48, 15, 10, main)
                             graphics.DrawCircle(canvas, 48, 15, 9, main)

                             graphics.DrawCircle(canvas, 15, 15, 10, main)
                             graphics.DrawCircle(canvas, 15, 15, 9, main)

                             graphics.DrawLine(canvas, 31, 21, 35, 26, main)
                             graphics.DrawLine(canvas, 31, 21, 25, 26, main)
            else:
                             print("			last blink at " + str(updates), end="\r", flush=True)

                             graphics.DrawLine(canvas, 5, 15, 25, 15, main)
                             graphics.DrawLine(canvas, 5, 16, 25, 16, main)

                             graphics.DrawLine(canvas, 38, 15, 58, 15, main)
                             graphics.DrawLine(canvas, 38, 16, 58, 16, main)

                             graphics.DrawLine(canvas, 31, 21, 35, 26, main)
                             graphics.DrawLine(canvas, 31, 21, 25, 26, main)

        def clock():
            graphics.DrawText(canvas, font, 4, 17, main, time.strftime("%H:%M:%S"))

            graphics.DrawLine(canvas, 31, 21, 35, 26, main)
            graphics.DrawLine(canvas, 31, 21, 25, 26, main)


        def testo():
            graphics.DrawText(canvas, font, 24, 10, main, "aaaaaaa")

        def paroline_magiche():
            inputting = input("Digita una parolina magica...")

            if inputting == "clock that tea":
                clock()
                show = True

        while True:
            canvas.Clear()

            if show == True:
                normale_faccia()
                #clock()
            else:
                paroline_magiche()

            if keyboard.is_pressed("h"):
                show = False

            print(Fore.WHITE + Style.DIM + "UPDATES: "+ Style.BRIGHT + Fore.MAGENTA + str(updates), end="\r", flush=True)
            time.sleep(0.1)
            updates += 1

# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
