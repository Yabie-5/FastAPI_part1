""" 
This is module.

ここに起動イベントとシャットダウンイベントをラップ
データベース接続の作成とシャトダウンを担当する非同期関数を返す
 """
from typing import Callable
from fastapi import FastAPI

from app.db.tasks import connect_to_db, close_db_connection

def create_start_app_handler(app: FastAPI) -> Callable:
    """ 
    doc:

    開始時のハンドルを作成

    args:

    app(FastAPI): 

    return:

    start_app(Collable): 

     """
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app

def create_stop_app_handler(app: FastAPI) -> Callable:
    """ 
    docs:

    停止時のハンドルを作成

    args:

    app(FastAPI): 

    return:

    stop_app(Collable): 
     """
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app
