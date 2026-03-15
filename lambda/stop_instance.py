import boto3

region = 'us-east-1'
instances = ['i-04f8c46a7d43de2f6']

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    
    ec2.stop_instances(InstanceIds=instances)

    print('Stopped instances:', instances)