# Couchbase Command Line Interface Tool

## Prerequisites:
-Install Couchbase Server<br/>
-Install Couchbase Python SDK (3.0)<br/>
-dotenv

## Description
Takes in one command line argument as the query that you want to run and runs it against the predefined bucket. In this case, the bucket is the travel-sample data. <br/>
The tool handles transient exceptions and retries them at adjustable number of retries and delays before each retry. 

## How to Use:
Here are some examples of how to use the tool. I recommend to use single quotes (') to specify argument as it leads to less issues with the escaped (\`) in the command line. 

### Example 1:
```
python3 query_tool.py 'SELECT VALUE t.name FROM `travel-sample` t WHERE t.country = "United States" AND t.name IS NOT NULL LIMIT 25;'
```
Returns:
```
Running: SELECT VALUE t.name FROM `travel-sample` t WHERE t.country = "United States" AND t.name IS NOT NULL LIMIT 25;
40-Mile Air
Texas Wings
Atifly
Locair
SeaPort Airlines
Alaska Central Express
AirTran Airways
U.S. Air
PanAm World Airways
Bemidji Airlines
Bering Air
Air Cargo Carriers
CBM America
Black Stallion Airways
Trans Pas Air
Cape Air
Usa Sky Cargo
Era Alaska
Hankook Air US
Orbit Airlines
Chautauqua Airlines
XOJET
Orbit International Airlines
Orbit Regional Airlines
Orbit Atlantic Airways
Found 25 row(s)
```

### Example 2:
```
python3 query_tool.py 'SELECT VALUE t.name FROM `yelp` t WHERE t.country = "United States" AND t.name IS NOT NULL LIMIT 25;'
```
Returns:
```
Running: SELECT VALUE t.name FROM `yelp` t WHERE t.country = "United States" AND t.name IS NOT NULL LIMIT 25;
ERROR 12003: Keyspace not found in CB datastore keyspace yelp - cause: No bucket named yelp
```
