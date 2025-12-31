# 要件文書

## はじめに

AWS上のサーバレスサービスでホストする個人ポートフォリオハブシステム。写真家とインフラエンジニア両方の専門性を洗練されたデザインでアピールし、個人情報発信とAWS環境検証のプレイグランドとして機能する。コスト効率を最優先とした従量課金型のアーキテクチャを採用する。

## 用語集

- **Portfolio_Hub_System**: 個人ポートフォリオハブシステム全体
- **Visitor**: サイト訪問者（認証不要）
- **Admin**: サイト管理者（コンテンツ作成・編集権限）
- **Blog_Post**: ブログ記事エンティティ
- **Profile_Content**: 個人紹介コンテンツ
- **Photography_Portfolio**: 写真作品ポートフォリオ
- **Engineering_Portfolio**: エンジニアリング作品・プロジェクト
- **Serverless_Infrastructure**: AWS Lambda、API Gateway、Aurora Serverless v2等のサーバレスサービス群
- **CI_CD_Pipeline**: AWS CodePipeline、CodeBuild、CodeDeployによる継続的インテグレーション・デリバリー基盤
- **Aurora_Serverless_v2**: 0 ACU対応のサーバレスPostgreSQLデータベース
- **IaC_Tool**: Infrastructure as Code ツール（TerraformまたはCloudFormation）

## 要件

### 要件 1

**ユーザーストーリー:** サイト訪問者として、写真家・エンジニア両方の専門性を表現した洗練されたプロフィール情報を閲覧したい。そうすることで、サイト運営者の多面的な才能について理解できる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL サイトのトップページに写真家・エンジニア両方の専門性を表現したプロフィール情報を表示する
2. WHEN 訪問者がプロフィールセクションにアクセスする時、THE Portfolio_Hub_System SHALL 経歴、スキル、連絡先情報を洗練されたデザインで表示する
3. THE Portfolio_Hub_System SHALL レスポンシブデザインでモバイルデバイスでも美しく表示する
4. THE Portfolio_Hub_System SHALL 3秒以内にプロフィールページを読み込む
5. THE Portfolio_Hub_System SHALL プロフェッショナルな印象を与える視覚的デザインを提供する

### 要件 2

**ユーザーストーリー:** サイト訪問者として、写真作品のポートフォリオを閲覧したい。そうすることで、写真家としての技術と芸術性を評価できる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL 写真作品をカテゴリ別に整理して表示する
2. WHEN 訪問者が写真ポートフォリオセクションにアクセスする時、THE Portfolio_Hub_System SHALL 高品質な画像表示とスムーズなナビゲーションを提供する
3. THE Portfolio_Hub_System SHALL 画像のライトボックス表示機能を提供する
4. THE Portfolio_Hub_System SHALL 各作品に撮影情報（カメラ設定、場所、日時）を表示する
5. THE Portfolio_Hub_System SHALL 画像の遅延読み込み（Lazy Loading）でページ表示速度を最適化する

### 要件 3

**ユーザーストーリー:** サイト訪問者として、エンジニアリングプロジェクトのポートフォリオを閲覧したい。そうすることで、技術的な能力と実績を評価できる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL エンジニアリングプロジェクトを技術スタック別に整理して表示する
2. WHEN 訪問者がエンジニアリングポートフォリオセクションにアクセスする時、THE Portfolio_Hub_System SHALL プロジェクト概要、使用技術、成果を表示する
3. THE Portfolio_Hub_System SHALL GitHubリポジトリやライブデモへのリンクを提供する
4. THE Portfolio_Hub_System SHALL プロジェクトのスクリーンショットや動画を表示する
5. THE Portfolio_Hub_System SHALL 技術的な詳細を分かりやすく説明する

### 要件 4

