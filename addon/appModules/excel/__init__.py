# -*- coding: UTF-8 -*-
#appModules/excel.py
#brailleChart for Excel
#Copyright (C) 2021 Travis Roth
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

import scriptHandler
from scriptHandler import getLastScriptRepeatCount, script
import api
import controlTypes
import ctypes
#some imports are left from Tony's audioCharts addon for creating GUI that may be needed of rfuture enhancements
#import gui
#from gui import guiHelper
#import wx
import NVDAHelper
from NVDAObjects.window import excel as excelWindow #resolve a name conflict with importing nvdaBuiltin.appModules.excel 
import ui
import config
from nvdaBuiltin.appModules import excel

import addonHandler

from .line import Line 

addonHandler.initTranslation()
ADDON_SUMMARY = addonHandler.getCodeAddon ().manifest["summary"]
#confspec = {
#  'testCasePath': 'string(default="")',
#}
#config.conf.spec["brailleChart"] = confspec

max_rows = 80 # Tony's collectValues addon sets this constant for convenience when no selection selects A1+max_rows 

class AppModule(excel.AppModule):
  scriptCategory = ADDON_SUMMARY
  #scriptCategory = "Braille Chart"
  
  def __init__(self,*args,**kwargs):
    super(AppModule,self).__init__(*args,**kwargs)
    #
    
  @script(description='Draw Braille chart.', gestures=['kb(desktop):nvda+b', 
      'kb(laptop):nvda+b'])
  def script_brailleChart(self, gesture):
    count=scriptHandler.getLastScriptRepeatCount()
    if count >= 2:
      return
    values = self.collectValues()
    if values is None:
      return
    if count == 0:
      #display the chart and info in browseable message
      chart = Line(values) 
      chartText = chart.getBraille() + "\n"
      #Translators: segment size (the quantity of the total range each Braille mark represents)
      chartText = chartText + _("Segment size: ") + str(chart.getSegmentSize()) + "\n"
      #Translators: Minimum value
      chartText = chartText + _("Min: ") + str(chart.getMin()) + "\n"
      #Translators: maximum value
      chartText = chartText + _("Max: ") + str(chart.getMax()) + "\n"
      #Translators: title of chart's browseableMessage
      ui.browseableMessage(chartText, _("Braille Chart") )  
    else:
      #self.showCalibrationDialog(values) #todo: decide if need settings
      return 

  def collectValues(self):
    # this function borrowed from AudioChart addon 
    #A part of the AudioChart addon for NVDA
    #Copyright (C) 2018 Tony Malykh
    focus = api.getFocusObject()
    values = []
    if isinstance(focus, excelWindow.ExcelSelection):
      colspan = focus._get_colSpan()
      rowspan = focus._get_rowSpan()
      if (colspan != 1) and (rowspan != 1):
        # Translators: Message when more than one column and more than 1 row is selected
        ui.message(_("Please select only a single column or a single row."))
        return None
      excelValues = focus.excelRangeObject.Value()
      for evTuple in excelValues:
        for ev in evTuple:
          try:
            values.append(float(ev))
          except:
            continue
      if len(values) == 0:
        # Translators: message when no numeric cells found within selected range
        ui.message(_("No numeric values found within the selection."))
        return None
    elif isinstance(focus, excelWindow.ExcelCell):
      excelValues = focus.excelCellObject.Range("A1", "A%d" % max_rows).Value()
      for evTuple in excelValues:
        try:
          ev = evTuple[0]
          values.append(float(ev))
        except:
          break
      if len(values) == 0:
        # Translators: message when currently selected cell doesn't contain a numeric value
        ui.message(_("Please select a numeric value - the beginning of time series."))
        return None
    else:
      # Translators: message when called not in Excel worksheet
      ui.message(_("Braille chart currently only works inMicrosoft Excel."))
      return None
    return values
    
