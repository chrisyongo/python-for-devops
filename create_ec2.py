import boto3

client = boto3.client('ec2')

response = client.run_instances(
	ImageId='ami-0230bd60aa48260c6',
	InstanceType='t2.micro',
	MaxCount=1,
	MinCount=1,
	KeyName = 'myFirstKeyPair'
	)

