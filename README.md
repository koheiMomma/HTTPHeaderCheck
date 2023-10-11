# HTTPHeaderCheck

HTTPHeaderCheckは、HTTPリクエストのヘッダとボディ情報をレスポンスとして返すシンプルなFlaskアプリケーションです。

## インストール

### 1. リポジトリのクローン

```bash
git clone https://github.com/mmmkx/HTTPHeaderCheck.git
cd HTTPHeaderCheck
```

### 2. Dockerイメージのビルド

```bash
docker build -t httpheadercheck:latest .
```

## 実行

```bash
docker run -p 5000:5000 httpheadercheck:latest
```

## 使用方法

- GETリクエスト: リクエストヘッダとクエリパラメータをJSON形式で返します。

```bash
curl http://localhost:5000?param1=value1&param2=value2
```

- POSTリクエスト: リクエストヘッダとボディをJSON形式で返します。

```bash
curl -X POST http://localhost:5000 -H "Content-Type: application/json" -d "{\"key1\": \"value1\", \"key2\": \"value2\"}"
```

## ライセンス

"HTTPHeaderCheck" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
