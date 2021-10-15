# -*- coding: utf-8 -*-
# @Time    : 2021-10-01 10:30
# @Author  : 薛小山
# @FileName: work.py
# @Software: PyCharm

import cv2 as cv
import os
import numpy as np
img_path = os.listdir(r"D:/pycharm/file/picture/")
save_path = "D:/pycharm/file/pic_save/"
if not os.path.exists(save_path):
    os.makedirs(save_path)
n = 1
for img in img_path:
    imgs = "D:/pycharm/file/picture/" + img
    pic = cv.imread(imgs)
    # print( imgs )
    # print(pic)
    w, h, c = pic.shape
    key = np.random.randint(0, 256, size=[w, h, c], dtype=np.uint8)
    encoder = cv.bitwise_xor(pic, key)
    pic_save_path = os.path.join(save_path, str(n)+".jpg")
    print('--加密第'+str(n)+'张图完成--')
    n += 1
    cv.imwrite(pic_save_path, encoder)
# 1、获取图片大小
# 2、生成和图片一样大小的加密码
# 3、对图片加密
# 4、把加密图片保存在 deal_img文件夹里



