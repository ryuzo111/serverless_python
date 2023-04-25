import json
import boto3
from datetime import datetime
# import requests


def lambda_handler(event, context):


    # DynamoDBクライアントを作成する
    # dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://192.168.11.5:8000')
    table_name = 'Users'
    table = dynamodb.Table(table_name)
    print("ここに来ている")

    # TODO オートインクリメント的なノリを作る
    id = 'user001'
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # テーブルにデータをインサートする
    item = {
        'id': id,
        'created_at': created_at
    }
    response = table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body" : response
    }
