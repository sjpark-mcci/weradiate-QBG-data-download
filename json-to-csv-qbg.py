#
# Module: json-to-csv-qbg.py
#
# Function:
#	Extract sensor data from a JSON file as CSV for QBG
#
# Copyright:
#	See LICENSE file.
#
# Author:
#	Sungjoon Park, MCCI Corporation
#
# Description:
#	This function extracts data from an influxdb JSON file generated
#	from the WeRadiate data set for a given sensor.

import json
import csv

# open json file and parse
with open('data-qbg.json', 'r') as data_qbg:
    data_qbg_parsed = json.load(data_qbg)
qbg_data = data_qbg_parsed['results'][0]['series'][0]

# open a file for writing
qbg_file_data = open('QBG-Data.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(qbg_file_data, lineterminator='\n')

# write headers
csvwriter.writerow(qbg_data['columns'])

# wrtie values
for qbg in qbg_data['values']:
    csvwriter.writerow(qbg)
qbg_file_data.close()


