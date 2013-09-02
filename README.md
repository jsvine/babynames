# Baby Name Data Fetcher

This repo contains CSVs of the [Social Security Administration's baby-name data](http://www.ssa.gov/oact/babynames/limits.html), as well as Python scripts for updating this data.

## The Data

- [births.csv](data/births.csv): A direct transcription of the SSA's ["Number of Social Security card holders born in the U. S. by year of birth and sex"](http://www.ssa.gov/oact/babynames/numberUSbirths.html) table.

- [name-counts.csv](data/name-counts.csv): The [number of babies registered with each name](http://www.ssa.gov/oact/babynames/limits.html), by year and sex. For privacy reasons, the SSA only lists names with at least five occurrences. 

- [babynames.csv.bz2](data/babynames.csv.bz2): a compressed file containing the data in [name-counts.csv](data/name-counts.csv), plus the proportion of births each row accounts for, based on [births.csv](data/births.csv). By default, this data is limited to the top 1,000 names per year for each sex. (See below if you'd like a different threshold.) If you want to do basic analysis on baby names, this is probably the file you want to use.

## The Scripts

- [fetch-births.py](bin/fetch-births.py): A basic web-scraper to turn [this table](http://www.ssa.gov/oact/babynames/numberUSbirths.html) into a CSV file.

- [fetch-name-counts.py][bin/fetch-name-counts.py]: Extracts all files from the SSA's [national baby names ZIP file](http://www.ssa.gov/oact/babynames/limits.html) and combines the data into a single CSV.

- [combine-data.py](bin/combine-data.py): For each year/sex/name combination, calculates the proportion it represents of all births for that year and sex, using the datasets fetched by the two scripts above. By default, outputs only the top 1,000 names for each year/sex. To generate a file with a different threshold, pass that number as the first command line argument to the script. E.g.:

    ./bin/combine-data.py 2000 > data/top2000.csv

