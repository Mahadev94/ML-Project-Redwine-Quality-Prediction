# ENd-TO-END-ML-PROJECT-IMPLEMENTATION 
    1.Github repo setup
    2.project template creation
    3.project setup
    4.to create logging,exception,utility
    5.project workflow creation
    6.notebook implementation
    7.components implementation:
        1.data ingestion
        2.data validation
        3.data transformation
        4.model training
        5.model evaluation
        6.model pusher
    8.training pipeline implementation
    9.prediction pipeline implementation
    10.dockering code
    11.AWS deployment configuration-CI/CD
    12.user app implementation

## Teck stack for project:
    1.pandas lib
    2.sk-learn lib
    3.matplotlib/seaborn library
    4.pyyaml library
    5.flask
    6.AWS
    7.docker
    8.Github Actions
## venv:
    conda create -n venv13 python=3.8 -y
    conda activate venv13

    # requiremnts installation:
    pip install -r requirements.txt

# End-to-end-ML-Project
## Project-Workflows:--->
1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity 
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py

# How to run?
### STEPS:

```bash
conda create -n mlproj python=3.8 -y 
```
```bash
conda activate mlproj
```
```bash
pip install -r requirements.txt
```

```bash
python app.py
```

```bash
Now open up your local host 0.0.0.0:8080
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app






 git config --global user.name "xyz"