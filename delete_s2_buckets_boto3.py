import boto3

client = boto3.client('s3')

""" Before deleting we have to check if the bucket is empty
"""

# obj = client.list_buckets()
# for item in obj['Buckets']:
# 	client.delete_bucket(item['Name'])


objs = client.list_buckets()['Buckets']
list_of_buckets = [obj['Name'] for obj in objs]
# print(list_of_buckets)

for item in list_of_buckets:
	# print(item)
	client.delete_bucket(Bucket=item)