#----------------------------------------------------------------------
# Python module to write SVG graphics files.
#
# Copyright 2017-2019 Dr. William T. Verts
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# Basic SVG functions.  All SVG files should be constructed as follows:
#
#   SVGheader(Name of file, width of graphic, height of graphic)
#   SVGprint(String to send to the SVG file)
#   SVGprint(String to send to the SVG file)
#   SVGprint(String to send to the SVG file)
#   SVGprint(String to send to the SVG file)
#   SVGprint(String to send to the SVG file)
#   SVGfooter()
#
# In most cases, SVGprint statements are not called directly, but
# are instead called from geometry functions such as SVGline,
# SVGcircle, SVGellipse, etc.  For example:
#
#   SVGheader("MyFile.svg",600,400)
#   SVGcircle(200,150,75,"red","yellow",3)
#   SVGrectangle(150,190,320,240,"blue","green",2)
#   SVGfooter()
#
#----------------------------------------------------------------------

def SVGprint (S):
    global SVGfile
    SVGfile.write(S + "\n")
    return

def SVGheader (Filename,W,H):
    global SVGfile
    SVGfile = open(Filename, "w")
    SVGprint ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
    SVGprint ('')
    SVGprint ('<svg')
    SVGprint ('    xmlns:svg="http://www.w3.org/2000/svg"')
    SVGprint ('    xmlns="http://www.w3.org/2000/svg"')
    SVGprint ('    version="1.1"')
    SVGprint ('    x="0px"')
    SVGprint ('    y="0px"')
    SVGprint ('    width="' + str(W) + 'px"')
    SVGprint ('    height="' + str(H) + 'px"')
    SVGprint ('    >')
    SVGprint ('')
    return

def SVGfooter ():
    global SVGfile
    SVGprint ('</svg>')
    SVGfile.close()
    return

#----------------------------------------------------------------------
# Plot various objects
#----------------------------------------------------------------------

def SVGcircle (Xc,Yc,R,StrokeColor="black",FillColor="white",StrokeWidth=1):
    SVGprint ('<circle')
    SVGprint ('    cx="' + str(Xc) + '"')
    SVGprint ('    cy="' + str(Yc) + '"')
    SVGprint ('    r="' + str(R) + '"')
    SVGprint ('    stroke="' + StrokeColor + '"')
    SVGprint ('    fill="' + FillColor + '"')
    SVGprint ('    stroke-width="' + str(StrokeWidth) + '"')
    SVGprint ('    />')
    SVGprint ('')
    return

def SVGellipse (Xc,Yc,Rx,Ry,StrokeColor="black",FillColor="white",StrokeWidth=1):
    SVGprint ('<ellipse')
    SVGprint ('    cx="' + str(Xc) + '"')
    SVGprint ('    cy="' + str(Yc) + '"')
    SVGprint ('    rx="' + str(Rx) + '"')
    SVGprint ('    ry="' + str(Ry) + '"')
    SVGprint ('    stroke="' + StrokeColor + '"')
    SVGprint ('    fill="' + FillColor + '"')
    SVGprint ('    stroke-width="' + str(StrokeWidth) + '"')
    SVGprint ('    />')
    SVGprint ('')
    return

def SVGrectangle (X1,Y1,X2,Y2,StrokeColor="black",FillColor="white",StrokeWidth=1):
    W = X2 - X1
    H = Y2 - Y1
    SVGprint ('<rect')
    SVGprint ('    x="' + str(X1) + '"')
    SVGprint ('    y="' + str(Y1) + '"')
    SVGprint ('    width="' + str(W) + '"')
    SVGprint ('    height="' + str(H) + '"')
    SVGprint ('    stroke="' + StrokeColor + '"')
    SVGprint ('    fill="' + FillColor + '"')
    SVGprint ('    stroke-width="' + str(StrokeWidth) + '"')
    SVGprint ('    />')
    SVGprint ('')
    return

def SVGline (X1,Y1,X2,Y2,StrokeColor="black",StrokeWidth=1):
    SVGprint ('<line')
    SVGprint ('    x1="' + str(X1) + '"')
    SVGprint ('    y1="' + str(Y1) + '"')
    SVGprint ('    x2="' + str(X2) + '"')
    SVGprint ('    y2="' + str(Y2) + '"')
    SVGprint ('    stroke="' + StrokeColor + '"')
    SVGprint ('    stroke-width="' + str(StrokeWidth) + '"')
    SVGprint ('    />')
    SVGprint ('')
    return

def SVGtext (X,Y,S,FontSize=12,FontColor="black",FontName="Courier New",Bold=False,Italic=False):
    SVGprint ('<text')
    SVGprint ('    x="' + str(X) + '"')
    SVGprint ('    y="' + str(Y) + '"')
    SVGprint ('    font-family="' + FontName + '"')
    SVGprint ('    font-size="' + str(FontSize) + '"')
    SVGprint ('    fill="' + FontColor + '"')
    if Bold:   SVGprint('    font-weight="bold"')
    if Italic: SVGprint('    font-style="italic"')
    SVGprint ('    >')
    SVGprint ('    ' + S)
    SVGprint ('</text>')
    SVGprint ('')
    return
