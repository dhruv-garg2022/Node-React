
import boto3

def fetch_id(name,access_id,secret_id,region):
    iam_client = boto3.client('iam',aws_access_key_id=access_id, aws_secret_access_key = secret_id,region_name= region)
    response = iam_client.get_user(UserName=name)
    return response['User']['UserId']
    