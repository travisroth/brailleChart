# -*- coding: UTF-8 -*-
#brailleChart for Excel
#Copyright (C) 2021 Travis Roth
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

# chart Symbols
# Braille patterns: https://en.wikipedia.org/wiki/Braille_Patterns

braillePatterns = {'blank': u'\u2800',
                   '1': u'\u2801',
                   '2': u'\u2802',
                   '12': u'\u2803',
                   '3': u'\u2804',
                   '13': u'\u2805',
                   '23': u'\u2806',
                   '123': u'\u2807',
                   '4': u'\u2808',
                   '14': u'\u2809',
                   '24': u'\u280A',
                   '34': u'\u280C',
                   '5': u'\u2810',
                   '15': u'\u2811',
                   '25': u'\u2812',
                   '35': u'\u2814',
                   '6': u'\u2820',
                   '26': u'\u2822',
                   '36': u'\u2824',
                   '7': u'\u2840',
                   '76': u'\u2860',
                   '8': u'\u2880',
                   '38': u'\u2884',
                   '78': u'\u28C0',
                   "4568": u'\u28B8',
                   "12345678": u'\u28FF'
  }

def brailleSymbol(segment):
  # returns a segment indicator
  dots = braillePatterns["blank"]
  #base+10 is uptrend, base+20 is down, 0-6 are mapped to the math calculations
  if segment == 0: dots = braillePatterns['78']
  if segment == 10: dots = braillePatterns['7']
  if segment == 20: dots = braillePatterns['8']
  if segment == 1: dots = braillePatterns['76']
  if segment == 11: dots = braillePatterns['76']
  if segment == 21: dots = braillePatterns['38']
  if segment == 2: dots = braillePatterns['36']
  if segment == 12: dots = braillePatterns['3']
  if segment == 22: dots = braillePatterns['6']
  if segment == 3: dots = braillePatterns['35']
  if segment == 13: dots = braillePatterns['35']
  if segment == 23: dots = braillePatterns['26']
  if segment == 4: dots = braillePatterns['25']
  if segment == 14: dots = braillePatterns['2']
  if segment == 24: dots = braillePatterns['5']
  if segment == 5: dots = braillePatterns['24']
  if segment == 15: dots = braillePatterns['24']
  if segment == 25: dots = braillePatterns['15']
  if segment == 6: dots = braillePatterns['14']
  if segment == 16: dots = braillePatterns['1']
  if segment == 26: dots = braillePatterns['4']
  return dots
 
