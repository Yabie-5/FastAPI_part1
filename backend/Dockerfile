# pythonのTags名を指定。
FROM python:3.10.4-alpine
# 処理を実行するフォルダ名を指定。
WORKDIR /backend
# 実行環境にインストールする内容を記載したtxtファイルを実行フォルダにコピーする
COPY ./requirements.txt /backend/requirements.txt
# requirements.txtで記載したミドルウェアのインストールの実行

RUN set -eux \
    && apk add --no-cache build-base \
    && pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir --trusted-host pypi.python.org -r /backend/requirements.txt \
    && apk del build-base 

COPY . /backend
