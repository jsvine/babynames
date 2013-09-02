LIMIT=1000
default: births counts combined

births:
	./bin/fetch-births.py > data/births.csv

counts:
	./bin/fetch-name-counts.py > ./data/name-counts.csv

combined:
	./bin/combine-data.py $(LIMIT) | bzip2 -c > ./data/babynames.csv.bz2
