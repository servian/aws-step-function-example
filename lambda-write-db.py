import boto3

def lambda_handler(event, context):
    '''
    Adds the review data to the review database table
    '''
    
    #select correct table based on input data
    dynamodb = boto3.client('dynamodb')
    if event['reviewType'] == 'Product':
        tableName = 'my-products-table'
    elif event['reviewType'] == 'Service':
        tableName = 'my-services-table'
    else:
        raise Exception("Input review is neither Product nor Service")
    
    #construct response to put data in table
    response = dynamodb.put_item(
        TableName=tableName,
        Item={
            'reviewID': {"N": event['reviewID'] },
            'customerID': {"N": event['customerID'] },
            'productID': {"N": event['productID'] },
            'feedback': {"S": event['feedback'] },
            'sentiment': {"S": event['sentiment'] }
        },
    )
    
    #pass through values 
    response['reviewType'] = event['reviewType']
    response['reviewID'] = event['reviewID']
    response['customerID'] = event['customerID']
    response['productID'] = event['productID']
    response['feedback'] = event['feedback']
    response['sentiment'] = event['sentiment']
        
    return response