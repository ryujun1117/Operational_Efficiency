#Dockerfileはイメージを作るモノ。
#ネットワーク・ボリュームは作成できない
#取得するイメージを指定する
# FROM python:3
# #ユーザー名を指定
# USER root
# #パッケージのインストール
# RUN apt-get update
# #日本語化のためのパッケージのインストール→しないと文字化けする
# RUN apt-get -y install locales && \
#     localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
# #環境変数の設定（日本語化・）
# ENV LANG ja_JP.UTF-8
# ENV LANGUAGE ja_JP:ja
# ENV LC_ALL ja_JP.UTF-8
# #タイムゾーンの設定
# ENV TZ JST-9
# #とりあえず指定しておく
# ENV TERM xterm
# #vimのインストール（理由は不明）
# RUN apt-get install -y vim less
# #pythonのモジュールのアップデート
# RUN pip install --upgrade pip
# RUN pip install --upgrade setuptools
# #dash・pandasモジュールの追加
# RUN pip install dash
# RUN pip install pandas
# RUN pip install streamlit

# EXPOSE 8001
# CMD ["bash"]

FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# RUN pip install dash
# RUN pip install pandas
# RUN pip install streamlit

EXPOSE 8001
CMD ["bash"]