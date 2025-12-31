# Portfolio Hub Steering

## プロジェクト概要
AWS上のサーバレスサービスでホストする個人ポートフォリオハブサイトの開発
写真家とインフラエンジニア両方の専門性を洗練されたデザインでアピール

## 技術方針

### デザイン重視
- **洗練されたUI/UX**: 写真家・エンジニア両方の専門性を表現
- **ポートフォリオ特化**: 作品展示に最適化されたレイアウト
- **プロフェッショナル**: 高品質な視覚的印象

### インフラ構成
- **ホスティング**: AWS サーバレスサービス（Lambda、API Gateway、CloudFront等）
- **コスト最優先**: アクセス課金型のサービスを選択
- **データベース**: コスト重視でAurora Serverless（0ACU対応）またはDynamoDB
- **プロビジョニングRDS**: 避ける（コスト面で不適切）

### 開発者プロファイル
- **強み**: インフラエンジニア、AWS、Python
- **弱み**: フロントエンド開発
- **学習目標**: フロントエンド技術の習得

### プロジェクト目的
1. **写真家としてのアピール**: 写真作品の美しい展示
2. **エンジニアとしてのアピール**: 技術プロジェクトの効果的な紹介
3. **個人ブランディング**: 両方の専門性を統合したプロフェッショナルイメージ
4. **検証プレイグランド**: AWS環境構築の実験・検証
5. **学習**: フロントエンド技術とRDBMS（PostgreSQL）の実践的習得

## 技術選択基準

### フロントエンド技術選択
1. **汎用性**: 業界で広く使用されている技術
2. **学習価値**: エンジニアとしてのスキルアップに寄与
3. **保守性**: 長期的な維持管理が容易
4. **パフォーマンス**: 写真表示に適した高速レンダリング
5. **エコシステム**: 豊富なライブラリとコミュニティサポート

### 候補技術スタック
- **React + Next.js**: 業界標準、SSG対応、豊富なエコシステム
- **Vue.js + Nuxt.js**: 学習しやすい、パフォーマンス良好
- **TypeScript**: コード品質向上、大規模開発対応
- **Tailwind CSS**: 効率的なスタイリング、カスタマイズ性

### フロントエンド
- **技術選択**: 汎用性が高く現代的なフレームワーク（React、Vue.js、Next.js等を検討）
- **エンジニアポートフォリオ適性**: 業界標準的で学習価値の高い技術
- **デザイン重視**: 洗練されたUI/UXライブラリの採用
- **画像最適化**: 写真作品の高品質表示
- AWS Amplifyとの親和性を重視
- 静的サイト生成（SSG）でCloudFrontでの配信を想定
- TypeScript採用でコード品質向上

### バックエンド
- Python優先（既存スキルを活用）
- AWS Lambda + API Gateway
- サーバレス First

### CI/CD基盤
- **GitHub**: ソースコード管理・公開リポジトリ
- **AWS Codeシリーズ**: CodePipeline、CodeBuild、CodeDeploy
- **統合**: GitHub Webhook → CodePipeline連携
- **AWSネイティブ**: AWS環境に特化した実績構築
- **自動化**: ブランチ別の段階的デプロイメント
- **監視**: CloudWatchによる包括的な監視・ログ記録

### データベース選択基準
1. **第一選択**: Aurora Serverless v2（0 ACU対応、PostgreSQL）
   - コスト効率: アイドル時$0、低トラフィック時$5-20/月
   - 学習価値: RDBMS設計、SQL、Aurora運用
   - スケーラビリティ: 自動スケーリング（0-128 ACU）
2. **避ける**: プロビジョニングRDS（固定コスト発生）
3. **将来検討**: DynamoDB（NoSQL学習目的）

## 開発フェーズ
1. **Phase 1**: 基本的な個人ポートフォリオサイト（プロフィール、写真・エンジニアリングポートフォリオ）
2. **Phase 2**: ブログ機能追加
3. **Phase 3**: 管理機能・高度な機能（コンテンツ管理システム）

