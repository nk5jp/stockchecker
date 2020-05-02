# 色々なお作法のメモ書き

## イメージをビルドする場合のコマンド

`docker build -t xxx/yyy https://github.com/nk5jp/stockchecker.git#ブランチ名:docker`

## コンテナを起動してアクセスする場合のコマンド

- `docker run -d -p 8080:80 --privileged --rm --name zzz xxx/yyy /sbin/init`
- `docker exec -it zzz /bin/bash`

## 初期起動時にmysql向けに実行すること

- `sudo systemctl start mysqld.service`
- `sudo systemctl enable mysqld.service`
- `mysql_secure_installation`

