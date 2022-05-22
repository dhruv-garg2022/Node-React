import boto3

def delete(name,access_id,secret_id,region):
    iam_client = boto3.client('iam',aws_access_key_id=access_id, aws_secret_access_key = secret_id,region_name= region)
    iam_client.remove_user_from_group(GroupName="iam_group",UserName=name)
    iam_client.delete_user(UserName=name)

