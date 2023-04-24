# serverless_python
サーバーレスで遊びます。

## 起動
* dockerを立ち上げる

```
docker compose up -d // dynamodb localを立ち上げる
cd serverless_python // プロジェクトディレクトリに移動
sam build
sam local start-api
```