**ユーザーストーリー:** サイト訪問者として、ブログ記事一覧を閲覧したい。そうすることで、最新の投稿や過去の記事を発見できる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL ブログ記事を投稿日時の降順で一覧表示する
2. WHEN 記事一覧ページにアクセスする時、THE Portfolio_Hub_System SHALL 各記事のタイトル、投稿日、概要を表示する
3. THE Portfolio_Hub_System SHALL ページネーション機能で記事一覧を分割表示する
4. WHEN 記事タイトルをクリックする時、THE Portfolio_Hub_System SHALL 該当記事の詳細ページに遷移する

### 要件 5

**ユーザーストーリー:** サイト訪問者として、個別のブログ記事を読みたい。そうすることで、詳細な内容を理解できる。

#### 受入基準

1. WHEN 訪問者が記事詳細ページにアクセスする時、THE Portfolio_Hub_System SHALL 記事の全文、タイトル、投稿日時を表示する
2. THE Portfolio_Hub_System SHALL Markdownで記述された記事をHTMLに変換して表示する
3. THE Portfolio_Hub_System SHALL コードブロックのシンタックスハイライト機能を提供する
4. THE Portfolio_Hub_System SHALL 記事の読了時間を推定表示する

### 要件 6

**ユーザーストーリー:** サイト管理者として、新しいブログ記事を作成・公開したい。そうすることで、情報発信を継続できる。

#### 受入基準

1. WHEN 管理者が認証済みの状態で記事作成ページにアクセスする時、THE Portfolio_Hub_System SHALL 記事作成フォームを表示する
2. THE Portfolio_Hub_System SHALL タイトル、本文、タグの入力フィールドを提供する
3. WHEN 管理者が記事を保存する時、THE Portfolio_Hub_System SHALL 記事をデータベースに永続化する
4. THE Portfolio_Hub_System SHALL Markdownプレビュー機能を提供する
5. THE Portfolio_Hub_System SHALL 下書き保存機能を提供する

### 要件 7

**ユーザーストーリー:** サイト管理者として、既存の記事を編集・削除したい。そうすることで、コンテンツの品質を維持できる。

#### 受入基準

1. WHEN 管理者が認証済みの状態で記事管理ページにアクセスする時、THE Portfolio_Hub_System SHALL 全記事の一覧を表示する
2. WHEN 管理者が記事を編集する時、THE Portfolio_Hub_System SHALL 既存の内容を編集フォームに表示する
3. WHEN 管理者が記事を削除する時、THE Portfolio_Hub_System SHALL 確認ダイアログを表示する
4. THE Portfolio_Hub_System SHALL 記事の公開状態（公開/下書き）を切り替える機能を提供する

### 要件 8

**ユーザーストーリー:** サイト管理者として、写真作品とエンジニアリングプロジェクトを管理したい。そうすることで、ポートフォリオコンテンツを最新の状態に保てる。

#### 受入基準

1. WHEN 管理者が認証済みの状態でポートフォリオ管理ページにアクセスする時、THE Portfolio_Hub_System SHALL 写真・プロジェクト管理インターフェースを表示する
2. THE Portfolio_Hub_System SHALL 写真のアップロード、カテゴリ分類、メタデータ編集機能を提供する
3. THE Portfolio_Hub_System SHALL エンジニアリングプロジェクトの追加、編集、削除機能を提供する
4. THE Portfolio_Hub_System SHALL 画像の自動リサイズと最適化機能を提供する
5. THE Portfolio_Hub_System SHALL ポートフォリオアイテムの表示順序変更機能を提供する

### 要件 10

**ユーザーストーリー:** システム運用者として、コスト効率的なインフラで運用したい。そうすることで、個人プロジェクトとして持続可能な運用ができる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL AWSサーバレスサービスでホストされる
2. THE Portfolio_Hub_System SHALL アクセス数に応じた従量課金モデルで動作する
3. WHEN アクセスが無い期間、THE Portfolio_Hub_System SHALL 最小限のコストで待機状態を維持する
4. THE Portfolio_Hub_System SHALL Aurora Serverless v2（0 ACU対応）をデータストレージとして使用する
5. THE Portfolio_Hub_System SHALL CloudFrontを使用して静的コンテンツを配信する

