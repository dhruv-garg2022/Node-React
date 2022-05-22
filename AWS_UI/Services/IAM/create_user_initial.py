import boto3

def create(name, id,access_id,secret_id,region):
    print("\n\n\n",access_id,secret_id,region,"\n\n\n")
    iam_client = boto3.client('iam',aws_access_key_id=access_id, aws_secret_access_key = secret_id,region_name= region)
    username=name+id
    response = iam_client.create_user(UserName=username)
    iam_client.add_user_to_group(GroupName="ecom_user",UserName=username)
    return response['User']['UserId']