import cv2

# CannyFilter.edge(グレースケールの画像, 名前) でエッジ抽出をした画像を
# 引数nameの名前で、img/edge_imgに保存するプログラムです。

# 使用例：CannyFilter.edge(gray_img, name)
# 引数nameに拡張子を含めてください。(a.jpg, b.png など)
def edge(grayImg, name):
    threshold1 = 180
    threshold2 = 360
    edgeImg = cv2.Canny(grayImg, threshold1, threshold2)
    cv2.imwrite('img/edge_img/' + name, edgeImg)