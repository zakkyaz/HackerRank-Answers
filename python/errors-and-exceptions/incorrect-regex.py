import sys
import re
    
lines = [line.strip() for line in sys.stdin]

for regex in lines[1:]:
    try:
        re.compile(regex)
        print(True)
    except re.error:
        print(False)
