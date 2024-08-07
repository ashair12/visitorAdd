import boto3
import json
from datetime import datetime

print('Loading function')
dynamodb = boto3.client('dynamodb')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

    
def lambda_handler(event, context):
    headers = event['headers']
    sourceip = headers['X-Forwarded-For']
    dynamodb.put_item(TableName="resume-db", Item={'visitorid':{'S':sourceip},'timestamp':{'S': datetime.now().isoformat(timespec='seconds')}})

