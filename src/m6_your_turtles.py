"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Drew Roberts.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
drew = rg.SimpleTurtle('turtle')
drew.pen = rg.Pen('Green', 2)
drew.speed = 15

size = 250

for k in range(10):
    drew.draw_square(size)
    drew.pen_up()
    drew.right(30)
    drew.backward(15)
    drew.left(30)

    drew.pen_down()
    size = size - 15

window = rg.TurtleWindow()
window.tracer(15)
carl = rg.SimpleTurtle('circle')
carl.pen = rg.Pen('red', 3)
carl.forward(50)

for k in range(300):
    carl.right(90)
    carl.forward(k)
