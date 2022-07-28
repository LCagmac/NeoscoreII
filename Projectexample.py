# libraries to import
import pathlib
import math
import time
import threading



from neoscore.common import*
from neoscore.core.brush import Brush
from neoscore.core.color import Color
from neoscore.core.pen import Pen
from neoscore.core.point import ORIGIN, Point
from neoscore.core.positioned_object import PositionedObject
from neoscore.core.text import Text
from neoscore.core import key_event
#from helpers import render_example
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



window_center_x = Unit(0)
window_center_y = Unit(-300)
neoscore.setup(A4.make_rotation())

flowable = Flowable((Mm(0), Mm(0)), None, Mm(500), Mm(30), Mm(10))

staff = Staff((Mm(10), Mm(50)), flowable, Mm(500))
unit = staff.unit
clef = Clef(ZERO, staff, "treble")
KeySignature(ZERO, staff, "f_major")

center = unit(15)

n1 = Notehead(center, staff, "e", Duration(1, 4))
n2 = Notehead(center, staff, "a", Duration(1, 4))
n3 = Notehead(center, staff, "c", Duration(1, 4))
n4 = Notehead(center, staff, "f", Duration(1, 4))
n5 = Notehead(center, staff, "b", Duration(1, 4))
n6 = Notehead(center, staff, "g", Duration(1, 4))

#images to import
resources_dir = (pathlib.Path(__file__).parent / ".." / "tests").resolve()
pixmap_path = resources_dir / "square.png"
svg_path = resources_dir / "triangle.png"
svg_again = resources_dir / "triangle1.png"
square_two = resources_dir / "squareicon.png"
cover_shape = resources_dir / "kshape.png"
kaleidoscopeturn = resources_dir/"kaleidoscopepartI.png"


runner = -300



#location of images on score
Donut = Image((Mm(-30), Mm(-30)), None, kaleidoscopeturn, scale=5.0, z_index = 23000)
CS = Image((Mm(-100), Mm(-50)), None, cover_shape, scale=0.5, z_index = 20000)
IN=Image(ORIGIN, None, pixmap_path, scale = 0.5)
INI=Image((Mm(75), Mm(10)), None, pixmap_path, scale = 0.5)
INII=Image((Mm(75), Mm(70)), None, pixmap_path, scale = 0.5)
INIII=Image((Mm(45), Mm(130)), None, pixmap_path, scale = 0.5)
INIV=Image((Mm(200), Mm(10)), None, pixmap_path, scale = 0.5)
INV = Image((Mm(200), Mm(150)), None, pixmap_path, scale = 0.5)
Tri=Image(ORIGIN, None, svg_again, 0.2)
TriI = Image((Mm(75), Mm(50)), None, svg_again, 0.4)
TriII=Image((Mm(90), Mm(10)), None, svg_again, 0.2)


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


#Background color

def colorchange0():
    brush = set_background_brush(colorselect[0])

brush = set_background_brush(colorselect[0])
t = threading.Timer(1, colorchange0)
t.start()


#functions for animations
def refresh_func(time):
    Im.z_index = (math.sin((time / 2)) * 8000)
    IN.rotation = (math.sin((time / 2)) * 800)
    INI.z_index = (math.sin((time / 2)) * 1000)
    Tri.z_index = (math.sin((time / 2)) * 80)
    Tri.rotation = (math.sin((time / 2)) * 100)
    ImI.rotation = (math.sin((time / 2)) * 2000)
    INIV.z_index = (math.sin((time / 2)) * 500)
    INV.z_index = (math.sin((time / 2)) * 4000)
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

    n1.x = center + Mm(math.sin((time / 2)) * 10)
    n2.x = center + Mm(math.sin((time / 2) + 1) * 12)
    n3.x = center + Mm(math.sin((time / 2) + 1.7) * 7)
    n4.x = center + Mm(math.sin((time / 2) + 2.3) * 15)
    n5.x = center + Mm(math.sin((time / 2) + 2.3) * 5)
    n6.x = center + Mm(math.sin((time / 2) + 2.3) * 20)
    #kaleidoscope "handpiece" that moves with animation
    Donut.rotation = (math.sin((time)))

def refresh_func1(time):
    Im.y = (math.sin((time / 2)) * -8000)
    IN.x = (math.sin((time / 2)) * 800)
    INI.y = (math.sin((time / 2)) * -1000)
    Tri.x = (math.sin((time / 2)) * 80)
    Tri.y = (math.sin((time / 2)) * -100)
    ImI.x = (math.sin((time / 2)) * 2000)
    INIV.y = (math.sin((time / 2)) * -500)
    INV.x = (math.sin((time / 2)) * 4000)
    MusicExample.z_index = (math.sin((time / 2)) * -10000)
    ImII.y = (math.sin((time * 2)) * 10000)
    ImII.x = (math.sin((time * 2)) * -5000)
    INII.y= (math.sin((time * 4)) * 5000)
    INIII.x=(math.sin((time * 2)) * -5000)
    TriI.y = (math.sin((time * 5)) * 5000)
    TriII.x=(math.sin((time * 3)) * -5000)
    Tri1.y= (math.sin((time * 4)) * 5000)
    TriI1.x = (math.sin((time * 2)) * -5000)
    TriI2.y = (math.sin((time / 2)) * 500)
    TriII1.x= (math.sin((time * 2)) * -5000)
    TriII1.y= (math.sin((time * 2)) * 5000)
    Squar.x= (math.sin((time * 5)) * -5000)
    SquarI.y= (math.sin((time * 3)) * 5000)



#if a key is hit then the animation starts
KeyHit = key_event.KeyEvent(event_type= 1, code= 0x01000012, modifiers=0, text = None)


def key_handler(event):
    """Simply print key events"""
    if(KeyHit.text == None and KeyHit.code == 0x01000012 and KeyHit.event_type == 1):
        neoscore.show(refresh_func)
        print(event)



neoscore.set_key_event_handler(key_handler)


#render_example("images")
if __name__ == "__main__":
    neoscore.show(auto_viewport_interaction_enabled=False)
