import logging, boto3, os
from dotenv import dotenv_values
from pathlib import Path
from botocore.exceptions import ClientError


class S3FileUploader:
	env_path = Path('.') / '.env'
	envs = dotenv_values(env_path)
	# Set variables from .env file
	access_key = envs['AWS_ACCESS_KEY']
	secret_key = envs['AWS_SECRET_KEY']

	def __init__(self,local_file, s3_bucket, destination_file):
		self.local_file = local_file
		self.s3_bucket = s3_bucket
		self.destination_file = destination_file

	def upload_file_to_bucket(self):
		s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
	
		try:
			s3_client.upload_file(local_file, s3_bucket, destination_file)
			return True
		except FileNotFoundError:
			print(f'\tFile not found!')
			return False
		except NoCredentialsError:
			print(f'\tNo credentials provided!')
			return False

