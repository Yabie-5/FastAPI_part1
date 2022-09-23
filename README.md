# FastAPI_part1
FastAPIでWebAPIを作ってみるその1

- 開発環境 \
	- Python: 3.10.4 \
	- FastAPI: 0.78.0 \
	- Uvicorn: 0.18.1 \
	- Docker: 20.10.16 \
	- postgresql: 14.4 \

- フォルダ構造 \
.
├── backend \
│   ├── Dockerfile \
│   ├── alembic.ini \
│   ├── app \
│   │   ├── api \
│   │   │   │ \
│   │   │   ├── main.py \
│   │   │   └── routes \
│   │   │       ├── __init__.py \
│   │   │       └── ma_companyController.py \
│   │   ├── core \
│   │   │   ├── config.py \
│   │   │   └── tasks.py \
│   │   └── db \
│   │       ├── __init__.py \
│   │       ├── migrations \
│   │       │   ├── env.py \
│   │       │   ├── script.py.mako \
│   │       │   └── versions \
│   │       ├── repositories \
│   │       │   ├── __init__.py \
│   │       │   └── base.py \
│   │       └── tasks.py \
│   └── requirements.txt \
└── docker-compose.yml 

- 参考資料

	- Fast APIでWebAPIを作ってみるシリーズ:[Qiita](https://qiita.com/AQUA651/items/d130132493d6b2ad0bd7), [nMoMo's](https://nmomos.com/tips/2021/01/23/fastapi-docker-1/)

