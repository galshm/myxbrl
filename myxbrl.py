import os
import sys
from xbrl import XBRLParser
from xbrl import GAAP
from xbrl import GAAPSerializer
from xbrl import DEISerializer
from xbrl import XBRLParserException
import string

xbrl_parser = XBRLParser(0)
#xbrl_result = xbrl_parser.parse(os.file("./X1560963.xbrl"))
xbrl_result = xbrl_parser.parse("./X1560963.xbrl")


