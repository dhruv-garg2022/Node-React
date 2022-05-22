import secrets
import boto3
from Services.DB import delete_key

def generate(name,a_id,main_id,main_key, region):
    
    if len(a_id)==0:
        access = main_id
        secret = main_key
        print(access,"acess",secret,"1")
    else:
        access = a_id[0][0]
        secret = a_id[0][1]
        print(access,"acess",secret,"2")

        
    print("\n\n\n",access,"acess",secret,"\n\n\n")
    iam_client = boto3.client('iam',aws_access_key_id=access, aws_secret_access_key = secret,region_name= region)
    # print(a_id, "a_id ", name, " name")
    for access_key in a_id:

        try:
            delete_key.delete(name,access_key[0])
            iam_client.delete_access_key(
                UserName = name,
                AccessKeyId= access_key[0]
            )

        except:
            pass
    response = iam_client.create_access_key(UserName=name)
    # print([response['AccessKey']['AccessKeyId'], response['AccessKey']['SecretAccessKey']])
    # print("AccessKeyID:\t", response['AccessKey']['AccessKeyId'],"\nSecretAccessKey:\t", response['AccessKey']['SecretAccessKey'])
    return [(response['AccessKey']['AccessKeyId'], response['AccessKey']['SecretAccessKey'])]

# generate('dhruv1',[])