## 最終技術スタック構成

### **確定技術スタック**
```
Frontend: Next.js 14 + TypeScript + Tailwind CSS
Backend: AWS Lambda + API Gateway (Python)
Database: Aurora Serverless v2 (PostgreSQL, 0 ACU対応)
Storage: S3 (画像・静的ファイル)
CDN: CloudFront
Auth: AWS Cognito
IaC: Terraform (汎用性重視)
CI/CD: GitHub + AWS Code シリーズ (GitHub → CodePipeline → CodeBuild → CodeDeploy)
Monitoring: CloudWatch
```

### **予想月額コスト**
```
S3 + CloudFront: $2-8/月
Aurora Serverless v2: $5-20/月
Lambda + API Gateway: $0-2/月
その他AWS サービス: $1-3/月
合計: $8-33/月
```

### **学習・実績価値**
- **フロントエンド**: Next.js、TypeScript、モダンWeb開発
- **バックエンド**: Python、サーバレスアーキテクチャ
- **データベース**: PostgreSQL、RDBMS設計、SQL最適化
- **インフラ**: Terraform、IaC、サーバレス運用
- **CI/CD**: AWS Codeシリーズ、自動化基盤
- **監視**: CloudWatch、運用監視

## コード品質・保守性指針

### ディレクトリ構成
- **保守性重視**: 機能別・レイヤー別の明確な分離
- **スケーラビリティ**: 機能追加時の影響範囲を最小化
- **可読性**: 新規参加者が理解しやすい構造
- **業界標準**: 各技術スタックのベストプラクティスに準拠

### コード管理原則
1. **単一責任原則**: 1つのファイル・関数は1つの責任
2. **依存関係の明確化**: モジュール間の依存を最小化
3. **テスタビリティ**: テストしやすい構造
4. **ドキュメント**: コードの意図を明確に記述

### 推奨ディレクトリ構成

#### フロントエンド（Next.js）
```
src/
├── app/                    # App Router (Next.js 13+)
│   ├── (auth)/            # Route Groups
│   ├── admin/             # 管理画面
│   ├── blog/              # ブログ関連
│   ├── portfolio/         # ポートフォリオ
│   └── globals.css
├── components/            # 再利用可能コンポーネント
│   ├── ui/               # 基本UIコンポーネント
│   ├── forms/            # フォーム関連
│   ├── layout/           # レイアウト関連
│   └── portfolio/        # ポートフォリオ特化
├── hooks/                # カスタムフック
├── lib/                  # ユーティリティ・設定
├── types/                # TypeScript型定義
├── utils/                # ヘルパー関数
└── __tests__/            # テストファイル
    ├── components/
    ├── hooks/
    ├── utils/
    └── properties/       # プロパティベーステスト
```

#### バックエンド（Python Lambda）
```
backend/
├── src/
│   ├── handlers/         # Lambda関数ハンドラー
│   │   ├── auth/
│   │   ├── blog/
│   │   └── portfolio/
│   ├── services/         # ビジネスロジック
│   ├── models/           # データモデル
│   ├── utils/            # ユーティリティ
│   └── config/           # 設定管理
├── tests/                # テストファイル
│   ├── unit/
│   ├── integration/
│   └── properties/
└── requirements/         # 依存関係管理
    ├── base.txt
    ├── dev.txt
    └── prod.txt
```

#### インフラ（Terraform）
```
terraform/
├── modules/              # 再利用可能モジュール
│   ├── aurora/
│   ├── lambda/
│   ├── s3/
│   └── cloudfront/
├── environments/         # 環境別設定
│   ├── dev/
│   ├── staging/
│   └── prod/
├── global/               # 共通リソース
└── scripts/              # デプロイスクリプト
```

## コスト管理
- 月額コストを最小限に抑制
- 使用量ベースの課金モデルを優先
- 定期的なコスト監視とアラート設定