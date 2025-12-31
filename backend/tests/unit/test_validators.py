"""バリデーターのテスト"""

import pytest
from uuid import uuid4

from src.utils.validators import (
    validate_required,
    validate_string_length,
    validate_email,
    validate_uuid,
    validate_slug,
    ValidationError
)


class TestValidators:
    """バリデーターのテストクラス"""
    
    def test_validate_required_success(self):
        """必須バリデーション成功ケース"""
        validate_required("test", "テストフィールド")
        validate_required(123, "数値フィールド")
        validate_required([], "リストフィールド")
    
    def test_validate_required_failure(self):
        """必須バリデーション失敗ケース"""
        with pytest.raises(ValidationError) as exc_info:
            validate_required(None, "テストフィールド")
        assert "必須です" in str(exc_info.value)
        
        with pytest.raises(ValidationError):
            validate_required("", "テストフィールド")
        
        with pytest.raises(ValidationError):
            validate_required("   ", "テストフィールド")
    
    def test_validate_string_length_success(self):
        """文字列長バリデーション成功ケース"""
        validate_string_length("test", "テスト", min_length=1, max_length=10)
        validate_string_length("hello", "テスト", min_length=5, max_length=5)
    
    def test_validate_string_length_failure(self):
        """文字列長バリデーション失敗ケース"""
        with pytest.raises(ValidationError):
            validate_string_length("a", "テスト", min_length=5)
        
        with pytest.raises(ValidationError):
            validate_string_length("very long string", "テスト", max_length=5)
    
    def test_validate_email_success(self):
        """メールアドレスバリデーション成功ケース"""
        validate_email("test@example.com")
        validate_email("user.name+tag@domain.co.jp")
    
    def test_validate_email_failure(self):
        """メールアドレスバリデーション失敗ケース"""
        with pytest.raises(ValidationError):
            validate_email("invalid-email")
        
        with pytest.raises(ValidationError):
            validate_email("@example.com")
        
        with pytest.raises(ValidationError):
            validate_email("test@")
    
    def test_validate_uuid_success(self):
        """UUIDBバリデーション成功ケース"""
        test_uuid = str(uuid4())
        result = validate_uuid(test_uuid, "ID")
        assert str(result) == test_uuid
    
    def test_validate_uuid_failure(self):
        """UUIDバリデーション失敗ケース"""
        with pytest.raises(ValidationError):
            validate_uuid("invalid-uuid", "ID")
        
        with pytest.raises(ValidationError):
            validate_uuid("123", "ID")
    
    def test_validate_slug_success(self):
        """スラッグバリデーション成功ケース"""
        validate_slug("test-slug")
        validate_slug("hello-world-123")
        validate_slug("simple")
    
    def test_validate_slug_failure(self):
        """スラッグバリデーション失敗ケース"""
        with pytest.raises(ValidationError):
            validate_slug("Test-Slug")  # 大文字
        
        with pytest.raises(ValidationError):
            validate_slug("test_slug")  # アンダースコア
        
        with pytest.raises(ValidationError):
            validate_slug("test slug")  # スペース