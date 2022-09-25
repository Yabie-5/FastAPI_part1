from fastapi import FastAPI

from databases import Database
from app.core.config import DATABASE_URL
import logging

logger = logging.getLogger(__name__)

async def connect_to_db(app: FastAPI) -> None:
    """ 
    doc:

    databasesパッケージを使用し
    core/config.py ファイルで構成したDATABASE_URLを使用し
    PostgreSQLへの接続を確立している 
    
    これは async/await によって非同期に行われ、
    接続が正常に完了するまで待機したのちに 
    FastAPI オブジェクトである app の state に _db としてアタッチしている"""
    database = Database(DATABASE_URL, min_size=2, max_size=5)

    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn("--- DATABASE CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DATABASE CONNECTION ERROR ---")
        

async def close_db_connection(app: FastAPI) -> None:
    """ 
    doc:
    
    アプリがシャットダウンした際にデータベースから切断 """
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DATABASE DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DATABASE DISCONNECT ERROR ---")