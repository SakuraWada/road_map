# ベースイメージ
FROM python:3.12

# 環境変数を設定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを設定
RUN mkdir /code
WORKDIR /code

# 依存関係をインストール
RUN pip install --upgrade pip && \
    pip install pipenv
COPY ./Pipfile ./Pipfile.lock /code/
RUN pipenv install --system

# プロジェクトファイルをコピー
COPY . /code/