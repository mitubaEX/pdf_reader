# -*- coding: utf-8 -*-
import cv2
import os
import sys
import commands
import glob
import re

i = 0
scriptpath = os.path.dirname(os.path.abspath(__file__))
os.system("rm "+scriptpath+"/image/*.jpg")
filename = sys.argv[1].replace(" ","\ ").replace("(","\(").replace(")","\)")
pwd = os.getcwd()
os.system("cp "+pwd+"/"+filename+" "+ scriptpath+"/image")
os.chdir(scriptpath+"/image")
os.system("ruby "+scriptpath+"/image/extract_image.rb "+scriptpath+"/image/"+filename)

# jpgファイルを取得
tmp = glob.glob("*.jpg")
# 数字部分を抽出してグループ化
tmp_ = [(re.search("[0-9]+", x).group(), x) for x in tmp]
#
tmp_.sort(cmp = lambda x, y:cmp(int(x[0]), int(y[0])))
#
tmp = [x[1] for x in tmp_]
im = cv2.imread(tmp[0])
cv2.namedWindow("result", cv2.WINDOW_NORMAL)
cv2.resizeWindow("result",2040,770)
cv2.imshow("result", im)
while True:
    key_num = cv2.waitKey(0)
    if key_num == 63235:
        cv2.destroyAllWindows()
        i += 1
        if i > len(tmp) - 1:
            i = 0
        im = cv2.imread(tmp[i])
        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("result",2040,770)
        cv2.imshow("result", im)
    elif key_num == 63234:
        cv2.destroyAllWindows()
        i -= 1
        if i < 0:
            i = len(tmp) -1
        im = cv2.imread(tmp[i])
        cv2.namedWindow("result", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("result",2040,770)
        cv2.imshow("result", im)

    elif key_num == 63232:
        break;

