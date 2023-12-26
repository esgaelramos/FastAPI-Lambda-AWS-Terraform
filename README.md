# FastAPI-Lambda-AWS-Terraform

Project to deploy a FastAPI application on AWS Lambda using Terraform.

| [Installation](#installation)
| [AWS CLI](#aws-cli)
| [Terraform](#terraform)
| [GitHub Actions](#github-actions)
| [ExtraTools](#extratools) |

## Installation
Create a virtual environment
```bash
python -m venv env
```

Activate the virtual environment
```bash
source env/bin/activate
```

Install the requirements
```bash
pip install -r requirements.txt
```

Run the application
```bash
python src/app.py
```

<br>

## AWS CLI

First of all, you need to [install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
Select your OS and follow the instructions. Good luck!

Check the installation
```bash
aws --version
```

### Generate AWS Credentials Keys

1. Log in to the AWS Console:
    + Go to AWS Management Console and log in with your AWS account.
    + Navigate to IAM:

2. Create a new user in IAM
    + Inside IAM, go to the "Users" section and choose "Add user".
    + Assign a username.
    + Select "Programmatic access" to generate an: 
        + Access key ID.
        + Secret access key.
    + Then, click on "Next".

3. Assign Permissions to the User
    + Choose the permissions you want to assign to this user. 
    + You can add the user to a group with specific permissions,
        + Or copy permissions from an existing user, 
        + Or attach policies directly to the user.
    + For this example, we need to check [the Terraform file](infra-lambda/main.tf)
    + And assign the permissions for every resource that we are going to use.
    
4. Review and Creation:
    + Review your user configuration and click on "Create user".
    + Once the user is created, you will see a screen with the keys:
    + Copy the "Access key ID".
    + Copy the "Secret access key".

Set up your credentials
```bash
aws configure
```

### Create a bucket S3 in AWS
    
1. Log in to the AWS Console:
    + Go to AWS Management Console and log in with your AWS account.
    + Navigate to S3:

2. Create a new bucket in S3
    + Inside S3, click on "Create bucket".
    + Assign a name to the bucket.
    + Select the region. 
    + Note: (Same region that you are going to use in the Terraform file)
    + Then, click on "Create bucket".

3. Review and Creation:
    + Review your bucket configuration and click on "Create bucket".
    + Once the bucket is created, you will see a screen with the bucket name:
    + Copy the "Bucket name".

4. Set up your bucket name in the Terraform file:
    + Go to the [Terraform file](infra-lambda/main.tf)
    + And set the bucket name in the variable "bucket_name".

<br>

## Terraform

First of all, you need to [install Terraform](https://developer.hashicorp.com/terraform/install).
Select your OS and follow the instructions. Good luck!

Check the installation
```bash
terraform -version
```

### Terraform Commands

All instructions of deploy are executed in the [GitHub Actions](#github-actions) workflow, but you can run it locally.
After you have installed Terraform, you can run the following commands in your machine:

Initialize a Terraform
```bash
terraform init
```

Validate the configuration files
```bash
terraform validate
```

Generate and show an execution plan
```bash
terraform plan
```

Create or update infrastructure
```bash
terraform apply
```

Finally, destroy the infrastructure
```bash
terraform destroy
```

<br>

## GitHub Actions

The workflow is executed when a push is made to the main branch.
The workflow is executed in the following order:

### Deploy Production

1. Checkout Repository
    + Checkout the repository to the runner's file system.

2. Configure AWS Credentials
    + Configure AWS credentials for use in other actions.
    + The credentials are configured as secrets in the repository settings.
    + DON'T FORGET CREATE THE SECRETS IN THE REPOSITORY SETTINGS!
        + AWS_ACCESS_KEY_ID
        + AWS_SECRET_ACCESS_KEY
    
3. Install Terraform
    + Install Terraform on the runner.

4. Terraform Init
    + Initialize a Terraform working directory.
    + The working directory is the location of the Terraform files.
    + In this case, the Terraform files are in the folder "infra-lambda".

5. Terraform Apply
    + Apply a Terraform execution plan.
    + The execution plan is generated in the previous step.
    + The execution plan is applied automatically.

<br>

## ExtraTools
Tree of the fundamental project
```bash
tree -I "env|.git|.pytest_cache|__pycache__|.terraform" -la
```
