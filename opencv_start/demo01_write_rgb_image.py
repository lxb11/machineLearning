#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np  # 科学运算库
import cv2  # 计算机视觉库


def demo01():
    """
    demo01
    :return:
    """
    # 1、实例化代表图片的列表数据
    image_list = [
        [[0, 0, 255], [0, 0, 255]],
        [[0, 255, 0], [0, 255, 0]],
        [[255, 0, 0], [255, 0, 0]],
    ]

    # 2、把列表数据转换成numpy中的个数组
    image_array = np.array(image_list)

    # 3、把转化好的数组对象写入道特定的文件中
    cv2.imwrite("./images/chrisdemo3x2.png", image_array)
    print("done\n")


def demo02():
    """
    使用opencv读取刚刚写入的图片，查看像素内容，查看形状或者说维度信息
    :return:
    """
    # 1、通过opencv库读取图片
    src = cv2.imread("images/chrisdemo3x2.png")
    # 2、查看像素内容
    print(src)
    # 3、查看维度信息
    print(src.shape)  # (3, 2, 3)


def demo03():
    """
    把彩色图像转换成灰度图像
    并看看灰度图像在计算机中是怎样表示的
    :return:
    """
    # 1、读取彩色猫图
    rgb_cat = cv2.imread("images/cat.png")
    # 2、把彩色图片转换为灰度图片
    gray_cat = cv2.cvtColor(rgb_cat, cv2.COLOR_BGR2GRAY)
    # 3、查看灰度图像的像素内容
    print(gray_cat)
    # 4、查看灰度图片的维度信息
    print(gray_cat.shape)
    # 5、保存灰度图像
    cv2.imwrite("images/cat_gray.png", gray_cat)


if __name__ == "__main__":
    # demo01()
    demo03()
