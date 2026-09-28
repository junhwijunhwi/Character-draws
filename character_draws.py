from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

clear_canvas()
character.draw(100, 100)
update_canvas()
delay(10)


close_canvas()



