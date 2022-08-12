# Braille Chart Addon for NVDA

* Author: Travis Roth
* NVDA compatibility: 2022.2
* [Download brailleChart][1]

The Braille Chart addon for [NVDA][4] adds the feature to display a data series as a line graph on a refreshable Braille display. Note: this addon won't be useful without a Braille display.
Braille Chart is inspired by Tony Malykh's [audioChart][2] addon. And the [Accessible Graphs][3] project which demonstrates making a Braille chart on a Braille display.
Braile Chart may be used on any eight-dot refreshable Braille display. This reader recommends 40 cells or more for more optimal use. Your results may vary. The reader may consider constructing a representative sample of larger data sets to be of more use. For instance, drawing a 10,000 point Braille line chart is likely not useful. Braille Chart addon will do a one-to-one mapping of data points to Braille symbols, so it is up to the reader to construct a reasonable frequency sample.

## Commands
Select a range of data in either a row or column in Microsoft Excel.

* NVDA+b: display a Braille chart of the selected data
* (Note: NVDA uses this keystroke by default to read dialogs which I don't use in Excel. If you use it or have other conflicts, use NvDA's Input Gestures functionality to assign it to your preference. There are too many functions and addons for me to search for something that doesn't conflict with something else and is still pressable without 50 fingers.)
* Ctrl+Space: Built-in Excel keystroke to select an entire column. 
* Shift+Space: Built-in Excel keystroke to select an entire row.

## Explanation of the Braille
If you have tried the [Accessible Graphs][3] project this wwill be familiar to you. A symbol on the Braille display is used to mark a value range in the chart. Lower symbols in a cell are lesser values, and higher go higher.
This addon is designed around a typical eight dot Braille display. It uses 7 different segments. For instance, if a range has a minum of 10 and a maximum value of 80 each segment will represent 10 points of the graph (80-10)/7. The Braille representation follows: 

⣀⡠⠤⠔⠒⠊⠉

(Note: if the reader is reading this document with a screen reader and sppeech only Braille demonstrations in this document may not be read aloud unless the user explores character by character and queries for unicode values.)

In addition to the seven segment symbols illustrated on the above Braille line there are three downward right-slanting diagonals also used (dots 15, 26, 37). These are equal in value to their opposite counterparts and are used to make the Braille line prettier and to help indicate trend. The reader can tell if the value represented in the segment is trending up or down from the previous segment.

Example data: 10 20 30 40 50 60 80 65 45 25 15:

⣀⡠⠤⠔⠒⠊⠉⠑⠢⢄⣀

To further assist the reader in determining trends Braille Chart uses continuation single dots at the same level of a segment, with left side ones indicating an upward trending value and right side ones indicating a downtrend value. This is best illustrated by an example.
Consider the previous data series in which more values are interpolated inside each segment: 

10, 13, 18, 14, 20, 25, 24, 30, 35, 40, 50, 60, 80, 65, 45, 25, 15, 14

⣀⡀⡀⡀⡠⡠⢄⠤⠄⠔⠒⠊⠉⠑⠢⢄⣀⢀

Examine the last two cells of the chart. The first is dots 78 which indicates reaching the first or lowest valued segment. The next cell shows a dot 8 which indicates the next value (last value in our case) is also in the lowest segment and is a lesser value than the previous value that was the first one to move back into the lowest segment. 

Note: at this time segments that use the diagonals do not use continuation dots but still indicate trend. Notice how 25 to 24 is represented as the diagonal for 24 reverses direcvtion. 

Finally, as a convenience for orientation Braille Chart inserts a full Braille symbol in the middle of the chart to indicate the middle and at the end of the line. This may also help reorient the reader to the level of the segment symbols. For example with included orientation markers: 

⣀⡀⡀⡀⡠⡠⢄⠤⠄⣿⠔⠒⠊⠉⠑⠢⢄⣀⢀⣿


[1]: https://github.com/travisroth/brailleChart/releases/download/0.1/brailleChart-0.1.nvda-addon

[2]: https://addons.nvda-project.org/addons/AudioChart.en.html

[3]: https://accessiblegraphs.org/

[4]: https://www.nvaccess.org/
