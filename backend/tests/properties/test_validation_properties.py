"""バリデーション関数のプロパティベーステスト"""

import pytest
from hypothesis import given, strategies as st, settings, HealthCheck
import re

from src.utils.validators import (
    validate_string_length,
    validate_email,
    ValidationError
)


class TestValidationProperties:
    """バリデーション関数のプロパティテスト"""
    
    @given(st.text(min_size=1, max_size=100))
    def test_string_length_validation_property(self, text: str):
        """文字列長バリデーションのプロパティ: 有効な長さの文字列は例外を発生させない"""
        # 文字列の長さが範囲内の場合、例外は発生しない
        min_len = 1
        max_len = 100
        
        if min_len <= len(text) <= max_len:
            # 例外が発生しないことを確認
            try:
                validate_string_length(text, "テスト", min_len, max_len)
            except ValidationError:
                pytest.fail("有効な長さの文字列でValidationErrorが発生しました")
    
    @given(st.text(min_size=101))
    def test_string_too_long_property(self, text: str):
        """文字列長バリデーションのプロパティ: 長すぎる文字列は例外を発生させる"""
        max_len = 100
        
        with pytest.raises(ValidationError):
            validate_string_length(text, "テスト", max_length=max_len)
    
    @given(
        st.builds(
            lambda local, domain, tld: f"{local}@{domain}.{tld}",
            local=st.text(
                alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._+-",
                min_size=1,
                max_size=20
            ).filter(lambda x: x and not x.startswith('.') and not x.endswith('.')),
            domain=st.text(
                alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-",
                min_size=1,
                max_size=20
            ).filter(lambda x: x and not x.startswith('-') and not x.endswith('-')),
            tld=st.text(
                alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                min_size=2,
                max_size=6
            )
        )
    )
    def test_valid_email_property(self, email: str):
        """メールアドレスバリデーションのプロパティ: 有効なメールアドレスは例外を発生させない"""
        try:
            validate_email(email)
        except ValidationError:
            pytest.fail(f"有効なメールアドレス '{email}' でValidationErrorが発生しました")
    
    @given(st.one_of(
        st.text(max_size=50).filter(lambda x: '@' not in x),  # @がない
        st.text(max_size=50).filter(lambda x: x.count('@') > 1),  # @が複数
        st.builds(lambda x: f"{x}@", st.text(min_size=1, max_size=20)),  # ドメインがない
        st.builds(lambda x: f"@{x}", st.text(min_size=1, max_size=20)),  # ローカル部がない
    ))
    def test_invalid_email_property(self, invalid_email: str):
        """メールアドレスバリデーションのプロパティ: 無効なメールアドレスは例外を発生させる"""
        with pytest.raises(ValidationError):
            validate_email(invalid_email)