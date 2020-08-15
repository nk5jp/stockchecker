# 色々なお作法のメモ書き

## イメージをビルドする場合のコマンド

`docker build -t xxx/yyy:ttt https://github.com/nk5jp/stockchecker.git#ブランチ名 -f /docker/Dockerfile`

## コンテナを起動してアクセスする場合のコマンド

- `docker run -d -p 8080:80 --privileged --rm --name zzz xxx/yyy /sbin/init`
- `docker exec -it zzz /bin/bash`

## android側の開発時にide側に実施すること

[こちら](https://firebase.google.com/docs/android/setup?hl=ja#add-config-file)を元に，'android/app'配下に「google-services.json」を配置しておく．

## 初期起動時にサーバ側に実施すること

[こちら](https://firebase.google.com/docs/cloud-messaging/auth-server#provide_credentials_manually)の「認証情報を手動で提供する」を元に以下2点を実施する．
- `service-account-file.json`を入手して，サーバ内の適当なディレクトリ（例えば'/usr/bin/stockchecker/'に配置する．
- 環境変数`GOOGLE_APPLICATION_CREDENTIALS`に上記のパスを`export`で指定しておく．
  - `printenv`コマンドで，問題ないことを確認しておく． 
- `timedatectl set-timezone Asia/Tokyo`を実行してタイムゾーンをJSTに変更しておく

## 初期起動時にmysql向けに実施すること

- `sudo systemctl start mysqld.service`
- `sudo systemctl enable mysqld.service`
- `mysql_secure_installation`
- `mysql -u アカウント名 -pパスワード < /usr/bin/stockchecker/mysql/initialization.sql`

## 初期起動時にcrond向けに実施すること

- `systemctl start crond`
- `systemctl enable crond`
- `crontab -e`を実行し，定時処理を設定しておく．
  - 実体は`/var/spool/cron/アカウント名`に配置される．
  - こちらにも環境変数`GOOGLE_APPLICATION_CREDENTIALS`を設定しておく．
  - 例：`00 17 * * * /usr/local/bin/python3.7 /usr/bin/stockchecker/python/getCurrentPrice.py >> /var/log/getCurrentPrice 2>&1`
  - 例：`00 09 * * 6 /usr/bin/mysqldump -u<account> -p<password> -r /usr/bin/stockchecker/mysql/stockapp.backup --single-transaction stockapp`