import boto3

# Create an ECR client from documentation
ecr_client = boto3.client('ecr')

# Create a new ECR repository firstline create-name, getting response
repository_name = 'my-ecr-repo'
response = ecr_client.create_repository(repositoryName=repository_name)

# Print the repository URI
repository_uri = response['repository']['repositoryUri']
print(repository_uri)