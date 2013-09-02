#!/usr/bin/env python
import requests
from StringIO import StringIO
import zipfile
import sys

# Download the SSA zip file
sys.stderr.write("Downloading zipfile...\n")
SSA_URL = "http://www.ssa.gov/oact/babynames/names.zip"
ssa_content = requests.get(SSA_URL).content

# Extract the zip file
sys.stderr.write("Extracting zipfile...\n")
ssa_zip = zipfile.ZipFile(StringIO(ssa_content))

# Get all the text files, in order
# (Skips over the readme PDF.)
txt_files = [ fname for fname in sorted(ssa_zip.namelist())
    if fname[-3:] == "txt" ]

# Given a filename, extract the data and 
# prepend the birth year
def extract_from_filename(filename):
    year = filename[3:7]
    with ssa_zip.open(filename) as f:
        data = f.read().split("\n")
        prepended = ("%s,%s" % (year, line)
            for line in data if line)
        return "\n".join(prepended)

extracted = map(extract_from_filename, txt_files)

# Write the concatenated files to a CSV
sys.stderr.write("Writing data...\n")
header = "year,name,sex,count\n"
csv = header + "\n".join(extracted)
print csv
