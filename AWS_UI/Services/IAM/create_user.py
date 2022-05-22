import boto3

def create(name,access_id,secret_id,region):
    iam_client = boto3.client('iam',aws_access_key_id=access_id, aws_secret_access_key = secret_id,region_name= region)
    response = iam_client.create_user(UserName=name)
    iam_client.add_user_to_group(GroupName="iam_group",UserName=name)
    return response['User']['UserId']
