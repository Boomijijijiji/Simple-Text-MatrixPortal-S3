#MATRIXPORTAL S3 with ADAFRUIT 64x32 with 3mm pitch RGB BOARD and CIRCUITPYTHON 9.0x
# SPDX-License-Identifier: MIT

import os
import time
import board
import terminalio #Alternative to adafruit_bitmap_font
from adafruit_bitmap_font import bitmap_font
from adafruit_matrixportal.matrixportal import MatrixPortal
#import adafruit_requests


#INPUTS-INPUTS-INPUTS-INPUTS-INPUTS-INPUTS

    #INPUT ---- TEXT COLOR SELECTION
text_color_TopLine = 0xFF0000           # Some choices: 0x4b0082 INDIGO / 0xFF0000 RED / 0xFFFFFF WHITE / 0x00FF00 LIME / 0xF1C232 SAFFRON / 0xFF00FF FUSCHIA / 0x0000FF BLUE
text_color_SecondLine = 0xFFFFFF        # https://www.htmlcsscolor.com/ for more hex 0x..... color ideas
text_color_ThirdLine = 0x0000FF

    #INTPUT ----- FONT SELECTION
        #DEFAULT is TERMINALIO for EQUADISTANT LINES ON 64x32 RGB MATRIX BASED ON TERMINALIO.FONT
font_location = "fonts/6x10.bdf"         #Choose the .pcf or .bdf file from the device FONT folder
text_font_choice=terminalio.FONT         # Choose either 'terminalio.FONT' OR 'font_location'. font_location will lookup to file in font folder on S3 shown on line above.

    #INTPUT ----- TEXT
text_TopLine = ("ABCDEFGHIJ")
text_SecondLine = ("KLMNOPQRST")
text_ThirdLine = ("UVWXYZ1234")

#END OF INPUTS




# ----------- Display setup -----------
time_interval = 100000
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True)

#First Top Line Info
TopLine_header_text_area = matrixportal.add_text(
                            text_font=text_font_choice,
                            text_position=(2, (matrixportal.graphics.display.height // 5.0) - 1),
                            text=text_TopLine,
                            text_color=text_color_TopLine,
                            )

#Second Line Info
SecondLine_header_text_area = matrixportal.add_text(
                            text_font=text_font_choice, #terminalio.font #change font_file to terminalio.font for terminalio or font_file for adafruit_bitmap_font
                            text_position=(2, (matrixportal.graphics.display.height // 1.8) - 1),
                            text=text_SecondLine,
                            text_color=text_color_SecondLine,
                            )

#Third Line Info
ThirdLine_header_text_area = matrixportal.add_text(
                            text_font=text_font_choice, #terminalio.font #change font_file to terminalio.font for terminalio or font_file for adafruit_bitmap_font
                            text_position=(2, (matrixportal.graphics.display.height // 1.12) - 1),
                            text=text_ThirdLine,
                            text_color=text_color_ThirdLine,
                            )

time.sleep(time_interval)
