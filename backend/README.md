# User API


--------


**Frameworks:** \
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) 

**Main database:** \
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

**Cache database:** \
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)


--------


> Api for working with users!


## Quick Start

```shell
uvicorn main:app --host 127.0.0.1 --port 5000
```


## Migrations

```shell
# Create migrations file and init
aerich init -t src.settings.DATABASE_CONFIG
aerich init-db
# Migrate
aerich migrate
```


## Screenshot of the work:
![image](https://user-images.githubusercontent.com/84931791/188851322-3505da36-22fc-4371-86e6-10745f8bbe64.png)
