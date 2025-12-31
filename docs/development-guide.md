# 開発環境ガイド

## 概要

Portfolio Hub の開発環境は、開発者の利便性と本番環境の一貫性を両立するハイブリッド構成を採用しています。

## 開発環境戦略

### **ローカル開発（利便性・速度重視）**
- 日常的なコード開発・デバッグ
- 高速な起動・テスト実行
- IDEとの完全統合

### **Docker環境（一貫性・再現性重視）**
- 統合テスト・結合テスト
- 本番環境同等の検証
- CI/CD環境との一致

## 環境構成

### **技術スタック**
```
Frontend: Next.js 14 + TypeScript + Tailwind CSS
Backend: Python + FastAPI + uv
Database: PostgreSQL (Aurora Serverless v2互換)
```

### **開発ツール**
```
フロントエンド: Node.js + npm
バックエンド: uv (Python環境管理)
データベース: PostgreSQL (ローカル or Docker)
統合環境: Docker Compose
```

## セットアップ手順

### **1. 前提条件**
```bash
# 必要なツールのインストール
- Node.js 18+ 
- Python 3.11+
- uv (Python環境管理)
- Docker & Docker Compose
- PostgreSQL (ローカル) または Docker
```

### **2. プロジェクトクローン**
```bash
git clone https://github.com/your-username/portfolio-hub.git
cd portfolio-hub
```

### **3. フロントエンド環境セットアップ**
```bash
cd frontend
npm install
cp .env.example .env.local
# .env.local を編集（API URL等）
```

### **4. バックエンド環境セットアップ**
```bash
cd backend
uv sync                    # 依存関係インストール
cp .env.example .env       # 環境変数設定
# .env を編集（DB接続情報等）
```

### **5. データベースセットアップ**

#### **Option A: ローカルPostgreSQL**
```bash
# PostgreSQL インストール・起動
createdb portfolio_hub_dev
psql portfolio_hub_dev < schema/init.sql
```

#### **Option B: Docker PostgreSQL**
```bash
docker-compose up -d postgres
# 初期化は自動実行される
```

## 日常的な開発フロー

### **開発サーバー起動**

#### **1. データベース起動**
```bash
# ローカルPostgreSQL使用時
sudo systemctl start postgresql

# Docker使用時
docker-compose up -d postgres
```

#### **2. バックエンド開発サーバー起動**
```bash
cd backend
uv run uvicorn src.main:app --reload --port 8000
# → http://localhost:8000 で起動
# → http://localhost:8000/docs でAPI文書確認
```

#### **3. フロントエンド開発サーバー起動（別ターミナル）**
```bash
cd frontend
npm run dev
# → http://localhost:3000 で起動
```

### **開発作業**
```bash
# コード編集
# - フロントエンド: src/ 以下のReact/Next.jsコード
# - バックエンド: src/ 以下のPython/FastAPIコード

# ホットリロード
# - フロントエンド: ファイル保存で自動リロード
# - バックエンド: ファイル保存で自動リロード
```

### **テスト実行**

#### **単体テスト**
```bash
# フロントエンド単体テスト
cd frontend
npm test                    # Jest単体テスト
npm run test:watch          # ウォッチモード

# バックエンド単体テスト
cd backend
uv run pytest tests/unit/  # 単体テスト
uv run pytest tests/properties/  # プロパティベーステスト
```

#### **プロパティベーステスト**
```bash
# フロントエンド
cd frontend
npm run test:properties     # fast-check実行

# バックエンド
cd backend
uv run pytest tests/properties/ -v  # Hypothesis実行
```

## 統合テスト・結合テスト

### **Docker Compose環境**

#### **統合環境起動**
```bash
# 完全な統合環境を起動
docker-compose up -d

# サービス確認
docker-compose ps
```

#### **統合テスト実行**
```bash
# 統合テスト実行
docker-compose exec backend pytest tests/integration/
docker-compose exec frontend npm run test:integration

# E2Eテスト実行
npm run test:e2e
```

#### **環境リセット**
```bash
# データベースリセット
docker-compose down -v
docker-compose up -d postgres

# 完全リセット
docker-compose down -v --remove-orphans
docker-compose build --no-cache
docker-compose up -d
```