### 要件 12

**ユーザーストーリー:** エンジニアとして、技術的な専門性をアピールできる適切な技術スタックでサイトを構築したい。そうすることで、ポートフォリオサイト自体が技術力の証明となる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL 汎用性が高く現代的なフロントエンド技術スタックで構築される
2. THE Portfolio_Hub_System SHALL エンジニアとしての技術力を示すのに適した言語・フレームワークを採用する
3. THE Portfolio_Hub_System SHALL 保守性と拡張性を考慮した技術選択を行う
4. THE Portfolio_Hub_System SHALL 学習価値が高く業界標準的な技術を使用する
5. THE Portfolio_Hub_System SHALL ソースコードをGitHubで公開し、技術選択の根拠を示す

### 要件 14

**ユーザーストーリー:** AWSエンジニアとして、AWS Codeシリーズを活用したCI/CD基盤を構築したい。そうすることで、AWSネイティブな開発・運用スキルを実績として示せる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL GitHub リポジトリとAWS CodePipeline、CodeBuild、CodeDeployを統合したCI/CDパイプラインで構築される
2. WHEN コードがGitHubリポジトリにプッシュされる時、THE Portfolio_Hub_System SHALL Webhookを通じてAWS CodePipelineを起動し、自動的にビルド・テスト・デプロイを実行する
3. THE Portfolio_Hub_System SHALL 開発・ステージング・本番環境への段階的デプロイメントを自動化する
4. THE Portfolio_Hub_System SHALL ビルド・デプロイの状況をCloudWatchで監視・ログ記録する
5. THE Portfolio_Hub_System SHALL 失敗時の自動ロールバック機能を提供する

### 要件 16

**ユーザーストーリー:** エンジニアとして、RDBMS（PostgreSQL）の設計・運用スキルを習得したい。そうすることで、NoSQLとRDBMS両方の技術を実績として示せる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL Aurora Serverless v2（PostgreSQL）でリレーショナルデータベース設計を実装する
2. THE Portfolio_Hub_System SHALL 正規化されたテーブル設計でデータ整合性を保証する
3. THE Portfolio_Hub_System SHALL SQLクエリによる効率的なデータ操作を実装する
4. WHEN アクセスが無い期間、THE Portfolio_Hub_System SHALL 0 ACUにスケールダウンしてコストを最小化する
5. THE Portfolio_Hub_System SHALL データベースのパフォーマンス監視とクエリ最適化を実装する

### 要件 17

**ユーザーストーリー:** インフラエンジニアとして、汎用性の高いIaCツールでインフラ構成管理を行いたい。そうすることで、AWS以外のクラウドでも応用可能なスキルを習得できる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL TerraformまたはCloudFormationを使用してInfrastructure as Code（IaC）で構築される
2. THE Portfolio_Hub_System SHALL 汎用性が高く業界標準的なIaCツールを採用する
3. THE Portfolio_Hub_System SHALL インフラ構成をコードで管理し、バージョン管理する
4. THE Portfolio_Hub_System SHALL 環境別（開発・ステージング・本番）の構成差分を管理する
5. THE Portfolio_Hub_System SHALL インフラの変更履歴を追跡可能にする

### 要件 18

**ユーザーストーリー:** 開発者として、AWS環境での実験・検証を行いたい。そうすることで、新しい技術やサービスを学習できる。

#### 受入基準

1. THE Portfolio_Hub_System SHALL Infrastructure as Code（IaC）で構築される
2. THE Portfolio_Hub_System SHALL 開発、ステージング、本番環境を分離する
3. WHEN 新しいAWSサービスを検証する時、THE Portfolio_Hub_System SHALL 既存機能に影響を与えずに実験環境を提供する
4. THE Portfolio_Hub_System SHALL CI/CDパイプラインでデプロイメントを自動化する