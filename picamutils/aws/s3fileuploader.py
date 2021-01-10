import logging, boto3, os
from dotenv import dotenv_values
from pathlib import Path
from botocore.exceptions import ClientError

cli = False

class S3FileUploader:
	env_path = Path('./') / '.env'
	envs = dotenv_values(env_path)
	# Set variables from .env file
	access_key = envs['AWS_ACCESS_KEY']
	secret_key = envs['AWS_SECRET_KEY']
	access_print = access_key[:3] + (len(access_key)-6)*'*' + access_key[-3:]
	secret_print = secret_key[:3] + (len(secret_key)-6)*'*' + secret_key[-3:]
	s3_bucket = envs['S3_BUCKET']

	def __init__(self,local_file, object_name=None):
		self.local_file = local_file
		self.object_name = object_name
		if cli: print(f'access_key: {self.access_print}\nsecret_key: {self.secret_print}\ns3_bucket: {self.s3_bucket}')


	def upload_file_to_bucket(self):
		if self.object_name is None:
        		self.object_name = local_file
		s3_client = boto3.client('s3', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)
		try:
			s3_client.upload_file(self.local_file, self.s3_bucket, self.object_name, ExtraArgs={'ACL': 'public-read'})
			return True
		except FileNotFoundError:
			print(f'\tFile not found!')
			return False
		except NoCredentialsError:
			print(f'\tNo credentials provided!')
			return False


if __name__ == '__main__':
	cli = True
	local_file = 'tmp/snapshot.jpg'
	object_name = 'latest.jpg'
	s3 = S3FileUploader(local_file, object_name)
	result = s3.upload_file_to_bucket()
	if result: print(f'File `{local_file}` saved as `{object_name}` successfully.')
