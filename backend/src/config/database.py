"""データベース設定"""

import os
import psycopg2
from contextlib import contextmanager
from typing import Generator, Optional
import logging

from .settings import settings

logger = logging.getLogger(__name__)


class DatabaseConfig:
    """データベース設定クラス"""
    
    @staticmethod
    def get_connection_string() -> str:
        """データベース接続文字列を取得"""
        if not all([settings.db_host, settings.db_name, settings.db_user, settings.db_password]):
            raise ValueError("データベース接続情報が不完全です")
        
        return (
            f"host={settings.db_host} "
            f"port={settings.db_port} "
            f"dbname={settings.db_name} "
            f"user={settings.db_user} "
            f"password={settings.db_password}"
        )


@contextmanager
def get_db_connection() -> Generator[psycopg2.extensions.connection, None, None]:
    """データベース接続のコンテキストマネージャー"""
    conn = None
    try:
        conn_string = DatabaseConfig.get_connection_string()
        conn = psycopg2.connect(conn_string)
        yield conn
    except psycopg2.Error as e:
        logger.error(f"データベース接続エラー: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


def execute_query(
    query: str,
    params: Optional[tuple] = None,
    fetch_one: bool = False,
    fetch_all: bool = False
) -> any:
    """安全なクエリ実行"""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                
                if fetch_one:
                    return cursor.fetchone()
                elif fetch_all:
                    return cursor.fetchall()
                else:
                    conn.commit()
                    return cursor.rowcount
                    
    except psycopg2.Error as e:
        logger.error(f"クエリ実行エラー: {e}")
        raise