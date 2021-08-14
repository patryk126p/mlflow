# MLflow tracking server setup

For one person operation it is enough to install mlflow (`pip install mlflow`) and run command `mlflow server` to start server locally.<br>
It is good idea though to use database for backend store and for example S3 for artifact store - [more info](https://www.mlflow.org/docs/latest/tracking.html#mlflow-tracking-servers)

----
Simple setup for a team based on [article](https://towardsdatascience.com/deploy-mlflow-with-docker-compose-8059f16b6039)

1. Create S3 bucket for storing artifacts
2. Create IAM user with programmatic access and `AmazonS3FullAccess` permission
2. Create EC2 instance (eg. m5.xlarge) for MLflow server with exposed port 80
3. Make sure that docker-compose is available on the instance
4. Execute:
```
git clone https://github.com/patryk126p/mlflow.git
cd mlflow/tracking_server
export MYSQL_DATABASE=<INSERT_VALUE>
export MYSQL_USER=<INSERT_VALUE>
export MYSQL_PASSWORD=<INSERT_VALUE>
export MYSQL_ROOT_PASSWORD=<INSERT_VALUE>
export AWS_ACCESS_KEY_ID=<INSERT_VALUE>
export AWS_SECRET_ACCESS_KEY=<INSERT_VALUE>
export AWS_DEFAULT_REGION=<INSERT_VALUE>
export S3_BUCKET=<INSERT_VALUE>
docker-compose up -d --build
```
