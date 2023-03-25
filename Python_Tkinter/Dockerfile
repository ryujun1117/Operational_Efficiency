# 最低限必要な部分だけ抜粋
FROM python:3.8.2

# Japanese
RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL=ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8
RUN apt-get install -y fonts-migmix
RUN pip install pysimplegui

