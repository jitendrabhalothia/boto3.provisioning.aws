import boto3
client = boto3.resource(
    'ec2','us-east-1',
    aws_access_key_id='*******',
    aws_secret_access_key='**************',
   )


outfile = open('TST1.pem','w')
key_pair = client.create_key_pair(KeyName='TST1')
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)


instances = client.create_instances(
        ImageId='ami-2d39803a',
        MinCount=1,
        MaxCount=1,
        KeyName="TST1",
        InstanceType="t2.micro",
        SubnetId ='*******'
)
for instance in instances:  
    print(instance.id, instance.instance_type)                                                      
