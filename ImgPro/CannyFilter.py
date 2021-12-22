
import cv2
import sys

print(sys.path)
# CannyFilter.edge(グレースケールの画像, 名前) でエッジ抽出をした画像を
# 引数nameの名前で、img/edge_imgに保存するプログラムです。

# 使用例：CannyFilter.edge(gray_img, name)
# 引数nameに拡張子を含めてください。(a.jpg, b.png など)


def edge(Jpg_pass):
    im = cv2.imread('../img/original/' + Jpg_pass)
    grayImg = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    threshold1 = 180
    threshold2 = 360
    edgeImg = cv2.Canny(grayImg, threshold1, threshold2)
    cv2.imwrite('../img/Canny/cannyFilter' + Jpg_pass, edgeImg)
