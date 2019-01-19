import boto3
    client = boto3.client('s3',
    aws_access_key_id='AKIAJ3ETLJJW5P42DKSA',
    aws_secret_access_key='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'        
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('C:\Program Files (x86)\Jenkins\workspace\gitdevelopment\testwebproject\testweb.war', 'arn:aws:s3:::asg-cloudops/LN10.4', 'testweb.war')
