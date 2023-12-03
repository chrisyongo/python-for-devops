import boto3

ec2 = boto3.resource('ec2')
sns = boto3.client('sns')

tagfilter= [
{
	'Name': 'tag:Env',
	'Values': ['Production']
}
]

snapshot_list = [] # Epmty list

for instance in ec2.instances.filter():
	print(instance.instance_id)
	for volume in ec2.volumes.all():
		# print(volume.volume_id)
		snapshot = volume.create_snapshot(
			Description='Snapshot created via boto2'
			)
		snapshot_list.append(snapshot.snapshot_id)

print(snapshot_list)


response = sns.publish(
	TopicArn='arn:aws:sns:us-east-1:724418719945:notify-snapshot',
	Subject='EBS-Snapshot creation',
	Message = str(snapshot_list)
	)
print(response)