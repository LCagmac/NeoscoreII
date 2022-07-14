import pathlib
import math
import time
import pynput
from pynput import keyboard
import pygame
import threading
import sys
from pygame import event
from pynput.keyboard import Key, Listener
from neoscore.common import*

from neoscore.core.brush import Brush
from neoscore.core.color import Color
from neoscore.core.pen import Pen
from neoscore.core.point import ORIGIN, Point
from neoscore.core.positioned_object import PositionedObject
from neoscore.core.text import Text

from helpers import render_example
from neoscore.core import neoscore
from neoscore.core import paper
from neoscore.core.paper import Paper
from neoscore.core.paper import A4
from neoscore.core.paper import LETTER
from neoscore.core.image import Image
from neoscore.core.point import ORIGIN
from neoscore.core import neoscore
from neoscore.core.flowable import Flowable
from neoscore.core.path import Path
from neoscore.core.units import ZERO, Mm
from neoscore.western.clef import Clef
from neoscore.western.duration import Duration
from neoscore.western.key_signature import KeySignature
from neoscore.western.notehead import Notehead
from neoscore.western.staff import Staff
from neoscore.core.neoscore import set_background_brush


#paperI = new Paper.modified(width=Mm(300), height= Mm(200), margin_top=None, margin_right= Inch(3.0), margin_bottom= Inch(2.0), margin_left=None, gutter=None)
#paperII = new Paper.__init__(width=Mm(210), height=Mm(297), margin_top=Mm(20), margin_right= Mm(2), margin_bottom= Mm(2), margin_left=Inch(20), gutter=Mm(0.0))

window_center_x = Unit(0)
window_center_y = Unit(-300)
neoscore.setup(A4.make_rotation())

resources_dir = (pathlib.Path(__file__).parent / ".." / "tests" / "resources").resolve()
pixmap_path = resources_dir / "square.png"
svg_path = resources_dir / "triangle.png"
svg_again = resources_dir / "triangle1.png"
musi_examp = resources_dir / "music.png"
square_two = resources_dir / "squareicon.png"

#flowable = Flowable((Mm(0), Mm(0)), None, Mm(500), Mm(30), Mm(10))
#staff = Staff((Mm(0), Mm(0)), flowable, Mm(500))
#unit = staff.unit
#clef = Clef(ZERO, staff, "treble")
#KeySignature(ZERO, staff, "g_major")
runner = -300

#z = 2000

#center = unit(15)

IN=Image(ORIGIN, None, pixmap_path, scale = 0.5)
INI=Image((Mm(75), Mm(10)), None, pixmap_path, scale = 0.5)
INII=Image((Mm(75), Mm(70)), None, pixmap_path, scale = 0.5)
INIII=Image((Mm(45), Mm(130)), None, pixmap_path, scale = 0.5)
INIV=Image((Mm(200), Mm(10)), None, pixmap_path, scale = 0.5)
INV = Image((Mm(200), Mm(150)), None, pixmap_path, scale = 0.5)
Tri=Image(ORIGIN, None, svg_again, 0.2)
TriI = Image((Mm(75), Mm(50)), None, svg_again, 0.4)
TriII=Image((Mm(90), Mm(10)), None, svg_again, 0.2)
MusicExample = Image((Mm(40), Mm(50)), None, musi_examp, 0.5, rotation=0, z_index=-1000)

IN1=Image((Mm(160), Mm(30)), None, pixmap_path, scale = 0.5)
INI1=Image((Mm(130), Mm(80)), None, pixmap_path, scale = 0.5)
INII1=Image((Mm(130), Mm(100)), None, pixmap_path, scale = 0.5)
INIII1=Image((Mm(100), Mm(140)), None, pixmap_path, scale = 0.5)
INIV1=Image((Mm(150), Mm(70)), None, pixmap_path, scale = 0.5)
INV1 = Image((Mm(45), Mm(150)), None, pixmap_path, scale = 0.5)
IN2=Image((Mm(50), Mm(50)), None, pixmap_path, scale = 0.5)
INV1 = Image((Mm(130), Mm(45)), None, pixmap_path, scale = 0.5)
Tri1=Image((Mm(10), Mm(100)), None, svg_again, 0.2)
TriI1 = Image((Mm(100), Mm(60)), None, svg_again, 0.4)
TriI2 = Image((Mm(60), Mm(30)), None, svg_again, 0.4)
TriII1=Image((Mm(90), Mm(10)), None, svg_again, 0.2)
TriII1=Image((Mm(120), Mm(45)), None, svg_again, 0.2)
Squar= Image((Mm(175), Mm(50)), None, square_two, 1.0)
SquarI= Image((Mm(75), Mm(50)), None, square_two, 1.0, rotation=0, z_index=-100)
#MusicExample = Image((Mm(40), Mm(50)), None, musi_examp, scale=0.5, rotation=runner, z_index=-300)

