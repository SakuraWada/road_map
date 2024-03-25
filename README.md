# 概要
Django公式チュートリアルのためのDocker環境

# 前提
Dockerを用いた開発では、`docker compose`というコマンドを多用するため、`dc`というコマンドが`docker compose`を意味するようにエイリアスを設定します。
まずは、次のコマンドを実行して、`.zshrc`を開いてください。
```
$ vi ~/.zshrc
```
続いて、`.zshrc`に次の1文を追記してください。
```
alias dc='docker compose'
```
最後に、次のコマンドを実行して、`.zshrc`の変更を反映させてください。
```
$ source ~/.zshrc
```
適切な設定をすると、次のコマンドで`Docker Compose version`が表示されます。
```
$ dc version
Docker Compose version v2.23.3
````

# 作業方法
## 1. イメージをビルドする
次のコマンドで、`docker-compose.yml`に記述されたサービスのビルドプロセスを実行します。
```
$ dc build --no-cache
```
ビルドを再実行した際に、キャッシュによる予期せぬエラーが発生しないようにするために、「イメージの構築時、キャッシュを使用しない」ためのオプションである`--no-cache`を使用しています。
チュートリアルに取り組むにあたり、基本的にはイメージのビルドは1度だけで問題ありません。

## 2. コンテナを作成して起動する
次のコマンドで、ビルドしたイメージからコンテナを作成して起動します。
```
$ dc up -d
```
次のコマンドを実行すると、コンテナが起動していることが分かります。
```
$ dc ps
```

## 3. Djangoアプリを作成する
次のコマンドで、実行中のコンテナ内に入ります。
```
$ dc exec app bash
```
コンテナ内で次のコマンドを実行することで、`Django==4.2`がコンテナ内にインストールされていることが分かります。
```
$ pip freeze
Django==4.2
```
[公式チュートリアル]([url](https://docs.djangoproject.com/ja/5.0/intro/tutorial01/))の指示に従って、プロジェクトを作成します。
`mysite`ではなく`mysite .`であることに注意してください。
```
$ django-admin startproject mysite .
```
コンテナ内で次のコマンドを実行することで、開発サーバーを起動します。
`0:8080`は、ポート8080で起動し、すべてのIPアドレスからの接続を受け付けるようにすることを意味します。
```
$ python manage.py runserver 0:8080
```
ホストの8080ポートをコンテナの8080ポートにマッピングしているため、`https://localhost:8080`にアクセスすると、次の画面が表示されます。
<img width="1512" alt="スクリーンショット 2024-03-25 17 32 18" src="https://github.com/Scala-partners/djangio-tutorial-DC/assets/115516552/3f106c0e-32fb-4ee0-9c14-a1eb40cde76a">

## 4. コンテナを停止する
`control + D`でコンテナを出て、次のコマンドを実行して、コンテナを停止します。
```
$ dc down
```

## 5. その他
- 次回以降、`1. イメージをビルドする`をスキップして、`2. コンテナを作成して起動する`から実行することができます
- `dokcer-compose.yml`16行目のコメントアウトを外して`dc up -d`をすると、自動で開発サーバーが起動し、`https://localhost:8080`からアクセスできるようになります

