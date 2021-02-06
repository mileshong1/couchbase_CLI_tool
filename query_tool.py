# imports to connect to couchbase
from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

#import for query options
from couchbase.cluster import QueryOptions

#couchbase error import
from couchbase.exceptions import CouchbaseException, CouchbaseTransientException

#imports for .env file
import os
from dotenv import load_dotenv
load_dotenv()

#sys import for command line arguments
import sys

#Global Variables
MAX_RETRIES = 5
RETRY_DELAY = 50

def run_query(cluster, query):
    '''
    Parameters:
    -cluster: Cluster object
    -query: string, the query we want to execute

    Returns:
    -list of rows that are the result of the query
    '''
    try:
        rows = cluster.query(query, QueryOptions(positional_parameters=["CBS"]))

        return rows

    except CouchbaseException as err:
        for error in err.objextra.value["errors"]:
            print(f"ERROR {error['code']}: {error['msg']}")

    except CouchbaseTransientException as err:
        #retriable errors
        if MAX_RETRIES > 0:
            print("Transient Exception, retrying operation")

        run_query(cluster, query)

if __name__ == "__main__":
    num_args = len(sys.argv)

    if num_args == 1:
        print("ERROR: Missing query command line arugment.")
        exit(0)
    elif num_args == 2:
        #connect to cluster using auth
        cluster = Cluster("couchbase://localhost", ClusterOptions(
            PasswordAuthenticator(os.getenv('USERNAME'), os.getenv('PASSWORD'))
        ))
            
        #get travel-sample bucket
        cb = cluster.bucket('travel-sample') 

        query = sys.argv[1]

        print(f"Running: {query}")

        #run the query
        result = run_query(cluster, query)

        #iterate through rows and print
        for row in result:
            print(row)

    else:
        print("ERROR: Too many command line arugments")
        exit(0)