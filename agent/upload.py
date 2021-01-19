
import boto3
import uuid
import os
import sys
import time

def checkAWSValid():
    aws_access_id = os.getenv('AWS_ACCESS_KEY_ID', None)
    aws_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', None)
    if aws_access_id and aws_access_key:
        return True
    return False

def updateLogs(userId, types, db=None):
    if not checkAWSValid():
        print('Warning, cannot access your aws account. Please check if id and keys are stored in env var.')
        return 
    if not db:
        db = boto3.resource('dynamodb', region_name='us-east-2')

    table = db.Table('CHUSILOGS')
    response = table.put_item(
       Item={
            'tid': uuid.uuid4().hex,
            'userId': userId,
            'types': types,
            'timestamp': time.time()
        }
    )
    return response