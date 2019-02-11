import boto3
import csv
import json
    
#initialize
s3 = boto3.client('s3')

def lambda_handler(event, context):
    '''
    reads the .csv from the S3 landing event, returns a json-formatted
    dict formed from the first line (and column headers)
    '''
    
    #Fallback tests for initializations outside scope
    try:
        s3
    except NameError:
        s3 = boto3.client('s3')
    
    
    #read s3 object
    bucket_name = event['bucket_name']
    file_key = event['file_key']
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    
    #convert response to lines of CSV
    lines = response['Body'].read().decode('utf-8').split('\n')
    
    #DictReader -> convert lines of CSV to OrderedDict
    for row in csv.DictReader(lines):
        #return just the first loop (row) results!
        return json.loads(json.dumps(row))