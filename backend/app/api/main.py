from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import config, tasks # 追加
from app.api.routes import router as api_router


def get_application():
    app = FastAPI(title=config.PROJECT_NAME,version=config.VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        # cookieの共有を行う設定（defaultはFalse）
        allow_credentials=True,
        # 許可するHTTPメソッドを指定する。（defaultはGET）
        allow_methods=["*"],
        # オリジン間リクエストでサポートするHTTPリクエストヘッダーのリストを指定する。
        # Accept、Accept-Language、Content-Language、Content-Typeヘッダーが常に許可される。
        allow_headers=["*"],
    )
    # アプリ開始時のハンドラ
    app.add_event_handler("startup", tasks.create_start_app_handler(app)) # 追加
    # 終了時のハンドラ
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app)) # 追加
    
    app.include_router(api_router,prefix="/api")

    return app

app=get_application()