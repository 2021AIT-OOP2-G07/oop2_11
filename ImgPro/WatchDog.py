from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import Grayscale
import os
import Waku2
import CannyFilter


class ChangeHandler(FileSystemEventHandler):
    # 画像追加処理
    def on_created(self, event):
        # /.../.../.../filename.jpg
        filepath = event.src_path
        # filename.jpg
        filename = os.path.basename(filepath)
        print('%sが追加されました。' % filename)
        Grayscale.CleateGrayscale(filename)
        CannyFilter.edge(filename)
        Waku2.Createwaku(filename)


# メイン処理
if __name__ == '__main__':

    # 起動ログ
    print('フォルダ・ファイル監視スクリプトを起動します。')
    # 現在のフォルダパスを取得する(プログラムが実行されているフォルダパス)
    current_directory = "../img/original/"
    # インスタンス作成
    event_handler = ChangeHandler()
    observer = Observer()

    # フォルダの監視
    observer.schedule(event_handler, current_directory, recursive=True)

    # 監視の開始
    observer.start()

    try:
        # 無限ループ
        while True:
            # 待機
            time.sleep(0.05)
    # Ctrl-C をキャッチ
    except KeyboardInterrupt:

        # 監視の終了
        observer.stop()

        # スレッド停止を待つ
        observer.join()

        # 終了ログ
        print('フォルダ・ファイル監視スクリプトを終了します。')
