import boto3

def lambda_handler(event,contex):
    dynamodb_client = boto3.client('dynamodb')
    existing_tables = dynamodb_client.list_tables()['TableNames']
    return (existing_tables)