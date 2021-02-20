#!/usr/bin/env bash

# ECR Login
echo "Logging into ECR 001368854280.dkr.ecr.us-east-2.amazonaws.com"
aws ecr get-login-password --region us-east-2 --profile $1 | docker login --username AWS --password-stdin 001368854280.dkr.ecr.us-east-2.amazonaws.com

echo "Building lambda image"
docker-compose build

echo "Tagging lambda image"
docker tag selenium-docker_app:latest 001368854280.dkr.ecr.us-east-2.amazonaws.com/selenium-docker:latest
#docker tag web_client:latest 001368854280.dkr.ecr.us-east-2.amazonaws.com/lambda-prospect-conversions:${GITHUB_SHA::7}

echo "Pushing lambda image to ECR"
docker push 001368854280.dkr.ecr.us-east-2.amazonaws.com/selenium-docker:latest
#docker push 001368854280.dkr.ecr.us-east-2.amazonaws.com/lambda-prospect-conversions:${GITHUB_SHA::7}