## 環境別設定

### **開発環境（Development）**
```bash
# フロントエンド (.env.local)
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_ENV=development

# バックエンド (.env)
DATABASE_URL=postgresql://user:pass@localhost:5432/portfolio_hub_dev
DEBUG=true
LOG_LEVEL=DEBUG
```

### **統合テスト環境（Integration）**
```bash
# docker-compose.yml で自動設定
DATABASE_URL=postgresql://postgres:password@postgres:5432/portfolio_hub_test
API_URL=http://backend:8000
FRONTEND_URL=http://frontend:3000
```

## デバッグ・トラブルシューティング

### **よくある問題と解決方法**

#### **1. ポート競合**
```bash
# ポート使用状況確認
lsof -i :3000  # フロントエンド
lsof -i :8000  # バックエンド
lsof -i :5432  # PostgreSQL

# プロセス終了
kill -9 <PID>
```

#### **2. データベース接続エラー**
```bash
# PostgreSQL状態確認
sudo systemctl status postgresql

# Docker PostgreSQL確認
docker-compose logs postgres

# 接続テスト
psql -h localhost -U postgres -d portfolio_hub_dev
```

#### **3. 依存関係エラー**
```bash
# フロントエンド依存関係再インストール
cd frontend
rm -rf node_modules package-lock.json
npm install

# バックエンド依存関係再同期
cd backend
uv sync --reinstall
```

#### **4. キャッシュクリア**
```bash
# Next.jsキャッシュクリア
cd frontend
rm -rf .next
npm run build

# uvキャッシュクリア
cd backend
uv cache clean
```

## パフォーマンス最適化

### **開発環境の高速化**

#### **1. ファイル監視最適化**
```bash
# .gitignore に追加
node_modules/
.next/
__pycache__/
.pytest_cache/
```

#### **2. テスト実行最適化**
```bash
# 並列テスト実行
cd backend
uv run pytest -n auto  # pytest-xdist使用

# 変更ファイルのみテスト
cd frontend
npm test -- --onlyChanged
```

## 本番環境との差異

### **開発環境の特徴**
- **高速起動**: ローカル環境での即座の開発開始
- **ホットリロード**: コード変更の即時反映
- **デバッグ機能**: IDEデバッガーとの完全統合
- **ログ詳細**: 詳細なデバッグログ出力

### **本番環境との一致点（Docker使用時）**
- **環境変数**: 本番同等の設定
- **ネットワーク**: サービス間通信の再現
- **データベース**: Aurora Serverless v2互換のPostgreSQL
- **ビルド**: 本番同等のビルドプロセス

## 開発ワークフロー

### **機能開発の流れ**
```bash
1. ブランチ作成
   git checkout -b feature/new-feature

2. ローカル開発
   # 開発サーバー起動
   # コード編集
   # 単体テスト実行

3. 統合テスト
   docker-compose up -d
   # 統合テスト実行

4. コミット・プッシュ
   git add .
   git commit -m "feat: 新機能追加"
   git push origin feature/new-feature

5. プルリクエスト作成
   # GitHub でPR作成
   # CI/CDパイプライン自動実行
```

### **品質チェック**
```bash
# コード品質チェック
cd frontend
npm run lint
npm run type-check

cd backend
uv run ruff check .
uv run mypy src/
```

## 監視・ログ

### **開発環境でのログ確認**
```bash
# フロントエンドログ
# ブラウザ開発者ツール Console

# バックエンドログ
# ターミナル出力（uvicorn --reload）

# データベースログ
# PostgreSQLログファイル確認
```

### **Docker環境でのログ確認**
```bash
# サービス別ログ確認
docker-compose logs frontend
docker-compose logs backend
docker-compose logs postgres

# リアルタイムログ
docker-compose logs -f backend
```

## まとめ

この開発環境ガイドに従うことで：

1. **効率的な開発**: ローカル環境での高速開発
2. **確実な品質保証**: Docker環境での統合テスト
3. **本番環境との一貫性**: CI/CD環境との整合性
4. **トラブル対応**: 問題発生時の迅速な解決

開発中に問題が発生した場合は、このガイドを参照して解決してください。