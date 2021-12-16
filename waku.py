import cv2

#カスケード型識別機の読み込み
cascade_path = "./haarcascade_frontalface_default.xml"
#カスケード識別機のファイルパス
cascade=cv2.CascadeClassifier(cascade_path)

#?
#VideoCapture オブジェクトの取得
capture = cv2.imread('./img/test.jpg')


try:
    while(True):
        #フレームの読み取り
        ret,frame = capture.read()
        #グレースケール変換
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #顔の学習データ精査
        front_face_list=cascade.detectMultiScale(gray,minSize=(50,50))

        print(front_face_list)
        #認識しない場合はコマンドラインに"failed"と出力
        #？
        if len(front_face_list) ==0:
            print("Failed")
            cv2.waitKey(100)
            continue

        #顔を四角で囲みwindowに表示する
        for(x,y,w,h) in front_face_list:
            cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,255),thickness=5)
            cv2.imshow("frame_orig",gray)
            cv2.waitKey(100)
        cv2.waitKey(10)
except:
    cv2.destroyWindow("Window")
