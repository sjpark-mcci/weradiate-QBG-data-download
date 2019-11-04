#
# Module: json-to-csv-qbg.py
#
# Function:
#	Convert sensor data from a JSON file to CSV for QBG
#
# Copyright:
#	See LICENSE file.
#
# Author:
#	Sungjoon Park, MCCI Corporation
#
# Description:
#	This function convert data from an influxdb JSON file generated
#	from the WeRadiate data set for a given sensor to a CSV file.

import json
import csv
import argparse

# get input/output files from user
parser = argparse.ArgumentParser()
parser.add_argument("inputjson")
parser.add_argument("outputcsv")
args = parser.parse_args()

# open json file and parse
with open(args.inputjson, 'r') as data_qbg:
    data_qbg_parsed = json.load(data_qbg)
qbg_data = data_qbg_parsed['results'][0]['series'][0]

# open a file for writing
qbg_file_data = open(args.outputcsv, 'w')

# create the csv writer object
csvwriter = csv.writer(qbg_file_data, lineterminator='\n')

# write headers
csvwriter.writerow(qbg_data['columns'])

# wrtie values
for qbg in qbg_data['values']:
    csvwriter.writerow(qbg)
qbg_file_data.close()


