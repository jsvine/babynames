#!/usr/bin/env python
import pandas as pd
import sys

BIRTHS_FILE = "data/births.csv"
COUNTS_FILE = "data/name-counts.csv"

# By default, only return the top 1000 names.
# This can be overriden by passing a different
# threshold as the first command line argument
# to the script.
DEFAULT_LIMIT = 1000
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_LIMIT

# Read and reshape the annual births data
births = pd.read_csv(BIRTHS_FILE).set_index("year").stack()
births.index.names = [ "year", "sex" ]
births.name = "overall_count"

# Read the name-counts data
counts = pd.read_csv(COUNTS_FILE).set_index(["year", "sex"])

# Select only the top n names
def top_n(df, n):
    grouped = df.groupby(df.index)
    top = grouped.apply(lambda x: x[:n])
    return top.reset_index(level=0, drop=True)

top_counts = top_n(counts, LIMIT)

# Join the two datasets and calculate each name's share
names = top_counts.join(births)
names["prop"] = names["count"] * 1. / names["overall_count"]

# Write as a CSV to stdout
names[["name", "count", "prop"]].to_csv(sys.stdout)
