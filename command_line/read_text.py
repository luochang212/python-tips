"""usage1: cat info.txt | python read_text.py
   usage2: echo "hello" | python read_text.py
   usage3: python gen_text.py | python read_text.py
"""

import sys

for line in sys.stdin:
    line = line.strip()
    print(line + '......ok')
