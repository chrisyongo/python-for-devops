import boto3
from datetime import datetime, timezone, timedelta
ec2 = boto3.resource('ec2')
tagfilter = [
	{
	'Name': 'tag:Env',
	'Values': ['Production']
	}
]

snapshots = ec2.snapshots.filter(Filters=tagfilter)

client = boto3.client('ec2')
print(client.describe_snapshots(OwnerIds=['self']))
print('/n')

ebs_list = []
for snapshot in client.describe_snapshots(OwnerIds=['self'])['Snapshots']:
	ebs_list.append(snapshot['SnapshotId'])

	create_time = snapshot['StartTime']
	delete_time = datetime.now(tz=timezone.utc) - timedelta(minutes=23)
	if delete_time > create_time:
		client.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
		print('{} has been deleted'.format(snapshot['SnapshotId']))
	else:
		print('Existig snapshot {} is less than 23 minutes old'.format(snapshot['snapshot']))

