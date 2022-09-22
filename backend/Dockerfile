# pythonのTags名を指定。
FROM python:3.10.4-alpine
# 処理を実行するフォルダ名を指定。
WORKDIR /backend
# 実行環境にインストールする内容を記載したtxtファイルを実行フォルダにコピーする
COPY ./requirements.txt /backend/requirements.txt
# requirements.txtで記載したミドルウェアのインストールの実行

RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && python3 -m pip install -r /backend/requirements.txt --no-cache-dir \
    && apk --purge del .build-deps

COPY . /backend
