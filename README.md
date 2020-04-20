# rh-demo-app
デモアプリの構築

## もとのリポジトリ
Git Repo URL : https://github.com/ysuke25/rh-demo-app.git

# 事前準備
OpenshiftにSercletを登録すること

# 見た目の変更方法
- 見た目をオレンジ色と青色に設定することが可能です。
- 基本的にMasterを変更して問題ありません。
- Webで変更する方法を記載していますが、CLIで実施しても問題ありません

## 変更方法

1. [index.html](https://github.ibm.com/demo-repo/rh-ocp-demo-app/blob/master/templates/index.html)にアクセスします。
2. 「ペン」をクリックします。
3. 以下の行を変更します(例：青→オレンジへの変更)。
   ```
   <link rel="stylesheet" href="/static/main-blue.css" type="text/css">
   ```
   ↓
   ```
   <link rel="stylesheet" href="/static/main-orange.css" type="text/css">
   ```
4. 「commit chages」に変更後の色を記載します。
5. 「commit chages」をクリックします。