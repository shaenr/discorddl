#!/usr/bin/env python3

import csv
import codecs
import requests
from pathlib import Path
import subprocess
import sys
import os


CWD = Path.cwd()
CSV_DIR = CWD.joinpath('csv')
OUTPUT_DIR = CWD.joinpath('output')
EXECONCE = CWD.joinpath('executeonce.txt')

ENCODINGS = ["utf8", "cp1252"]

DATA = []

CHUNK_SIZE = 1024


def init_dirs(dirs: list):
    for d in dirs:
        d.mkdir(exist_ok=True)


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


def install(install_check: Path):
    if not install_check.exists():
        return
    else:
        if os.name == 'nt':
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', 'virtualenv'], check=True)
                subprocess.run([r'.\venv\Scripts\activate.bat'], check=True)
                subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
            except FileNotFoundError as e:
                print(e)
        else:
            subprocess.run(['bash', 'install_linux.sh'], check=True)

        install_check.unlink()


def reinitialize_executeonce(install_check: Path):
    if not install_check.exists():
        with install_check.open('w') as fo:
            fo.write()


def save_all_urls():
    failed_urls = []
    for item in DATA:
        url = item['url']
        if url == 'Attachments':
            continue

        # Get save location
        local_filename = url.split('/')[-1]
        destination = OUTPUT_DIR.joinpath(local_filename)

        # Check if file already exists
        if not destination.exists():
            print(f"Requesting {url}")
            try:
                r = requests.get(url, stream=True)
                r.raise_for_status()
                print(f"Response Code: {r.status_code}")

                if r.status_code == 200:
                    with open(destination, 'wb') as f:
                        print(f"Writing {local_filename} by chunk: {CHUNK_SIZE}")
                        for chunk in r.iter_content(CHUNK_SIZE):
                            f.write(chunk)
                    print(f"Saved {url} to\n\t{destination}")

            except requests.exceptions.MissingSchema as e:
                print(f"ERROR: {e}\nFailed on {url}")
                failed_urls.append(url)
                continue

    if failed_urls:
        print("Failed on these:")
        print(failed_urls)


init_dirs([CSV_DIR, OUTPUT_DIR])
install(EXECONCE)

csv_files = get_all_csv_paths()
_ = [read_csv_to_data(f) for f in csv_files]

save_all_urls()

print(f"Saved files to: {OUTPUT_DIR}")