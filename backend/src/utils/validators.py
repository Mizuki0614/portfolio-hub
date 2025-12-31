"""バリデーションユーティリティ"""

import re
from typing import Any, Optional
from uuid import UUID

from .error_handler import APIError, ErrorCode


class ValidationError(APIError):
    """バリデーションエラー"""
    
    def __init__(self, message: str, field: Optional[str] = None):
        details = {"field": field} if field else {}
        super().__init__(
            message=message,
            status_code=400,
            error_code=ErrorCode.VALIDATION_ERROR,
            details=details
        )


def validate_required(value: Any, field_name: str) -> None:
    """必須フィールドのバリデーション"""
    if value is None or (isinstance(value, str) and value.strip() == ""):
        raise ValidationError(f"{field_name}は必須です", field_name)


def validate_string_length(
    value: str, 
    field_name: str, 
    min_length: Optional[int] = None, 
    max_length: Optional[int] = None
) -> None:
    """文字列長のバリデーション"""
    if min_length is not None and len(value) < min_length:
        raise ValidationError(
            f"{field_name}は{min_length}文字以上で入力してください", 
            field_name
        )
    
    if max_length is not None and len(value) > max_length:
        raise ValidationError(
            f"{field_name}は{max_length}文字以下で入力してください", 
            field_name
        )


def validate_email(email: str, field_name: str = "メールアドレス") -> None:
    """メールアドレスのバリデーション"""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        raise ValidationError(f"{field_name}の形式が正しくありません", field_name)


def validate_uuid(value: str, field_name: str) -> UUID:
    """UUID形式のバリデーション"""
    try:
        return UUID(value)
    except ValueError:
        raise ValidationError(f"{field_name}のUUID形式が正しくありません", field_name)


def validate_slug(slug: str, field_name: str = "スラッグ") -> None:
    """スラッグ形式のバリデーション"""
    slug_pattern = r'^[a-z0-9]+(?:-[a-z0-9]+)*$'
    if not re.match(slug_pattern, slug):
        raise ValidationError(
            f"{field_name}は小文字の英数字とハイフンのみ使用できます", 
            field_name
        )