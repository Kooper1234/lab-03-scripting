#!/bin/bash
set -euo pipefail

curl -o lab3-bundle.tar.gz https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz            

tar -xzf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3-bundle.tar.gz > cleaned.tzv

tr '\t' ',' < cleaned.tsv > cleaned.csv

ROWS=$(( $(wc -l < cleaned.csv) - 1 ))
echo "Data rows remaining: $ROWS"

tar -czf converted-archive.tar.gz cleaned.csv
