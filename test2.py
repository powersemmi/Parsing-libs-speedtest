#!/bin/env python3.11
from pathlib import Path

from lxml import html

data = Path("test.html").read_text()

for _ in range(100000):
    root = html.fromstring(data)
    res = root.xpath("//ul/li/text()")
