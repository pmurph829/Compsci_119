# Peter J. Murphy - Lab #3 - Greebles / Anime Eyes
from DrBillsInputOutput import *
from DrBillsSVGwriter import *
import math

def Test():
    Filename = pickAFolder("Enter Folder for SVG file")+"/TEST.svg"
    SVGheader (Filename,600,600)
    return 

#--------------------------------------------------------------
# This function paints a bunch of lines radially around <Xc,Yc>
# where R1 and R2 are the inner and outer radii and Segments
# indicates the number of lines.
#--------------------------------------------------------------

def addStarburst (Xc,Yc,R1,R2,Segments):
    Angle = 0
    Increment = 2*math.pi / Segments
    while Angle < 2*math.pi:
        X1 = Xc + R1 * math.cos(Angle)
        Y1 = Yc - R1 * math.sin(Angle)
        X2 = Xc + R2 * math.cos(Angle)
        Y2 = Yc - R2 * math.sin(Angle)
        SVGline(X1,Y1,X2,Y2)
        Angle = Angle + Increment
    return

#--------------------------------------------------------------
# This function paints ONE anime eyeball, centered at <Xc,Yc>.
# The color of the iris is NewColor, the pupil is black, and
# the highlights are white. The sizes and positions of the
# iris, pupil, and highlights are derived from center point
# <Xc,Yc> and the radius of the iris R.
#--------------------------------------------------------------

def addEyeball (Xc,Yc,R,NewColor):
    Offset = 0.25 * R * math.sqrt(2)
    Iris       = SVGcircle(Xc,Yc,R,NewColor,NewColor)
    Pupil      = SVGcircle(Xc,Yc,R/2,"black","black")
    addStarburst(Xc, Yc, R/2 + ((1/15)*R), R - ((1/15)*R), 40)
    Highlight1 = SVGcircle(Xc + Offset,Yc - Offset,R/4,"white")
    Highlight2 = SVGcircle(Xc - Offset,Yc + Offset,R/7,"white")
    return

#--------------------------------------------------------------
# This function paints a Greeble at center <Xc,Yc> with Xradius
# indicating the size of the Greeble (everything else is
# computed from those three values). The Greeble has ellipses
# for the body and mouth, and calls addEyeball TWICE (once for
# each eye).
#--------------------------------------------------------------

def addGreeble (Xc,Yc,Xradius,NewColor):
    Yradius = Xradius * (2/5)
    Head = SVGellipse(Xc,Yc,Xradius,Yradius,"black","gray")
    MouthXRadius = Yradius / 2
    MouthYRadius = Yradius / 6
    Mouth = SVGellipse(Xc,Yc + MouthXRadius,MouthXRadius,MouthYRadius,"black","red")
    LEye = addEyeball(Xc - Xradius/2,Yc,Yradius * (2/3),NewColor)
    REye = addEyeball(Xc + Xradius/2,Yc,Yradius * (2/3),NewColor)
    return

#--------------------------------------------------------------
# This function computes the optimal X radius for the Greeble
# based on the size of the graphic, then plots the Greeble at
# the center of the graphic with that X radius.
#--------------------------------------------------------------

def Stare (NewColor,W,H):
    Xmid = W/2
    Ymid = H/2
    if (Xmid-10)<=((Ymid-10)*2.5): Xradius = Xmid - 10
    else                         : Xradius = (Ymid-10)*2.5
    addGreeble(Xmid,Ymid,Xradius,NewColor)
    return

#--------------------------------------------------------------
# Prompt the user for a color. You MAY NOT change ANY code
# in the requestColor function!
#--------------------------------------------------------------

def requestColor (Message):
    Colors = ["red","green","blue","cyan","magenta","yellow"]
    while True:
        S = requestString(Message)
        S = S.lower()
        if (S in Colors): return S

#--------------------------------------------------------------
# This function establishes the size of the canvas and the
# color of the eyes. You MAY NOT change ANY code in
# the Main function except to replace my name with yours!
#--------------------------------------------------------------

def Main():
    Filename = pickAFolder("Enter Folder for SVG file")+"/Greeble.svg"
    Width = requestIntegerInRange("Enter Width",10,1000)
    Height = requestIntegerInRange("Enter Height",10,1000)
    Color = requestColor("Enter Iris Color")
    SVGheader(Filename, Width, Height)
    SVGrectangle(0,0,Width,Height,"black","white")
    SVGtext(10, 35, "Peter J. Murphy", 36, "black", "Arial", True)
    Stare(Color,Width,Height)
    SVGfooter()
    return

