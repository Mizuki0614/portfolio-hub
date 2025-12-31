#!/usr/bin/env python3
"""開発用スクリプト"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(command: list[str], description: str) -> bool:
    """コマンドを実行"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"✅ {description} 完了")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} 失敗")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False


def setup_dev_environment():
    """開発環境のセットアップ"""
    print("🚀 Portfolio Hub Backend 開発環境セットアップ")
    
    # 依存関係のインストール
    if not run_command(["python", "-m", "uv", "sync"], "依存関係のインストール"):
        return False
    
    # コードフォーマット
    if not run_command(["python", "-m", "uv", "run", "black", "src/", "tests/"], "コードフォーマット"):
        return False
    
    if not run_command(["python", "-m", "uv", "run", "isort", "src/", "tests/"], "インポート整理"):
        return False
    
    # リント
    if not run_command(["python", "-m", "uv", "run", "flake8", "src/", "tests/"], "リント実行"):
        return False
    
    # 型チェック
    if not run_command(["python", "-m", "uv", "run", "mypy", "src/"], "型チェック"):
        return False
    
    # テスト実行
    if not run_command(["python", "-m", "uv", "run", "pytest", "tests/", "-v"], "テスト実行"):
        return False
    
    print("🎉 開発環境セットアップ完了!")
    return True


def run_tests():
    """テストの実行"""
    print("🧪 テスト実行")
    
    # 単体テスト
    if not run_command(["python", "-m", "uv", "run", "pytest", "tests/unit/", "-v"], "単体テスト"):
        return False
    
    # プロパティベーステスト
    if not run_command(["python", "-m", "uv", "run", "pytest", "tests/properties/", "-v"], "プロパティベーステスト"):
        return False
    
    # カバレッジ付きテスト
    if not run_command([
        "python", "-m", "uv", "run", "pytest", "tests/", 
        "--cov=src", "--cov-report=html", "--cov-report=term"
    ], "カバレッジテスト"):
        return False
    
    print("✅ 全テスト完了!")
    return True


def main():
    """メイン関数"""
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  python scripts/dev.py setup    # 開発環境セットアップ")
        print("  python scripts/dev.py test     # テスト実行")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "setup":
        success = setup_dev_environment()
    elif command == "test":
        success = run_tests()
    else:
        print(f"不明なコマンド: {command}")
        sys.exit(1)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()