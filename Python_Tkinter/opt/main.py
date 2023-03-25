# coding: utf-8
#! /usr/bin/env python


# tkinterのインポート
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText



def go_2():
    global frame_app
    frame_app.destroy()
    global frame_app_2
    frame_app_2.destroy()

    # メインフレームの作成と設置
    frame_app = tk.Frame(root, width=600, height=450, bg="black")

    # 各種ウィジェットの作成
    label1_frame_app = ttk.Label(frame_app, text= u"情報",font=("Meiryo", "40", "bold"),foreground='white', background='black')
    entry1_frame_app = ScrolledText(frame_app, font=("", 15), height=10, width=60)
    button_change_frame_app = tk.Button(frame_app, text=u'予測！', foreground='black', background='white', font=("Meiryo", "20", "bold"), command=go_3)
    frame_app.pack()
    frame_app.propagate(0)
    # 各種ウィジェットの設置
    label1_frame_app.pack(anchor="center", expand=1)
    entry1_frame_app.pack(anchor="center", expand=1)
    button_change_frame_app.pack(anchor="center", expand=1)

def go_3():
    global frame_app
    global frame_app_2
    frame_app.destroy()
    # メインフレームの作成と設置
    frame_app = tk.Frame(root, width=600, height=350, bg="black")
    frame_app_2 = tk.Frame(root, width=600, height=100, bg="black")
    tree = ttk.Treeview(frame_app)
    # 列インデックスの作成
    tree["columns"] = (1,2,3)
    # 表スタイルの設定(headingsはツリー形式ではない、通常の表形式)
    tree["show"] = "headings"
    # 各列の設定(インデックス,オプション(今回は幅を指定))
    tree.column(1,width=75)
    tree.column(2,width=75)
    tree.column(3,width=100)
    # 各列のヘッダー設定(インデックス,テキスト)
    tree.heading(1,text=u"順位")
    tree.heading(2,text=u"項目")
    tree.heading(3,text=u"確率")
    # レコードの作成
    # 1番目の引数-配置場所（ツリー形式にしない表設定ではブランクとする）
    # 2番目の引数-end:表の配置順序を最下部に配置
    #             (行インデックス番号を指定することもできる)
    # 3番目の引数-values:レコードの値をタプルで指定する
    tree.insert("","end",values=("1",u"い",0.30))
    tree.insert("","end",values=("2",u"ろ",0.15))
    tree.insert("","end",values=("3",u"は",0.01))

    # 各種ウィジェットの作成
    label1_frame_app = ttk.Label(frame_app, text=u"予測結果",font=("Meiryo", "40", "bold"),foreground='white', background='black')
    entry1_frame_app = tk.Button(frame_app_2, text=u'確定入力！', foreground='black', background='white', font=("Meiryo", "20", "bold"), command=go_4)
    button_change_frame_app = tk.Button(frame_app_2, text=u'もどる', foreground='black', background='white', font=("Meiryo", "20", "bold"), command=go_2)
    frame_app.pack()
    frame_app.propagate(0)
    frame_app_2.pack()
    frame_app_2.propagate(0)
    # 各種ウィジェットの設置
    label1_frame_app.pack(anchor="center", expand=1 )
    tree.pack(anchor="center", expand=1 )
    entry1_frame_app.pack(side=tk.RIGHT)
    button_change_frame_app.pack(side=tk.LEFT)


def go_4():
    global frame_app
    frame_app.destroy()
    global frame_app_2
    frame_app_2.destroy()
    # メインフレームの作成と設置
    frame_app = tk.Frame(root, width=600, height=450, bg="black")
    # 各種ウィジェットの作成
    label1_frame_app = ttk.Label(frame_app, text=u"確定",font=("Meiryo", "40", "bold"),foreground='white', background='black')
    entry1_frame_app = ttk.Entry(frame_app, font=("", 30))
    button_change_frame_app =tk.Button(frame_app, text=u'登録', foreground='black', background='white', font=("Meiryo", "20", "bold"), command=go_5)
    frame_app.pack()
    frame_app.propagate(0)
    # 各種ウィジェットの設置
    label1_frame_app.pack(anchor="center", expand=1)
    entry1_frame_app.pack(anchor="center", expand=1)
    button_change_frame_app.pack(anchor="center", expand=1)

def go_5():
    global frame_app
    frame_app.destroy()
    # メインフレームの作成と設置
    frame_app = tk.Frame(root, width=600, height=450, bg="black")
    # 各種ウィジェットの作成
    label1_frame_app = tk.Label(frame_app, text=u'ご利用いただきありがとうございました',foreground='white', background='black', font=("Meiryo", "20", "bold"))
    button_change_frame_app =tk.Button(frame_app, text=u'最初に戻る', foreground='black', background='white', font=("Meiryo", "20", "bold"), command=restart)
    frame_app.pack()
    frame_app.propagate(0)
    # 各種ウィジェットの設置
    label1_frame_app.pack(anchor="center", expand=1)
    button_change_frame_app.pack(anchor="center", expand=1)

def restart():
    global frame_app
    frame_app.destroy()
    frame_app = tk.Frame(root, width=600, height=450, bg="black")
    label1_frame = tk.Label(frame_app, text=u'ばぁーん( ^ ^ )',foreground='white', background='black', font=("Meiryo", "70", "bold"))
    button_change = tk.Button(frame_app,text=u'はじめる', foreground='black', background='white', font=("Meiryo", "20", "bold"), command=go_2)
    frame_app.pack()
    frame_app.propagate(0)
    label1_frame.pack(anchor="center", expand=1)
    button_change.pack(anchor="center", expand=1)


if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title("DEMO")
    root.geometry("600x450")
    root.configure(bg="black")
    frame_app = tk.Frame(root, width=600, height=450, bg="black")
    frame_app_2 = tk.Frame()
    label1_frame = tk.Label(frame_app, text=u'ばぁーん( ^ ^ )',foreground='white', background='black', font=("Meiryo", "70", "bold"))
    button_change = tk.Button(frame_app,text=u'はじめる', foreground='black', background='white', font=("Meiryo", "20", "bold"), command=go_2)
    frame_app.pack()
    frame_app.propagate(0)
    label1_frame.pack(anchor="center", expand=1)
    button_change.pack(anchor="center", expand=1)
  

    root.mainloop()