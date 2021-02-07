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
```
python3 
```
