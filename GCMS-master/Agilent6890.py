#!python3
#Agilent 6890 Series GC System ピークまとめプログラム
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
output_file = open("C:\\Users\\ryuichi1117\\GC_project\\"+filename,"a",newline="")
output_writer = csv.writer(output_file)
output_writer.writerow("sample:" + str(count))
m = ["Peak[#]","RetTime[min]","Type","Width[min]","Area[pA*s]","Height[pA]","Area[%]"]
output_writer.writerow(m)

for i in range(count):
    #try文で下位ディレクトリ内にのReport.txtが存在するときに実行
    try:
        #---titleversion---タイトル行の抽出
        hello_file = open(".\\" + files[i] + "\\Report.txt")
        hello_content = hello_file.read()
        #replace関数で置換
        hello_replaced = hello_content.replace("\x00","")
        #headとtailで挟まれた部分を文字列として抽出
        head = "Sample Name: "
        tail = "\n\n"
        extraction = hello_replaced.split(head)[-1].split(tail)[0]
        #splitで区切ってリストにして抽出
        extraction_comp_t = extraction.split(" ")
        #csvファイルに書き込み
        output_writer.writerow(extraction_comp_t)
        #タイトル記入終了
        hello_file.close()

        #---dataversion---データ行の抽出
        hello_file = open(".\\" + files[i] + "\\Report.txt")
        hello_content = hello_file.read()
        hello_replaced = hello_content.replace("\x00","")
        #headとtailで挟まれた部分を文字列として抽出
        head = "%\n\n----|-------|----|-------|----------|----------|--------|\n\n"
        tail = "\n\n=====================================================================\n\n"
        extraction = hello_replaced.split(head)[-1].split(tail)[0]
        #抽出したデータの整形処理
        #\n\nを,に置き換える（1試料あたりのデータをカンマで区切る）。
        extraction_ncomp = extraction.replace("\n\n",",")
        #カンマ位置で文字列を分割しリストを作成
        extraction_nncomp= extraction_ncomp.split(",")
        #後ろから二行を削除（totalの部分）
        del extraction_nncomp[-2:]

        #type修正用(適宜編集。もれなくする。)
        extraction_nncomp_repair = []
        for i in range(len(extraction_nncomp)):
            t = extraction_nncomp[i]
            if "V T" in t:
                t = t.replace("V T", "VT")
            elif "V R" in t:
                t = t.replace("V R", "VR")
            elif "V E" in t:
                t = t.replace("V E", "VE")
            elif "B T" in t:
                t = t.replace("B T", "BT")
            elif "B R" in t:
                t = t.replace("B R", "BR")
            elif "B E" in t:
                t = t.replace("B E", "BE")
            elif "B S" in t:
                t = t.replace("B S", "BS")
            extraction_nncomp_repair.append(t)
        #結果を代入
        extraction_comp_d = extraction_nncomp_repair
        #リストを1要素ずつ読み込み→書き込み
        for i in range(len(extraction_comp_d)):
            k = extraction_comp_d[i]
            n = k.split()
            output_writer.writerow(n)
        hello_file.close()
    except:
        continue

print("completed")

