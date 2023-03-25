# TkinterをDocker上で使ってみた

windowsの実機上で構築する分にはPythonの仮想環境を用意すれば割と簡単に動く  
*環境*
windows：
Docker desktop

## 準備
Dockerコンテナを利用をするにあたって、以下が必要。
* VcXsrv Windows X Server  https://sourceforge.net/projects/vcxsrv/

## Docker構築
コード例
```
docker compose up -d --build
docker compose exec [コンテナ名] bash
```

## 実行前に...

DockerコンテナのDISPLAYの環境変数の設定が必要
```
export DISPLAY=[IPアドレス]:x.0
```
* IPアドレス：ipconfigで確認。使用する回線ごとに変化するので注意
* x：x window systemの表示を確認する
