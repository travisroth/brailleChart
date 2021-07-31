# -*- coding: UTF-8 -*-
#brailleChart for Excel
#Copyright (C) 2021 Travis Roth
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

#make the braille chart output

from  .symbols import braillePatterns, brailleSymbol

class Line:
  def __init__(self, rawData, description=None, minValue=None, maxValue=None):
    self.rawData = rawData
    self.yData = []
    if type(rawData)==str: self.yData = [float(idx) for idx in rawData.split() if idx] #if csv has empty line at end get '' so the if returns false not adding it
    elif type(rawData)==list: self.yData = [float(idx) for idx in rawData if idx] #if csv has empty line at end get '' so the if returns false not adding it
    self.description = description
    if not minValue: self.minValue = min(self.yData) 
    else: self.minValue = minValue 
    if not maxValue: self.maxValue = max(self.yData)  
    else: self.maxValue = maxValue 
    self.segments = 7
    self.range = (self.maxValue-self.minValue)  
    self.size =  self.range/self.segments
    self.line = []
    self.brailleLine = ''
    self.graphLine() 


  def graphLine(self ):
    # first value is a one off nothing to ascend from
    self.line.append( int( ((self.yData[0]-self.minValue)/self.size) ) )
    if self.yData[0] == self.maxValue: self.line[0] = self.segments-1 #a division bug hard hackign
    trailing = 0
    for i in self.yData[1:]: 
      x = int( ((i-self.minValue)/self.size) )  
      if (self.yData[trailing] >= i) and (self.line[-1]==x or self.line[-1]==(x+10) or self.line[-1]==(x+20)): 
        x = x+20
      elif (self.yData[trailing] < i) and (self.line[-1]==x or self.line[-1]==(x+10) or self.line[-1]==(x+20)):
        x = x + 10
      elif i == self.maxValue:
        x = self.segments-1 #getting the 7 segment when max hit, bug, hard hacking
      #the diagonals have only 2 symbols the flats have 3, copensated for the 3
      #but means whenever go to a lower diag segment will show increasing
      if (x==1 or x==3 or x==5) and (i<self.yData[trailing]): x = x+20
      trailing = trailing + 1
      self.line.append(x)
      #endFor
    #encoding
    #print(line[8], line[9]) 
    brailleLine = ""
    for i in self.line: brailleLine = brailleLine + brailleSymbol(i)
    #add marker for orientation
    #brailleLine = brailleLine + braillePatterns['12345678']
    marker = int(len(brailleLine)/2)
    brailleLine = brailleLine[:marker] + braillePatterns['12345678'] + brailleLine[marker:] + braillePatterns['12345678']    
    self.brailleLine = brailleLine   

  def getBraille(self):
    return self.brailleLine
  
  def getMax(self):
    return self.maxValue
  
  def getMin(self):
    return self.minValue

  def getDescription(self):
    return self.Description

  def getSegmentSize(self):
    return self.size 
  
  def getRange(self):
    return self.range 
  
#a = [0,1,2,3,4,5,6,7,8,9]
#print (a)
#print (graphLine(a))
#b = [339.5, 341, 346.25, 352, 359.25, 340]
       
#cz20 = [float(i) for i in cz20.split()]
#print(cz20)
#print (cz20[8], cz20[9])

if __name__ == "__main__":
  import sys
  fileName = sys.argv[1]
  data = []
  with open(fileName, 'r') as file:
  #with open(fileName, 'r', encoding="utf-8") as file:
    data = file.read().splitlines()
  l = Line(data)
  print ("Min: ", l.getMin())
  print ("Max: ", l.getMax()) 
  print("Range: ", l.getRange())
  print ("Segment size: ", l.getSegmentSize())
  print (l.getBraille())
