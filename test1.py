#!/bin/env python3.11
from pathlib import Path

from bs4 import BeautifulSoup

data = Path("test.html").read_text()

for _ in range(100000):
    soup = BeautifulSoup(data, "html.parser")
    res = [i.string for i in soup.select("li")]
