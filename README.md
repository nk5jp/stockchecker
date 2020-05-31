# 色々なお作法のメモ書き

## イメージをビルドする場合のコマンド

`docker build -t xxx/yyy https://github.com/nk5jp/stockchecker.git#ブランチ名:docker`

## コンテナを起動してアクセスする場合のコマンド

- `docker run -d -p 8080:80 --privileged --rm --name zzz xxx/yyy /sbin/init`
- `docker exec -it zzz /bin/bash`

## android側の開発時にide側に実施すること

[こちら](https://firebase.google.com/docs/android/setup?hl=ja#add-config-file)を元に，'android/app'配下に「google-services.json」を配置しておく．

## 書記起動時にサーバ側に実施すること

[こちら](https://firebase.google.com/docs/cloud-messaging/auth-server#provide_credentials_manually)の「認証情報を手動で提供する」を元に以下2点を実施する．
- `service-account-file.json`を入手して，サーバ内の適当なディレクトリ（例えば'/usr/bin/stockchecker/'に配置する．
- 環境変数に上記のパスを指定しておく．
  - `printenv`コマンドで，問題ないことを確認しておく． 

## 初期起動時にmysql向けに実施すること

- `sudo systemctl start mysqld.service`
- `sudo systemctl enable mysqld.service`
- `mysql_secure_installation`
- `mysql -u アカウント名 -pパスワード < /usr/bin/stockchecker/mysql/initialization.sql`

## 初期起動時にcrond向けに実施すること

- `systemctl start crond`
- `systemctl enable crond`