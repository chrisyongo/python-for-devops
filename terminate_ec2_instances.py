import boto3

client = boto3.client('ec2')

response = client.describe_instances()

new_list = []
for reservation in response['Reservations']:
	for instance in reservation['Instances']:
		new_list.append(instance['InstanceId'])
print(new_list)
client.terminate_instances(InstanceIds=(new_list))