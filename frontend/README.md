# Portfolio Hub Frontend

個人ポートフォリオサイトのフロントエンドアプリケーション

## 概要

Portfolio Hub Frontendは、写真家とインフラエンジニア両方の専門性をアピールする個人ポートフォリオサイトのフロントエンドです。洗練されたデザインと高いパフォーマンスを実現します。

## 技術スタック

- **フレームワーク**: Next.js 14 (App Router)
- **言語**: TypeScript
- **スタイリング**: Tailwind CSS
- **テスト**: Jest + React Testing Library + fast-check
- **リント**: ESLint + Prettier
- **デプロイ**: AWS CloudFront + S3

## セットアップ

### 前提条件

- Node.js 18.17+
- npm, yarn, pnpm, または bun

### インストール

```bash
# 依存関係のインストール
npm install
# または
yarn install
# または
pnpm install
```

### 開発サーバー起動

```bash
npm run dev
# または
yarn dev
# または
pnpm dev
# または
bun dev
```

ブラウザで [http://localhost:3000](http://localhost:3000) を開いて結果を確認してください。

`app/page.tsx` を編集することでページを変更できます。ファイルを編集すると自動的にページが更新されます。

## 開発

### コマンド

```bash
# 開発サーバー起動
npm run dev

# ビルド
npm run build

# 本番サーバー起動
npm run start

# リント
npm run lint

# テスト実行
npm run test

# プロパティベーステスト
npm run test:properties
```

### ディレクトリ構成

```
frontend/
├── src/
│   ├── app/                    # App Router
│   │   ├── (public)/          # 公開ページグループ
│   │   ├── (admin)/           # 管理画面グループ
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/            # 再利用可能コンポーネント
│   │   ├── ui/               # 基本UIコンポーネント
│   │   ├── layout/           # レイアウト関連
│   │   ├── portfolio/        # ポートフォリオ特化
│   │   └── blog/             # ブログ関連
│   ├── hooks/                # カスタムフック
│   ├── lib/                  # ライブラリ・設定
│   ├── types/                # TypeScript型定義
│   └── utils/                # ユーティリティ関数
├── public/                   # 静的ファイル
└── __tests__/                # テストファイル
    ├── components/
    ├── hooks/
    ├── utils/
    └── properties/           # プロパティベーステスト
```

## 機能

### 公開機能
- **プロフィール**: 写真家・エンジニア両方の専門性を表現
- **写真ポートフォリオ**: カテゴリ別写真ギャラリー、ライトボックス表示
- **エンジニアリングポートフォリオ**: 技術プロジェクト紹介
- **ブログ**: Markdown記事表示、シンタックスハイライト

### 管理機能
- **コンテンツ管理**: 記事・写真・プロジェクトの作成・編集・削除
- **認証**: AWS Cognito統合
- **画像管理**: アップロード・最適化・メタデータ編集

## デプロイ

AWS CloudFront + S3での静的サイトホスティングを想定しています。
Terraformを使用したインフラ自動化により、CI/CDパイプラインでデプロイされます。

## ライセンス

MIT License
