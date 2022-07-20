# sellon_backend

## Dev Settings

1. 패키지매니저로 pipenv를 활용합니다.
```sh
# Mac인경우
> brew install pipenv

# Windows인 경우
> pip install pipenv


> cd webapp
> pipenv install
```

2. pre-commit을 설정합니다. (1번 수행 후)
```sh
> pre-commit install
```

## Commands
### nginx reload
```
docker exec -it nginx-dev-container nginx -s reload
```

### 로그 보기
```
## 전체 
docker-compose logs -f

## webapp 로그 보기
docker-compose logs -f webapp
```

### 슈퍼 유저 생성
```
docker-compose run --rm webapp python manage.py createsuperuser
```

### 마이그레이션 생성
```
docker-compose run --rm webapp python manage.py makemigrations
```
