from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')
angle = 0
x2 = 100
y2 = 100

while True:
    x = 200 + 100 * math.sin(angle)
    y = 200 + 100 * math.cos(angle)
   

    if 100<=x2<200 and y2 >=100:
        x2+=2
    if x2>=200 and y2 >=100:
        y2+=2
    if 100<x2<=200 and y2>=200:
        x2-=2
    if x2>=100 and y2 <=200:
        y2-=2    


    clear_canvas()
    character.draw(x, y)
    character.draw(x2,y2)
    update_canvas()
    delay(0.01)
    angle += 0.05





