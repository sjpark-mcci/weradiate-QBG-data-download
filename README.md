# Data download from InfluxDB and file conversion for WeRadiate

There are mainly two parts:
1. raw data download as json file (get-influxdb-data-qbg.sh)
2. convert json file to csv file (json-to-csv-qbg.py)

Please get the raw data first then use python file to convert the json file to csv file.

For the basic option for getting raw data,
'-r [probe]' for selecting probe(default is 1a) and 't [days]' for number of days from today.

Probe options are: 1a, 3a, 5a, 1b, 3b, 5b
## Example commands

### shell scrip to download raw data in json form

To fetch the last 36 days from default source and
	series, do the following. (The -v option causes the script to display
	the curl command.)

	$ get-influxdb-data-qbg.sh -v -t36 > data.json
	get-influxdb-data-qbg.sh: curl -G --basic --user ezra https://analytics.weradiate.com/influxdb:8086/query?pretty=true --data-urlencode db=thermosense --data-urlencode q=SELECT mean("tWater")*9/5+32 as "tWater" from "compost" where "deviceid" = 'device-02-6a' AND time > now() - 36d GROUP BY time(1ms) fill(none) tz('America/New_York')
	Enter host password for user 'ezra':
  	% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	100 29977    0 29977    0     0  92236      0 --:--:-- --:--:-- --:--:-- 93096

To get water temperature, pressure and battery data for sensor probe 5a for the last 7 days:

	$ get-influxdb-data-qbg.sh -q 'mean("tWater")*9/5+32 as "tWater",mean("p") as "p",mean("vBat") as "vBat"' -r 5a -v -t7 > data.json
	get-influxdb-data-qbg.sh: curl -G --basic --user ezra https://analytics.weradiate.com/influxdb:8086/query?pretty=true --data-urlencode db=thermosense --data-urlencode q=SELECT mean("tWater")*9/5+32 as "tWater",mean("p") as "p",mean("vBat") as "vBat" from "compost" where "deviceid" = 'device-02-6e' AND time > now() - 7d GROUP BY time(1ms) fill(none) tz('America/New_York')
	Enter host password for user 'ezra':
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	100  6509    0  6509    0     0  47166      0 --:--:-- --:--:-- --:--:-- 47510

Note: 'sh get-influxdb-data-qbg.sh ....' for MAC bash

### python command to convert json file to csv file
    $ python3 json-to-csv-qbg.py data.json data.csv

Note: You can just use python instead of python3 as well