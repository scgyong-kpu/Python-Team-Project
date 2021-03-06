from pico2d import *
import gfw
import gobj
from button import Button


import ctypes

user32 = ctypes.windll.user32
canvas_width, canvas_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def enter():
    gfw.world.init(['bg', 'ui'])

    center = (canvas_width//2, canvas_height//2)
    bg = gobj.ImageObject('bg.png', center)
    gfw.world.add(gfw.layer.bg, bg)

    # Button(l, b, w, h, font, text, callback, btnClass=None):
    font = gfw.font.load(gobj.res('ENCR10B.TTF'), 40)

    l,b,w,h = 50,350,get_canvas_width()-100,80
    btn = Button(l,b,w,h,font,"Play Card Version", lambda: print("Card"))
    gfw.world.add(gfw.layer.ui, btn)

    b -= 120
    btn = Button(l,b,w,h,font,"Play Twice Version", lambda: print("Twice"))
    gfw.world.add(gfw.layer.ui, btn)

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    
def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()

    # print('ms.he()', e.type, e)
    if handle_mouse(e):
        return

capture = None 
def handle_mouse(e):
    global capture
    if capture is not None:
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    for obj in gfw.world.objects_at(gfw.layer.ui):
        if obj.handle_event(e):
            capture = obj
            return True

    return False

def exit():
    pass

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()
