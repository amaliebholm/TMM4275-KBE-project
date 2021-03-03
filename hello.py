#hello.py
from shapes.Block import Block
from shapes.Cylinder import Cylinder
from shapes.Sphere import Sphere

baseBlock = Block(-10, -10, 0, 20, 20, 50, "RED", "Steel")
baseBlock.initForNX()

sTop = Sphere(0, 0, 50, 25, "YELLOW", "Stone")
sTop.initForNX()

cylTool = Cylinder(0,0,50,20,25,[0,0,1],"YELLOW","Wood")
cylTool.initForNX()

sTop.subtract(cylTool)
