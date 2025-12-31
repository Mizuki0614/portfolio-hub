"""エラーハンドリングユーティリティ"""

import json
import logging
from typing import Dict, Any, Optional
from enum import Enum
from functools import wraps

logger = logging.getLogger(__name__)


class ErrorCode(Enum):
    """エラーコード定義"""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    DATABASE_ERROR = "DATABASE_ERROR"


class APIError(Exception):
    """API例外クラス"""
    
    def __init__(
        self,
        message: str,
        status_code: int = 500,
        error_code: ErrorCode = ErrorCode.INTERNAL_ERROR,
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}
        super().__init__(message)


def error_handler(func):
    """Lambda関数用エラーハンドリングデコレータ"""
    @wraps(func)
    def wrapper(event, context):
        try:
            return func(event, context)
        except APIError as e:
            logger.error(f"API Error: {e.message}", extra={
                "error_code": e.error_code.value,
                "status_code": e.status_code,
                "details": e.details
            })
            return {
                "statusCode": e.status_code,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "x-error-code": e.error_code.value
                },
                "body": json.dumps({
                    "error": {
                        "message": e.message,
                        "code": e.error_code.value,
                        "details": e.details
                    }
                }, ensure_ascii=False)
            }
        except Exception as e:
            logger.exception("予期しないエラーが発生しました")
            return {
                "statusCode": 500,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "x-error-code": ErrorCode.INTERNAL_ERROR.value
                },
                "body": json.dumps({
                    "error": {
                        "message": "内部サーバーエラー",
                        "code": ErrorCode.INTERNAL_ERROR.value
                    }
                }, ensure_ascii=False)
            }
    return wrapper


class DatabaseError(APIError):
    """データベースエラー"""
    
    def __init__(self, message: str, original_error: Optional[Exception] = None):
        super().__init__(
            message=message,
            status_code=500,
            error_code=ErrorCode.DATABASE_ERROR,
            details={"original_error": str(original_error)} if original_error else {}
        )