"""
Filename    : exportImage.py
Description : 
"""

import model.relationship as r
import view.View as v
from PIL import (Image, ImageDraw)
import model.UMLClass as u
import math
from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    drawLine strategy super class
    """
    @abstractmethod
    def drawLine(self, image, startPt, endPt):
        pass

class exportImage():
    """
    export image class that uses strategy design pattern for each different line type
    """
    def __init__(self, strategy: Strategy):

        self._strategy = strategy
        self.boxes = None
        self.canvas = Image.new("RGB", (5000, 5000), color = "white")
        self.image = ImageDraw.Draw(self.canvas)
        self.startPt = None
        self.endPt = None

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def createBoxes(self):
        """
        fills boxes dictionary with umlclassname -> box coords (x, y)
        """
        self.boxes = {}
        #saves the coords of each box in a list
        for each in u.classIndex:
            new = v.classToString(each)    
            #gets the coords for each box based on x,y and text size
            coords = self.image.multiline_textbbox(xy=(each.location['x'], each.location['y']), text = new[0])
            #saves coods in a list with a buffer to draw boxes later
            self.boxes[each.name] = (coords[0] - 10, coords[1] - 10, coords[2] + 10, coords[3] + 10)

    def setCoords(self, each):
        """
        determines and sets the coordinate of the start and end points of a line to be drawn
        :param each: UML relationship object
        """

        #gets coords for source and dest
        sCoord = self.boxes[each.source]
        dCoord = self.boxes[each.destination]
        
        #if we want to use source edge coords instead of center coords
        # use the following 
        """
        sNW = (sCoord[0], sCoord[1])
        sW = (sCoord[0], sCoord[1] + (sCoord[3] - sCoord[1])//2)
        sN = (sCoord[0] + (sCoord[2] - sCoord[0])//2, sCoord[1])
        sNE = (sCoord[2], sCoord[1])
        sE = (sCoord[2], sCoord[1] + (sCoord[3] - sCoord[1])//2)
        sSE = (sCoord[2], sCoord[3])
        sS = (sCoord[0] + (sCoord[2] - sCoord[0])//2, sCoord[3])
        sSW = (sCoord[0], sCoord[3])
        sPoints = [sNW,sN,sNE,sE,sSE,sS,sSW,sW]
        """
        #determine center point of source box
        midPt = ((sCoord[2] - sCoord[0])//2 + sCoord[0], (sCoord[3] - sCoord[1])//2 + sCoord[1])
        sPoints = [midPt]

        #determines corner and center-edge points of dest box
        dNW = (dCoord[0], dCoord[1])
        dW = (dCoord[0], dCoord[1] + (dCoord[3] - dCoord[1])//2)
        dN = (dCoord[0] + (dCoord[2] - dCoord[0])//2, dCoord[1])
        dNE = (dCoord[2], dCoord[1])
        dE = (dCoord[2], dCoord[1] + (dCoord[3] - dCoord[1])//2)
        dSE = (dCoord[2], dCoord[3])
        dS = (dCoord[0] + (dCoord[2] - dCoord[0])//2, dCoord[3])
        dSW = (dCoord[0], dCoord[3])
        dPoints = [dNW,dN,dNE,dE,dSE,dS,dSW,dW]
        
        #determines closest dest point (above) to center source point 
        #saves a tuple (index, index) to get coord out of sPoints, dPoints
        m = math.dist(midPt,dNW)
        indexes = (0,0)
        for first in range(len(sPoints)):
            for second in range(len(dPoints)):
                val = math.dist(sPoints[first],dPoints[second])
                if m > val:
                    indexes = (first, second)
                    m = val
        #the source point and dest points determined above            
        self.startPt = sPoints[indexes[0]]
        self.endPt = dPoints[indexes[1]]
    
    
    def drawLines(self):
        """
        draws a line to the image based on the current selected strategy
        """
        self._strategy.drawLine(self.image, self.startPt, self.endPt)

    def drawBoxes(self):
        """
        draws the boxes to the image
        """
        for each in u.classIndex:
            #get text
            new = v.classToString(each)
            #draw box
            self.image.rectangle(xy=self.boxes[each.name], outline="black", fill = '#F0F0F0')    
            #draw text
            self.image.multiline_text(xy=(each.location['x'], each.location['y']), text = new[0], spacing=4, align='left', fill="black")        

    def exportEmpty(self, fileName):
        """
        saves a 800x600 canvas as the image if no boxes
        :param fileName: filename to save as
        """
        self.canvas = Image.new("RGB", (800, 600), color = "white")
        self.image = ImageDraw.Draw(self.canvas)
        self.canvas.save(fileName)

    def export(self, fileName):
        """
        saves a cropped image if boxes exist
        :param fileName: filename to save as  
        """
        xMin = []
        yMin = [] 
        xMax = []
        yMax = []
        #adds the coords of each box to a list
        for each in self.boxes:
            xMin.append(self.boxes[each][0])
            yMin.append(self.boxes[each][1])
            xMax.append(self.boxes[each][2])
            yMax.append(self.boxes[each][3])
        #determines largest/smallest xy coord 
        x = min(xMin)
        y = min(yMin)
        h = max(yMax) 
        w = max(xMax)
        #crops the canvas
        self.canvas = self.canvas.crop((x-10,y-10,w+10,h+10))
        #saves it to file
        self.canvas.save(fileName)


class inherLine(Strategy):
    """
    inheritance line strategy
    """
    
    def drawLine(self, image, startPt, endPt):
        """
        draws a solid line with a empty (white) arrow tip
        :param image: image to draw to  
        :param startPt: start point (x,y) for line 
        :param endPt: end point (x,y) for line 
        """   
        color = "white"
        image.line(xy=(startPt, endPt), fill="black", width=2)
        #if verticle line
        if startPt[0] == endPt[0]:
            #if pointing up
            if startPt[1] > endPt[1]:
                #draw triangle using 3 coords based on end point of line
                image.polygon([endPt, (endPt[0] + 8, endPt[1] + 8), (endPt[0] - 8, endPt[1] + 8)],fill=color ,outline="black")
            #pointing down
            else:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] - 8), (endPt[0] - 8, endPt[1] - 8)], fill=color, outline="black" )
        #if horiz line
        elif startPt[1] == endPt[1]:
            if startPt[0] > endPt[0]:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] + 8), (endPt[0] + 8, endPt[1] - 8)], fill=color, outline="black")
            else:
                image.polygon([endPt, (endPt[0] - 8, endPt[1] + 8), (endPt[0] - 8, endPt[1] - 8)], fill=color, outline="black")
        #not horiz or vert
        else:
            #determine slope of line
            slope = (endPt[1] - startPt[1]) / (endPt[0] - startPt[0])
            #line point towards the right direction
            if startPt[0] < endPt[0]:
                #fancy math to determing the coords of the triangle to draw based on line angle
                baseX, baseY = (endPt[0] - (8 / (math.sqrt(1 + slope**2))), endPt[1] - (8 * slope) / (math.sqrt(1 + slope**2))) 
                invSlope = -1/slope
                pt1x, pt1y = (baseX - (8 / (math.sqrt(1 + invSlope**2))), baseY - (8 * invSlope) / (math.sqrt(1 + invSlope**2))) 
                pt2x, pt2y = (baseX + (8 / (math.sqrt(1 + invSlope**2))), baseY + (8 * invSlope) / (math.sqrt(1 + invSlope**2)))
                #draw the triangle using coords above
                image.polygon([endPt, (pt1x,pt1y), (pt2x, pt2y)], fill=color, outline="black")     
            #line point towards the left direction
            else:
                baseX, baseY = (endPt[0] + (8 / (math.sqrt(1 + slope**2))), endPt[1] + (8 * slope) / (math.sqrt(1 + slope**2))) 
                invSlope = -1/slope
                pt1x, pt1y = (baseX - (8 / (math.sqrt(1 + invSlope**2))), baseY - (8 * invSlope) / (math.sqrt(1 + invSlope**2))) 
                pt2x, pt2y = (baseX + (8 / (math.sqrt(1 + invSlope**2))), baseY + (8 * invSlope) / (math.sqrt(1 + invSlope**2)))
                image.polygon([endPt, (pt1x,pt1y), (pt2x, pt2y)], fill=color, outline="black")
           

class realLine(Strategy):
    """
    realization line strategy  
    """
    
    def drawLine(self, image, startPt, endPt):
        """
        draws a dashed line with a empty (white) arrow tip
        :param image: image to draw to  
        :param startPt: start point (x,y) for line 
        :param endPt: end point (x,y) for line 
        """   
        color = "white"
        #starting x and y points
        x = startPt[0]
        y = startPt[1] 
        #if line is verticle 
        if startPt[0] == endPt[0]:
            #if line points up
            if startPt[1] > endPt[1]:
                #draw 4 pixes then skip 4 pixes until reach end of line
                while y > endPt[1]:
                    #go 4 pixels up
                    nextX, nextY = (x,  y - 4)
                    #draw line from start pt to 4 pixels up
                    image.line(xy=((x,y),(nextX, nextY)), fill="black", width=2)
                    #update start pt to 4 pixels past end pt of most recently drawn line segment
                    x, y = (nextX,  nextY - 4)
            #line points down
            else:
                while y < endPt[1]:
                    nextX, nextY = (x,  y + 4)
                    image.line(xy=((x,y),(nextX, nextY)), fill="black", width=2)
                    x, y = (nextX,  nextY + 4)                                    
        #if line is horizontal
        elif startPt[1] == endPt[1]:
            #line points right
            if startPt[0] > endPt[0]:
                while x > endPt[0]:
                    nextX, nextY = (x - 4, y)
                    image.line(xy=((x,y),(nextX, nextY)), fill="black", width=2)
                    x, y = (nextX - 4, nextY)
            #line points left
            else:
                while x < endPt[0]:
                    nextX, nextY = (x + 4, y)
                    image.line(xy=((x,y),(nextX, nextY)), fill="black", width=2)
                    x, y = (nextX + 4, nextY)
        #line is not horiz or vert
        else:
            #determines slope
            slope = (endPt[1] - startPt[1]) / (endPt[0] - startPt[0])
            #if lines points towards the right
            if startPt[0] < endPt[0]:
                while x < endPt[0]:
                    #fancy math to go 4 pixels down the line
                    nextX, nextY = (x + (4 / (math.sqrt(1 + slope**2))), y + (4 * slope) / (math.sqrt(1 + slope**2)))
                    #draw the line
                    image.line(xy=((x,y),(nextX,nextY)), fill="black", width=2)
                    #move x and y 4 more pixels down the line (makes space)
                    x, y = (nextX + (4 / (math.sqrt(1 + slope**2))), nextY + (4 * slope) / (math.sqrt(1 + slope**2)))
            #if lines points towards the left
            else:
                while x > endPt[0]:
                    nextX, nextY = (x - (4 / (math.sqrt(1 + slope**2))), y - (4 * slope) / (math.sqrt(1 + slope**2)))
                    image.line(xy=((x,y),(nextX,nextY)), fill="black", width=2)
                    x, y = (nextX - (4 / (math.sqrt(1 + slope**2))), nextY - (4 * slope) / (math.sqrt(1 + slope**2)))
        #if verticle line
        if startPt[0] == endPt[0]:
            #if pointing up
            if startPt[1] > endPt[1]:
                #draw triangle using 3 coords based on end point of line
                image.polygon([endPt, (endPt[0] + 8, endPt[1] + 8), (endPt[0] - 8, endPt[1] + 8)],fill=color ,outline="black")
            #pointing down
            else:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] - 8), (endPt[0] - 8, endPt[1] - 8)], fill=color, outline="black" )
        #if horiz line
        elif startPt[1] == endPt[1]:
            if startPt[0] > endPt[0]:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] + 8), (endPt[0] + 8, endPt[1] - 8)], fill=color, outline="black")
            else:
                image.polygon([endPt, (endPt[0] - 8, endPt[1] + 8), (endPt[0] - 8, endPt[1] - 8)], fill=color, outline="black")
        #not horiz or vert
        else:
            #determine slope of line
            slope = (endPt[1] - startPt[1]) / (endPt[0] - startPt[0])
            #line point towards the right direction
            if startPt[0] < endPt[0]:
                #fancy math to determing the coords of the triangle to draw based on line angle
                baseX, baseY = (endPt[0] - (8 / (math.sqrt(1 + slope**2))), endPt[1] - (8 * slope) / (math.sqrt(1 + slope**2))) 
                invSlope = -1/slope
                pt1x, pt1y = (baseX - (8 / (math.sqrt(1 + invSlope**2))), baseY - (8 * invSlope) / (math.sqrt(1 + invSlope**2))) 
                pt2x, pt2y = (baseX + (8 / (math.sqrt(1 + invSlope**2))), baseY + (8 * invSlope) / (math.sqrt(1 + invSlope**2)))
                #draw the triangle using coords above
                image.polygon([endPt, (pt1x,pt1y), (pt2x, pt2y)], fill=color, outline="black")     
            #line point towards the left direction
            else:
                baseX, baseY = (endPt[0] + (8 / (math.sqrt(1 + slope**2))), endPt[1] + (8 * slope) / (math.sqrt(1 + slope**2))) 
                invSlope = -1/slope
                pt1x, pt1y = (baseX - (8 / (math.sqrt(1 + invSlope**2))), baseY - (8 * invSlope) / (math.sqrt(1 + invSlope**2))) 
                pt2x, pt2y = (baseX + (8 / (math.sqrt(1 + invSlope**2))), baseY + (8 * invSlope) / (math.sqrt(1 + invSlope**2)))
                image.polygon([endPt, (pt1x,pt1y), (pt2x, pt2y)], fill=color, outline="black")

class aggLine(Strategy):
    """
    Aggregation line strategy 
    """
    def drawLine(self, image, startPt, endPt):
        """
        draws a solid line with a empty (white) square tip
        :param image: image to draw to  
        :param startPt: start point (x,y) for line 
        :param endPt: end point (x,y) for line 
        """
        #see comments from strategies above for implementation details       
        color = "white"
        image.line(xy=(startPt, endPt), fill="black", width=2)
        if startPt[0] == endPt[0]:
            if startPt[1] > endPt[1]:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] + 8), (endPt[0], endPt[1] + 16) ,(endPt[0] - 8, endPt[1] + 8)],fill=color ,outline="black")
            else:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] - 8), (endPt[0], endPt[1] - 16), (endPt[0] - 8, endPt[1] - 8)], fill=color, outline="black" )
        elif startPt[1] == endPt[1]:
            if startPt[0] > endPt[0]:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] + 8),(endPt[0] + 16, endPt[1]), (endPt[0] + 8, endPt[1] - 8)], fill=color, outline="black")
            else:
                image.polygon([endPt, (endPt[0] - 8, endPt[1] + 8),(endPt[0] - 16, endPt[1]), (endPt[0] - 8, endPt[1] - 8)], fill=color, outline="black")
        else:
            slope = (endPt[1] - startPt[1]) / (endPt[0] - startPt[0])
            if startPt[0] < endPt[0]:
                baseX, baseY = (endPt[0] - (8 / (math.sqrt(1 + slope**2))), endPt[1] - (8 * slope) / (math.sqrt(1 + slope**2))) 
                invSlope = -1/slope
                pt1x, pt1y = (baseX - (8 / (math.sqrt(1 + invSlope**2))), baseY - (8 * invSlope) / (math.sqrt(1 + invSlope**2))) 
                pt2x, pt2y = (baseX + (8 / (math.sqrt(1 + invSlope**2))), baseY + (8 * invSlope) / (math.sqrt(1 + invSlope**2)))
                pt3x, pt3y = (endPt[0] - (16 / (math.sqrt(1 + slope**2))), endPt[1] - (16 * slope) / (math.sqrt(1 + slope**2))) 
                image.polygon([endPt, (pt1x,pt1y), (pt3x, pt3y), (pt2x, pt2y)], fill=color, outline="black")     
            else:
                baseX, baseY = (endPt[0] + (8 / (math.sqrt(1 + slope**2))), endPt[1] + (8 * slope) / (math.sqrt(1 + slope**2))) 
                invSlope = -1/slope
                pt1x, pt1y = (baseX - (8 / (math.sqrt(1 + invSlope**2))), baseY - (8 * invSlope) / (math.sqrt(1 + invSlope**2))) 
                pt2x, pt2y = (baseX + (8 / (math.sqrt(1 + invSlope**2))), baseY + (8 * invSlope) / (math.sqrt(1 + invSlope**2)))
                pt3x, pt3y = (endPt[0] + (16 / (math.sqrt(1 + slope**2))), endPt[1] + (16 * slope) / (math.sqrt(1 + slope**2)))
                image.polygon([endPt, (pt1x,pt1y), (pt3x, pt3y), (pt2x, pt2y)], fill=color, outline="black")


class compLine(Strategy):
    """
    composite line stratedy
    """
    def drawLine(self, image, startPt, endPt):
        """
        draws a solid line with a filled (black) square tip
        :param image: image to draw to  
        :param startPt: start point (x,y) for line 
        :param endPt: end point (x,y) for line 
        """ 
        #see comments from strategies above for implementation details  
        color = "black"
        image.line(xy=(startPt, endPt), fill="black", width=2)
        if startPt[0] == endPt[0]:
            if startPt[1] > endPt[1]:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] + 8), (endPt[0], endPt[1] + 16) ,(endPt[0] - 8, endPt[1] + 8)],fill=color ,outline="black")
            else:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] - 8), (endPt[0], endPt[1] - 16), (endPt[0] - 8, endPt[1] - 8)], fill=color, outline="black" )
        elif startPt[1] == endPt[1]:
            if startPt[0] > endPt[0]:
                image.polygon([endPt, (endPt[0] + 8, endPt[1] + 8),(endPt[0] + 16, endPt[1]), (endPt[0] + 8, endPt[1] - 8)], fill=color, outline="black")
            else:
                image.polygon([endPt, (endPt[0] - 8, endPt[1] + 8),(endPt[0] - 16, endPt[1]), (endPt[0] - 8, endPt[1] - 8)], fill=color, outline="black")
        else:
            slope = (endPt[1] - startPt[1]) / (endPt[0] - startPt[0])
            if startPt[0] < endPt[0]:
                baseX, baseY = (endPt[0] - (8 / (math.sqrt(1 + slope**2))), endPt[1] - (8 * slope) / (math.sqrt(1 + slope**2))) 
                invSlope = -1/slope
                pt1x, pt1y = (baseX - (8 / (math.sqrt(1 + invSlope**2))), baseY - (8 * invSlope) / (math.sqrt(1 + invSlope**2))) 
                pt2x, pt2y = (baseX + (8 / (math.sqrt(1 + invSlope**2))), baseY + (8 * invSlope) / (math.sqrt(1 + invSlope**2)))
                pt3x, pt3y = (endPt[0] - (16 / (math.sqrt(1 + slope**2))), endPt[1] - (16 * slope) / (math.sqrt(1 + slope**2))) 
                image.polygon([endPt, (pt1x,pt1y), (pt3x, pt3y), (pt2x, pt2y)], fill=color, outline="black")     
            else:
                baseX, baseY = (endPt[0] + (8 / (math.sqrt(1 + slope**2))), endPt[1] + (8 * slope) / (math.sqrt(1 + slope**2))) 
                invSlope = -1/slope
                pt1x, pt1y = (baseX - (8 / (math.sqrt(1 + invSlope**2))), baseY - (8 * invSlope) / (math.sqrt(1 + invSlope**2))) 
                pt2x, pt2y = (baseX + (8 / (math.sqrt(1 + invSlope**2))), baseY + (8 * invSlope) / (math.sqrt(1 + invSlope**2)))
                pt3x, pt3y = (endPt[0] + (16 / (math.sqrt(1 + slope**2))), endPt[1] + (16 * slope) / (math.sqrt(1 + slope**2)))
                image.polygon([endPt, (pt1x,pt1y), (pt3x, pt3y), (pt2x, pt2y)], fill=color, outline="black")


    
