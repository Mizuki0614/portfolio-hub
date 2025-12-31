"""アプリケーション設定"""

import os
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """アプリケーション設定クラス"""
    
    # アプリケーション設定
    app_name: str = "Portfolio Hub Backend"
    app_version: str = "0.1.0"
    debug: bool = False
    
    # データベース設定
    db_host: Optional[str] = None
    db_port: int = 5432
    db_name: Optional[str] = None
    db_user: Optional[str] = None
    db_password: Optional[str] = None
    
    # AWS設定
    aws_region: str = "ap-northeast-1"
    s3_bucket_name: Optional[str] = None
    cognito_user_pool_id: Optional[str] = None
    cognito_client_id: Optional[str] = None
    
    # セキュリティ設定
    secret_key: Optional[str] = None
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS設定
    allowed_origins: list[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# グローバル設定インスタンス
settings = Settings()