# import re
import boto3

def start(instance_id,access_id,secret_id,region):
  ec2_client = boto3.client("ec2",aws_access_key_id=access_id, aws_secret_access_key = secret_id,region_name=region)
  reponse = ec2_client.start_instances(InstanceIds=[instance_id])

# id=input("Enter the instance id\n")
# stop_instance(id)