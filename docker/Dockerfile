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

# mysqlのインストール
RUN yum install -y https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
RUN yum install -y mysql-server

# 認証方式の変更
RUN echo 'default-authentication-plugin = mysql_native_password' >> /etc/my.cnf
