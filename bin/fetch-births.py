#!/usr/bin/env python
import requests
import lxml.html

# Fetch page and parse HTML
SSA_URL = "http://www.ssa.gov/oact/babynames/numberUSbirths.html"
ssa_text = requests.get(SSA_URL).text
ssa_dom = lxml.html.fromstring(ssa_text)

# Extract relevant HTML
table = ssa_dom.cssselect("table.border")[0]
rows = table.cssselect("tr")[1:]

# Parse all but the last column
parse_cell = lambda cell: cell.text.replace(",", "")
parse_row = lambda row: map(parse_cell, row.cssselect("td")[:-1])
data = map(parse_row, rows)

header = [[ "year", "M", "F" ]]
csv = "\n".join(",".join(line) for line in header + data)

print csv
