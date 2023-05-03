# チャットアプリ

## ディレクトリ構成
```
Chat
  ├─chat_app
  |   ├─templates
  |   |   └─top.html
  |   ├─apps.py
  |   ├─urls.py
  |   └─views.py
  |
  ├─chat_project
  |   ├─settings.py
  |   ├─urls.py
  |   └─wsgi.py
  |   
  ├─db.splite3
  ├─manage.py
  ├─README.md
  └─requirements.txt
```

## 仮想環境有効化手順
```bash
# on Terminal

# プロジェクトディレクトリへ移動
cd RealtimeChat

# 仮想環境有効化
source venv/bin/activate
```

## ローカルサーバー起動手順
```bash
# on Terminal

# プロジェクトディレクトリへ移動
(venv)$ cd RealtimeChat

# ローカルサーバー起動
(venv)$ python3 manage.py runserver

# access to http://127.0.0.1:8000/
```

## ライブラリインストール手順
```bash
# on Terminal

# requirements.txtに記載されているライブラリをインストール
pip install -r requirements.txt
```

## 仮想環境無効化手順
```bash
# on Terminal

# 仮想環境無効化
(venv)$ deactivate
```