import cv2
import numpy as np


def CleateGrayscale(Jpg_pass):
    im = cv2.imread('../img/original/' + Jpg_pass)

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("img/gray_img/gray_" + Jpg_pass, im_gray)

    # 閾値の設定
    threshold = 100

    # 二値化(閾値100を超えた画素を255にする。)
    ret, im_th = cv2.threshold(im_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imwrite("../img/th/" + Jpg_pass, im_th)
