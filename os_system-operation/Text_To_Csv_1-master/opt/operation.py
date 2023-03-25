#python3

import os
import csv
import datetime

#関数化
#空白対策が必要
#変数の命名"抽出"
def text_sampling():
    with open("report.txt", "r") as f:
        data = f.read()
    #l→lineにする
    line = data.split("\n")
    mydict = {
    }
    for i in range(len(line)):
        #tmpは変える
        tmp = line[i].split("：")
        #何を取るのか
        try:
            KEY = tmp[0]
            VALUE = tmp[1]
        except:
            KEY = "error"
            VALUE = "error"
        #：がなくてtmp[1]が存在しない場合エラー処理
        mydict[KEY]=VALUE
    return mydict
# tmp = line[0].split(":")
# tmp
#csvの出力
#csvファイルを作成する（最初のみ実行）
def create_csv(mydict):
    now = datetime.datetime.now()
    filename = "report.csv"
    with open(filename, "w",encoding="cp932") as f:
        writer = csv.writer(f)
        writer.writerow(mydict.keys())

#csvファイルに追記する（2回目以降の実行）
def add_info(mydict):
    now = datetime.datetime.now()
    filename = "report.csv"
    while(1):
        now_str = datetime.datetime.now().strftime("%Y%m%d")

        with open(filename, "a",encoding="cp932") as f:
            writer = csv.writer(f)
            writer.writerow(mydict.values())
        break
    print("finish")

info = text_sampling()
File_Exists = os.path.isfile("report.csv")
if File_Exists == False:
    create_csv(info)
add_info(info)