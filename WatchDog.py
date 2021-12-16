from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import grayscale
import os


class ChangeHandler(FileSystemEventHandler):
    # ファイルやフォルダが作成された場合
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを作成しました。' % filename)
        grayscale.CleateGrayscale(filepath)
    # ファイルやフォルダが更新された場合

    def on_modified(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを変更しました。' % filename)

    # ファイルやフォルダが移動された場合
    def on_moved(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを移動しました。' % filename)

    # ファイルやフォルダが削除された場合
    def on_deleted(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%sを削除しました。' % filename)


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

    except KeyboardInterrupt:

        # 監視の終了
        observer.stop()

        # スレッド停止を待つ
        observer.join()

        # 終了ログ
        print('フォルダ・ファイル監視スクリプトを終了します。')
