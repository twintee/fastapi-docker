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
    1. コンテナ生成
        `python3 init.py`  
        - 応答は基本'y'でボリュームやlogの削除は都度判断。dumpはスクリプトから制御しない。
        - nodeの種類を切り替えたい場合`config.py`を事前に実行してから、生成スクリプトを実行。
        - 1ホストでmaster/slave構成したい場合  
        `python3 init.py all`  

- dbのホストを変更する場合`api/app/mysql/db.py`を修正
