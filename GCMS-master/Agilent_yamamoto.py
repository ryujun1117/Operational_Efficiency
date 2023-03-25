#!python3
#山本研の液クロのピークを読み込むプログラム

import os
import csv
#対話型
print("読み込みフォルダ名を入力")
x = str(input())
print("出力ファイル名を入力（.csv必須）")
filename = str(input())
#ファイル操作。ファイル数（試料数）の測定
os.chdir(x)
path=os.getcwd()
files=os.listdir(path)
#処理回数（ファイル数）をcountにわたす
count= len(files)
output_file = open("C:\\Users\\ryuichi1117\\LC_project\\"+filename,"a",newline="")
output_writer = csv.writer(output_file)
output_writer.writerow("sample:" + str(count))
m = ["ﾋﾟｰｸ","RT","ﾀｲﾌﾟ","ﾋﾟｰｸ幅","面積","面積%","化合物名"]
output_writer.writerow(m)

for i in range(count):
    #try文で下位ディレクトリ内にのReport.txtが存在するときに実行
    try:
        #---titleversion---タイトル行の抽出
        hello_file = open(".\\" + files[i] + "\\Report.txt",encoding = "utf-16")
        hello_content = hello_file.read()
        #headとtailで挟まれた部分を文字列として抽出
        head = "サンプル名 : "
        tail = "\n"
        extraction = hello_content.split(head)[-1].split(tail)[0]
        extraction.replace(" ","")
        box = []
        box.append(extraction)
        #csvファイルに書き込み
        output_writer.writerow(box)
        #タイトル記入終了
        hello_file.close()
#ここまで修正済み↑
        #---dataversion---データ行の抽出
        hello_file = open(".\\" + files[i] + "\\Report.txt",encoding = "utf-16")
        hello_content = hello_file.read()
        hello_replaced = hello_content.replace("\n\n\n",",").split(",")
        #new!! 特定の文字列が含まれている要素の抽出
        line = []
        for j in range(len(hello_replaced)):
            hello_replaced_content = hello_replaced[j]
            content = "----|-------|------|-------|----------|--------|---------------------" in hello_replaced_content
            if content == True:
                line.append(hello_replaced_content)
        del line[-1]
        #headとtailで挟まれた部分を文字列として抽出
        head = "\n----|-------|------|-------|----------|--------|---------------------\n"
        tail = "\nトータル"
        line2 = []
        for k in range(len(line)):
            line_content = line[k]
            extraction = line_content.split(head)[-1].split(tail)[0]
            line2.append(extraction)
        #peak6:2データの処理
        two = line2[4].split("\n")
        line2[4] = two[0]
        line2.insert(5,two[1])
            
        #forぶん回しながら出力も一緒にやっていく
        for l in range(len(line2)):
            output = line2[l]
            result = output.strip().split()
            output_writer.writerow(result)
        
        output_writer.writerow("ピーク数:" + str(len(line2)))
        hello_file.close()

    except:
        continue
        
print("completed")