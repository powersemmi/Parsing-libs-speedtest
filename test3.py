#!/bin/env python3.11
from pathlib import Path

import jmespath
import xmltodict

data = "<root>\n%s</root>" % Path("test.html").read_text().replace(
    "<!doctype html>\n", ""
)
ex = jmespath.compile("root.body.main.ul.li")

for _ in range(100000):
    val = xmltodict.parse(data)
    res = ex.search(val)
