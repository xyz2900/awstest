# s3へオブジェクトを保存
import json
import boto3

bucket_name = "test-bucket"
json_key = "test.json"
s3 = boto3.resource('s3')
obj = s3.Object(bucket_name,json_key)

test_json = {'key': 'value'}
r = obj.put(Body = json.dumps(test_json))

# get json data
print(obj.get()['Body'].read())