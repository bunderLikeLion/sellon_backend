# infra


## ECR 생성

```
$ aws ecr create-repository --repository-name sellon-webapp --profile sellon
$ aws ecr create-repository --repository-name sellon-nginx --profile sellon
```


```
aws ecr get-login-password --region ap-northeast-2 --profile sellon | docker login --username AWS --password-stdin 741892569245.dkr.ecr.ap-northeast-2.amazonaws.com

docker-compose -f docker-compose.production.yml build
docker-compose -f docker-compose.production.yml push
```
