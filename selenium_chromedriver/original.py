# python3
import sys
sys.path.append("venv\Lib\site-packages")
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
import datetime

def make_stat(soup: str) -> tuple:

    # html = "/content/drive/MyDrive/2023/業務連携/技術道場/test.html"
    # f = open(html, "r", encoding="utf-8")
    # soup = BeautifulSoup(f, 'html.parser')

    # 必要な大枠を抽出
    tmp = soup.find("div", class_="o-statsContent__notesList")

    # 最新集計時刻とタイトルがspanタグに含まれている
    spanlist = [x.text.strip() for x in tmp.find_all("span")]
    # 最新集計時刻の取得 今回は1つ目の要素に対応
    noteListUpdatetime = spanlist[1]
    # 記事のタイトルリストを取得
    noteTitleList = spanlist[3:]
    print("最新集計時刻", noteTitleList)

    # 統計的な数値を取得
    tableStat = tmp.find("table", class_="o-statsContent__table")
    view = [x.text.strip() for x in tableStat.find_all("td", class_="o-statsContent__tableStat o-statsContent__tableStat--type_view")]
    comment= [x.text.strip() for x in tableStat.find_all("td", class_="o-statsContent__tableStat o-statsContent__tableStat--type_comment")]
    suki = [x.text.strip() for x in tableStat.find_all("td", class_="o-statsContent__tableStat o-statsContent__tableStat--type_suki")]

    # dfにまとめる
    df = pd.DataFrame({
        "タイトル": noteTitleList,
        "ビュー": view,
        "コメント": comment,
        "スキ": suki
    })
    
    return (noteListUpdatetime, df)