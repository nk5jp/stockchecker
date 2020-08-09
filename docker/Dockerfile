FROM centos:latest

# yumの更新
RUN yum install -y sudo
RUN sudo yum -y update

# yum経由で必要資材の取得
RUN yum install -y gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel make

# ソースコードの入手
RUN curl -O https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz

# 展開
RUN tar xf Python-3.7.3.tgz

# ビルド
WORKDIR ./Python-3.7.3
RUN ./configure --enable-optimizations
RUN make
RUN sudo make altinstall

# ファイルの削除
WORKDIR /
RUN rm -f Python-3.7.3.tgz
RUN rm -rf Python-3.7.3

# pipおよびモジュールのインストール
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python3.7
RUN pip install requests
RUN pip install firebase-admin
# RUN sudo yum -y install epel-release たぶん意味ない
RUN yum install -y python36-devel mysql-devel
RUN pip install mysqlclient
#numpyのインストール
RUN pip install numpy

# mysqlのインストール
RUN yum install -y https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
RUN yum install -y mysql-server

# cronのインストール
RUN yum install -y cronie

# 認証方式の変更
RUN echo 'default-authentication-plugin = mysql_native_password' >> /etc/my.cnf

# ディレクトリの作成と資材コピー
WORKDIR /
RUN mkdir /usr/bin/stockchecker/
COPY ../python/ /usr/bin/stockchecker/
COPY ../mysql/ /usr/bin/stockchecker/
COPY ../security/ /usr/bin/stockchecker/
COPY .exrc /root/

# 環境変数の設定
ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/bin/stockchecker/security/service-account-file.json"
ENV STOCK_PYTHON_PATH="/usr/bin/stockchecker/python/"

# タイムゾーンの修正
RUN timedatectl set-timezone Asia/Tokyo