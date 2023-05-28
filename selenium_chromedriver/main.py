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

from original import *


# noteのダッシュボードの情報を取得する
print("...noteダッシュボード情報の抽出を開始します...")

# ログイン情報を入力してもらう
print("ログインメールアドレスを入力してください")
login = input()
print("パスワードを入力してください")
password = input()

# ブラウザをheadlessモード実行
options = webdriver.ChromeOptions()
#ヘッドレスモード（バックグラウンドで起動）で実行。コラボの場合、必須。
options.add_argument('--headless')
#サンドボックスモードの解除。これも必須。
options.add_argument('--no-sandbox')
#これも設定した方がよい。
options.add_argument('--disable-dev-shm-usage')
#インスタンス化
driver = webdriver.Chrome('chromedriver',options=options)
#指定したドライバーが見つかるまで待機
driver.implicitly_wait(10)
#urlの指定
url="{target_url}"
driver.get(url)
time.sleep(3)
print("サイトのタイトルへアクセス：", driver.title)

# ユーザー名入力
driver.find_element(By.XPATH,"//*[@id='email']").send_keys(login)
# パスワード入力
driver.find_element(By.XPATH,"//*[@id='password']").send_keys(password)
# ログインボタンクリック
btn = driver.find_element(By.XPATH,"//*[@id='__layout']/div/div[1]/main/div/div[2]/div[5]/button/div")
btn.click()
print("ログイン成功...")
time.sleep(3)

# ダッシュボードに遷移
url = "{target_url}"
driver.get(url)
time.sleep(5)
# 「もっとみる」がなくなるまで押す。
more_btn = driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div[2]/div/main/div/div[3]/div/div[2]/div/div[5]/button")
try:
    while more_btn is not None:
        more_btn = driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div[2]/div/main/div/div[3]/div/div[2]/div/div[5]/button")
        print("もっとみる")
        more_btn.click()
        time.sleep(3)
except:
    pass

print("ダッシュボードの情報を保存中...")
time.sleep(3)


# 中間ファイルを作成する場合コメントオフ
# soup = str(BeautifulSoup(html, 'html.parser').decode("utf-8"))
# filename = "test.html"
# f = open(filename, "w", encoding="utf-8")
# f.write(soup)
# f.close()]
print("解析中...")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
time.sleep(5)

# 取得した情報を解析して表形式にまとめる
stat = make_stat(soup)

# エクセルファイルの作成
# 作成時の日時を取得
dt = datetime.datetime.today()
d = str(dt.date()).replace("-", "")
output_xlsx = stat[1]
output_xlsx.to_excel("WeeklyStat_" + d +".xlsx")

print("...出力完了")
print("...終了中")
time.sleep(3)

# end
