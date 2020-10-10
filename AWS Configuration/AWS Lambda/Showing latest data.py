import boto3
import json

def lambda_handler(event,contex):
    res = dynamodb.get_item(
        TableName='ESP8266_Sensor_Data',
        Key={
            'mac_Id' :
                {
                    'S': "84:f3:eb:fc:61:71"
                },
                'ts' : {
                    'N': '1601997016809'
                }
        }
    )
    return res