import boto3

def list(access_id,secret_id,region):
    iam_client = boto3.client('iam',aws_access_key_id=access_id, aws_secret_access_key = secret_id,region_name= region)
    list_users = iam_client.list_users()['Users']
    users=[]
    for user in list_users:
        users.append([user['UserName'],user['UserId'],user['Arn'],user['CreateDate']])
    return users
# list()
