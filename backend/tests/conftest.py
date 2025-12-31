"""pytest設定ファイル"""

import pytest
from unittest.mock import Mock, patch
import os
import sys

# srcディレクトリをPythonパスに追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


@pytest.fixture
def mock_db_connection():
    """モックデータベース接続"""
    with patch('src.config.database.get_db_connection') as mock_conn:
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
        mock_conn.return_value.__enter__.return_value = mock_connection
        yield mock_cursor


@pytest.fixture
def sample_user_data():
    """サンプルユーザーデータ"""
    return {
        "cognito_user_id": "test-cognito-id",
        "email": "test@example.com",
        "name": "テストユーザー",
        "role": "admin"
    }


@pytest.fixture
def sample_blog_post_data():
    """サンプルブログ記事データ"""
    return {
        "title": "テスト記事",
        "content": "# テスト記事\n\nこれはテスト記事です。",
        "excerpt": "これはテスト記事です。",
        "tags": ["test", "blog"],
        "status": "published"
    }


@pytest.fixture
def sample_photo_data():
    """サンプル写真データ"""
    return {
        "title": "テスト写真",
        "description": "テスト用の写真です",
        "file_path": "/images/test.jpg",
        "thumbnail_path": "/images/test_thumb.jpg",
        "metadata": {
            "camera": "Canon EOS R5",
            "lens": "RF 24-70mm f/2.8L IS USM",
            "settings": {
                "aperture": "f/2.8",
                "shutter_speed": "1/125",
                "iso": 400
            },
            "location": "東京",
            "date_taken": "2024-01-01T12:00:00Z"
        }
    }


@pytest.fixture
def sample_project_data():
    """サンプルプロジェクトデータ"""
    return {
        "title": "テストプロジェクト",
        "description": "テスト用のプロジェクトです",
        "tech_stack": ["Python", "FastAPI", "PostgreSQL"],
        "github_url": "https://github.com/test/project",
        "demo_url": "https://demo.example.com",
        "image_paths": ["/images/project1.jpg", "/images/project2.jpg"]
    }