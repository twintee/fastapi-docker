# fastapi-docker

## 📚 概要
私用で作ったfastapiノード作成用docker-composeとその他諸々
dbのmasterノードとslaveノード（複数の設定が可能）

## 🌏 検証環境

- ubuntu :20.04lts

## ⚙ 使用法

- ノード生成
    1. (初回のみ)イメージ作成  
        `docker-compose build`
    1. 設定変更
        * `.env`の修正
            * PORT_API : fastapi用ポートフォワード先（初期値8000)
            * DOMAIN : virtualhostの設定ドメイン（初期値fastapi.localhost)
    1. コンテナ生成
        `python3 init.py`  

- dbの接続先は`api/app/mysql/db.py`を修正
