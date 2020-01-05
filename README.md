# Data download from InfluxDB and file conversion for WeRadiate

### Software Requirement
- Ubuntu(For PC) - you can follow the installation instruction from here: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0
- Python - you can download from here: https://www.python.org/downloads/
### Instruction
1. Download or clone this repository to desired directory
2. Launch Ubuntu terminal from PC(refer to the above link) or Terminal from Mac.
	- To open terminal from Mac, either open your Applications folder, then open Utilities and double-click on Terminal, or press Command - spacebar to launch Spotlight and type "Terminal," then double-click the search result.
3. In the terminal, go to the directory where you downloaded(if you downloaded as a zip file, it needs to be extracted in the same folder) or cloned this repository
- For example, if the repository is cloned under `c:/client/windsor/sandbox/weradiate-QBG-data-download`,
```
sjpark@sjpark-note2:~$ cd /mnt/c/client/windsor/sandbox/weradiate-QBG-data-download
sjpark@sjpark-note2:/mnt/c/client/windsor/sandbox/weradiate-QBG-data-download$ ls
QBG-Data.csv  data-qbg-test.json  data.csv   data3.csv   get-influxdb-data-qbg.sh  qbg-data-test.csv   qbgdata.csv
README.md     data-qbg.json       data.json  data3.json  json-to-csv-qbg.py        qbg-data-test2.csv  qbgrawdata.json
sjpark@sjpark-note2:/mnt/c/client/windsor/sandbox/weradiate-QBG-data-download$
```
4. Download raw data as a json file from InfluxDB using `get-influxdb-data-qbg.sh`
- Basic option for getting raw data,
	- '-r [probe]' for selecting probe(default is 1a)
		- Probe options: 1a, 3a, 5a, 1b, 3b, 5b
	- '-t [days]' for number of days from today.
- Syntax 
	- PC: `./get-influxdb-data-qbg.sh -r [probe] -t [days] > [output file name].json`
	- Mac: `sh get-influxdb-data-qbg.sh -r [probe] -t [days] > [output file name].json`
- Example 1: get the last 5 days of data from probe 1a

\
PC
```
$ ./get-influxdb-data-qbg.sh -r 1a -t 5 > rawdata-1a.json
Enter host password for user 'ezra':
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    77    0    77    0     0    167      0 --:--:-- --:--:-- --:--:--   168
```

Mac
```
$ sh get-influxdb-data-qbg.sh -r 1a -t 5 > rawdata-1a.json
Enter host password for user 'ezra':
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    77    0    77    0     0    167      0 --:--:-- --:--:-- --:--:--   168
```

You will need to enter proper password to get the data. Also, for this example, this will create `rawdata-1a.json` file in the same directory

5. Convert a .json raw data file to a csv file using `json-to-csv-qbg.py`
- Syntax 
	- PC: `python3 json-to-csv-qbg.py [input file].json [output file].csv`
	- Mac: `python json-to-csv-qbg.py [input file].json [output file].csv`

	`[input file].json` is the json file that has been created in the previous step.
- Example 1: get the last 5 days of data from probe 1a

\
PC
```
$ python3 json-to-csv-qbg.py rawdata-1a.json csvfile-1a.csv
```

Mac
```
$ python json-to-csv-qbg.py rawdata-1a.json csvfile-1a.csv
```

For this example, this will create `csvfile-1a.csv` file in the same directory.
