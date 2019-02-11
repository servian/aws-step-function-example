import boto3

def lambda_handler(event, context):
    '''
    Sends notification of negative results from sentiment analysis via SNS
    '''
    
    #construct message from input data and publish via SNS
    sns = boto3.client('sns')
    sns.publish(
        TopicArn = 'arn:aws:sns:XXXXXXXXXXXXXXXX:my-SNS-topic',
        Subject = 'Negative Review Received',
        Message = 'Review (ID = %i) of %s (ID = %i) received with negative results from sentiment analysis. Feedback from Customer (ID = %i): "%s"' % (int(event['reviewID']), 
                    event['reviewType'], int(event['productID']), int(event['customerID']), event['feedback'])
    )
    
    #pass through values
    return {
        'sentiment': event['sentiment'],
        'reviewType': event['reviewType'],
        'reviewID': event['reviewID'],
        'customerID': event['customerID'],
        'productID': event['productID'],
        'feedback': event['feedback'],
    }