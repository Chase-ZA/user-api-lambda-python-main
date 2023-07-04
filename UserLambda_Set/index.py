import boto3

def lambda_handler(event, context):
    ddbClient = boto3.resource('dynamodb')
    ddbTable = ddbClient.Table('Users')
    response = ddbTable.put_item(
        Item={
            'id': event['id'],
            'name': event['name'],
            'surname': event['surname'],
            'gender': event['gender'],
            'id_number': event['id_number'],
            'birthday': event['birthday']
        }
    )
    return {
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        'body': 'Record ' + event['id'] + ' Added'
    }