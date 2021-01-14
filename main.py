#!/usr/bin/env python3

import csv
from pathlib import Path
import codecs
import requests

CWD = Path.cwd()
CSV_DIR = CWD.joinpath('csv')
OUTPUT_DIR = CWD.joinpath('output')

ENCODINGS = ["utf8", "cp1252"]

DATA = []


def get_all_csv_paths():
    return [f for f in CSV_DIR.iterdir() if f.suffix == '.csv']


def read_csv_to_data(fn):
    for encoding in ENCODINGS:
        with codecs.open(fn, encoding=encoding, errors='replace') as csv_file:
            for row in csv.reader(csv_file, delimiter=','):
                item = row[0] = {
                    'date': row[1],
                    'comment': row[2],
                    'url': row[3]
                }
                DATA.append(item)


def save_all_urls():
    for item in DATA:
        # Get save location
        local_filename = item['url'].split('/')[-1]
        destination = OUTPUT_DIR.joinpath(local_filename)

        # TODO Make request


csv_files = get_all_csv_paths()
_ = [read_csv_to_data(f) for f in csv_files]

save_all_urls()
