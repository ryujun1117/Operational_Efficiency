# 業務効率化ミニアプリ
とあるSNSプラットフォームの統計情報を自動的に取得し、表形式に整理して出力するアプリケーション

## 仕様
windows11
python3.9（仮想環境）  
chromedriver_113.*  

## 環境構築 
1. windows上にpython仮想環境を構築  
2. 各種モジュールをインストール

## 開発メモ  


仮想環境を作成→起動


仮想環境のバージョン
3.9.7 | packaged by conda-forge | (default, Sep 29 2021, 19:15:42) [MSC v.1916 64 bit (AMD64)]

クロームドライバのインストール解説記事
https://syachiku.net/windowspython-seleniumvenv/

クロームバージョン確認
chrome://settings/help
> バージョン: 113.0.5672.93（Official Build） （64 ビット）
113番台を使用する場合は"113.0.5672.63"を利用する

ドライバの一覧サイト
https://chromedriver.chromium.org/downloads

クロームドライバのインストール
> pip install chromedriver-binary==113.0.5672.63   

その他のinstall
pip install selenium
pip install bs4
pip install requests
pip install openpyxl


exe化
参考：https://camp.trainocate.co.jp/magazine/pyinstaller-python-exe/

pip install pyinstaller
pyinstaller main.py --clean --onefile
