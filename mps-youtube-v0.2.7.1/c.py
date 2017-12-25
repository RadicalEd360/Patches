""" Module for holding colour code values. """

import os
import re
import sys

from . import config

if sys.stdout.isatty():
    #white = "\x1b[%sm" % 0
    #ul = "\x1b[%sm" * 3 % (2, 4, 33)
    #cols = ["\x1b[%sm" % n for n in range(91, 96)]

#    if config.COLOR1.get is "":
#        shead='32;3'
#    else:
#        shead='31;4'

    search_header='36;3'
    search_even='36;4'
    search_odd='0;4'

    playlist_header='32;3'
    playlist_even='32;4'
    playlist_odd='0;4'

	#------------------------------'ul'-'red'-'green'-'yell'-'blue'-'pink'-'whi'-'pls1'-'pls2'-'sch1'-'sch2'-'plhe'-'sehe'
    cols = ["\x1b[%sm" % n for n in ['32;3','31;1','32;1','33;1','36;1','35;1','0;1',playlist_odd,playlist_even,search_odd,search_even,playlist_header,search_header]]
    #red, green, yellow, blue, pink = cols
	#for new colors add name here, corresponds to numbers above
    ul, red, green, yellow, blue, pink, white, pls1, pls2, sch1, sch2, plhe, sehe = cols
else:
	#update later
    ul = red = green = yellow = blue = pink = white = ""

	#set shorthand for new colors
#r, g, y, b, p, w = red, green, yellow, blue, pink, white
	#pls1 playlist odd selections
r, g, y, b, p, w, p1, p2, s1, s2, ph, sh = red, green, yellow, blue, pink, white, pls1, pls2, sch1, sch2, plhe, sehe

ansirx = re.compile(r'\x1b\[\d*m', re.UNICODE)

def c(colour, text):
    """ Return coloured text. """
    #colours = {'r': r, 'g': g, 'y': y, 'b':b, 'p':p}
	#gives the ability to use the shorthands
    colours = {'r':r, 'g':g, 'y':y, 'b':b, 'p':p, 'p1':p1, 'p2':p2, 's1':s1, 's2':s2, 'ph':ph, 'sh':sh}
    return colours[colour] + text + w

def charcount(s):
    """ Return number of characters in string, with ANSI color codes excluded. """
    return len(ansirx.sub('', s))
