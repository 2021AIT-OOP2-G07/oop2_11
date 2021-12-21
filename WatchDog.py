from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import grayscale
import os
import waku


class ChangeHandler(FileSystemEventHandler):
    # 画像追加処理
    def on_created(self, event):
        # /.../.../.../filename.jpg
        filepath = event.src_path
        # filename.jpg
        filename = os.path.basename(filepath)
        print('%sが追加されました。' % filename)
        grayscale.CleateGrayscale(filename)
        waku.Createwaku(filename)


# メイン処理
if __name__ == '__main__':

    # 起動ログ
    print('フォルダ・ファイル監視スクリプトを起動します。')

    # 現在のフォルダパスを取得する(プログラムが実行されているフォルダパス)
    current_directory = os.path.dirname(os.path.abspath(__file__))

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
