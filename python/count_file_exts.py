#!/usr/bin/env python

import os
from collections import Counter
from pprint import pprint

lst = []
for file in os.listdir('./'):
        name, ext = os.path.splitext(file)
        lst.append(ext)

pprint(Counter(lst))