#Image((Mm(10), Mm(10)), None, svg_path, 2)

Im = Image((Mm(50), Mm(20)), None, svg_path, scale = 0.5, rotation=runner, z_index=runner)
ImI = Image((Mm(150), Mm(20)), None, svg_path, scale = 0.5, rotation=runner, z_index=runner)
ImII = Image((Mm(250), Mm(20)), None, svg_path, scale = 0.5, rotation=runner, z_index=runner)
Im = Image((Mm(75), Mm(80)), None, svg_path, scale = 0.5, rotation=runner, z_index=runner)
ImI = Image((Mm(150), Mm(100)), None, svg_path, scale = 0.5, rotation=runner, z_index=runner)
ImII = Image((Mm(45), Mm(100)), None, svg_path, scale = 0.5, rotation=runner, z_index=runner)
ImII = Image((Mm(90), Mm(45)), None, svg_path, scale = 0.5, rotation=runner, z_index=runner)
#Image((Mm(120), Mm(220)), None, svg_path, rotation=180, z_index=2)

colorselect = [	"800080", "ebebeb", "e0e0e0", "d6d6d6", "cccccc", "c2c2c2", "b8b8b8", "adadad", "a3a3a3", "999999", "858585",
"7a7a7a", "707070", "666666", "5c5c5c", "525252", "474747", "3d3d3d", "333333", "292929", "1f1f1f", "141414", "0a0a0a", "000000"]

#snippet VI


def colorchange0():
    brush = set_background_brush(colorselect[0])

brush = set_background_brush(colorselect[0])
t = threading.Timer(1, colorchange0)
t.start()



def action():
    Im.z_index = (math.sin((300 / 2)) * z)

def valuechange():
    z = 1000

def valuechangeI():
    z = -1000

def refresh_func(time):
    #Im.y = center + Mm(math.sin((time / 2)) * 10)
    Im.z_index = (math.sin((time / 2)) * 8000)
    IN.rotation = (math.sin((time / 2)) * 800)
    INI.z_index = (math.sin((time / 2)) * 1000)
    Tri.z_index = (math.sin((time / 2)) * 80)
    Tri.rotation = (math.sin((time / 2)) * 100)
    ImI.rotation = (math.sin((time / 2)) * 2000)
    INIV.z_index = (math.sin((time / 2)) * 500)
    INV.z_index = (math.sin((time / 2)) * 4000)
    MusicExample.z_index = (math.sin((time / 2)) * 10000)
    ImII.z_index = (math.sin((time * 2)) * 10000)
    ImII.z_index = (math.sin((time * 2)) * 5000)
    INII.z_index= (math.sin((time * 4)) * 5000)
    INIII.z_index=(math.sin((time * 2)) * 5000)
    TriI.z_index = (math.sin((time * 5)) * 5000)
    TriII.z_index=(math.sin((time * 3)) * 5000)
    Tri1.z_index= (math.sin((time * 4)) * 5000)
    TriI1.z_index = (math.sin((time * 2)) * 5000)
    TriI2.z_index = (math.sin((time / 2)) * 500)
    TriII1.z_index= (math.sin((time * 2)) * 5000)
    TriII1.z_index= (math.sin((time * 2)) * 5000)
    Squar.z_index= (math.sin((time * 5)) * 5000)
    SquarI.z_index= (math.sin((time * 3)) * 5000)

#t = threading.Timer(10, neoscore.show(refresh_func))

#t1 = threading.Timer(15, valuechangeI)

#t1.start()
#window = pygame.display.set_mode((1000,800)) #Create a 1000x800 window


            #if event.key == pygame.K_f:
                #neoscore.show()
        #if event.type == pygame.KEYDOWN: #if a key is pressed down
        #    if event.key == pygame.K_f:
        #        print("Hi")
        #        neoscore.show()
                    #if event.key == pygame.K_f:
                        #neoscore.show()


#if __name__ == "__main__":
    #neoscore.show(refresh_func)
    #neoscore.show()
    #t = threading.Timer(10, refresh_func, ['bb'])
    #while 1:
    #    pass
    #t.start()

#Path.ellipse((Mm(0), Mm(10)), None, Mm(200), Mm(200), "#00ff00")

render_example("images")
