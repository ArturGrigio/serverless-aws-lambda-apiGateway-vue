# BACKEND SETUP

### 1) Setting up the RDS using `aws-cli`

 ```
 aws rds create-db-instance \
     --db-instance-identifier serverless \
     --db-instance-class db.t2.micro \
     --engine MySQL \
     --allocated-storage 5 \
     --no-publicly-accessible \
     --db-name serverless \
     --master-username serverless \
     --master-user-password YOUR_PASSWORD_HERE \
     --backup-retention-period 1
 ```

### 2) Create an execution role like described here:

https://docs.aws.amazon.com/lambda/latest/dg/vpc-rds-create-iam-role.html
Save the `ARN` ID for the role

### 3) Update your `env` variables and install `pymysql`

- Navigate to `/setup/rds_config.example.py` and update your credentials.
- Rename the file to `rds_config.example.py`
- Install   `pymysql`: `pip install pymysql -t /PATH/TO/DIRECTORY/`
    - **NOTE**: AWS gotcha - if you're using MacOSX you'll need to install pymysql like explained here:
    https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
- zip the `YOUR_FUNCTION/app.py` and `rds_config.py` into `app.zip`
    - you can use this command too `cd INTO/SETUP/DIRECTORY && zip -r app.zip app.py rds_config.py pymysql`

### 4) Setting up the Lambda using `aws-cli`

 ```
aws lambda create-function \
--region us-east-1 \
--function-name   serverless-get-employees  \
--zip-file fileb://YOUR_PATH_TO/app.zip \
--role execution-role-arn \
--handler app.handler \
--runtime python3.6 \
--vpc-config SubnetIds=comma-separated-subnet-ids,SecurityGroupIds=default-vpc-security-group-id \
--profile adminuser
```

### Testing

```
aws lambda invoke \
--function-name serverless-get-employees  \
--region us-west-1 \
--profile YOUR_USER \
output.txt  
```

### Repeat step 4 for each one of your lambda functions

# FRONTEND SETUP

### 1) Create the vue project

```
vue init webpack serverless && cd serverless && npm install
```

### 2) Build the `dist` for deployment

```
npm run build
```

### 3) Deploy on a the S3 Bucket
