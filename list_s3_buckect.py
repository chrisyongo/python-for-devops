import boto3


client = boto3.client('s3')

bucket_name = str(input('Please enter bucket name to be created: '))

bucket_create = client.create_bucket(
	ACL='private',
	Bucket=bucket_name	
	)

tag_response = str(input('Press Y if true and N if not'))

if tag_response == 'Y':
	tag_key= str(input('Please enter key for tag: '))
	tag_value = str(input('Please enter tag value: '))
	response = client.put_bucket_tagging(
    Bucket=bucket_name,
    Tagging={
        'TagSet': [
            {
                'Key': tag_key,
                'Value': tag_value,
            }
        ],
    },
)

response = client.list_buckets()
for name in response['Buckets']:
	print(name)