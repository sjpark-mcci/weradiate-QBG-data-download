# This repository is for data download for WeRadiate

-example command

sjpark@sjpark-note2:/mnt/c/client/windsor/sandbox/weradiate-QBG-data-download$ ./get-influxdb-data-qbg.sh -r 3a -t 5 -v > data-qbg.json
get-influxdb-data-qbg.sh: curl -G --basic --user ezra https://analytics.weradiate.com/influxdb:8086/query?pretty=true --data-urlencode db=thermosense --data-urlencode q=SELECT mean("tWater")*9/5+32 as "tWater" from "compost" where "deviceid" = 'device-02-6d' AND time > now() - 5d GROUP BY time(1ms) fill(none) tz('America/New_York')
Enter host password for user 'ezra':
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3153    0  3153    0     0  18547      0 --:--:-- --:--:-- --:--:-- 18656
sjpark@sjpark-note2:/mnt/c/client/windsor/sandbox/weradiate-QBG-data-download$ python3 json-to-csv-qbg.py