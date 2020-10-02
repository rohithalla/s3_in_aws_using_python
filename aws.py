import boto3
import pandas as pd

# Make dataframes
t1 = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})
t2 = pd.DataFrame({'x': [10, 20, 30], 'y': ['aa', 'bb', 'cc']})

# Save to csv
t1.to_csv('t1.csv')
t2.to_csv('t2.csv')


s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='your aws access key id',
    aws_secret_access_key='your aws secret access key'
)

# Print out bucket names
#for bucket in s3.buckets.all():
#    print(bucket.name)

#s3.Bucket('your bucket name').upload_file(Filename='t1.csv', Key='t1.csv')
#s3.Bucket('your bucket name').upload_file(Filename='t2.csv', Key='t2.csv')

for obj in s3.Bucket('your bucket name').objects.all():
    print(obj)

# Load csv file directly into python
obj = s3.Bucket('your bucket name').Object('t1.csv').get()
foo = pd.read_csv(obj['Body'], index_col=0)
print(foo)

# Download file and read from disc
#s3.Bucket('your bucket name').download_file(Key='foo.csv', Filename='foo2.csv')
#pd.read_csv('foo2.csv', index_col=0)
