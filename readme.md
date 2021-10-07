# 環境
Python 3.8 32bit

Python 3.9 64bit だと実行時に必要なdllが組み込まれないらしくエラーで動かない。 64bit版が悪そう。

# 実行ファイル化
pyinstaller <<ファイル名>> --onefile