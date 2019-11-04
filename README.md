# Data download from InfluxDB and file conversion for WeRadiate

## example commands

### shell scrip to download raw data in json form
sjpark@sjpark-note2:/mnt/c/client/windsor/sandbox/weradiate-QBG-data-download$ ./get-influxdb-data-qbg.sh -r 5a
 -t 4 -v > qbgrawdata.json
get-influxdb-data-qbg.sh: curl -G --basic --user ezra https://analytics.weradiate.com/influxdb:8086/query?pretty=true --data-urlencode db=thermosense --data-urlencode q=SELECT mean("tWater")*9/5+32 as "tWater" from "compost" where "deviceid" = 'device-02-6e' AND time > now() - 4d GROUP BY time(1ms) fill(none) tz('America/New_York')
Enter host password for user 'ezra':
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2673    0  2673    0     0   7815      0 --:--:-- --:--:-- --:--:--  7815

### python command to convert json file to csv file
sjpark@sjpark-note2:/mnt/c/client/windsor/sandbox/weradiate-QBG-data-download$ python3 json-to-csv-qbg.py qbgra
wdata.json qbgdata.csv