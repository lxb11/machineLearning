#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

import numpy as np


# NumPy的ndarray：一种多维数组对象
def demo01():
    """
    基于NumPy的算法要比纯Python快10到100倍（甚至更快），并且使用的内存更少。
    :return:
    """
    my_arr = np.arange(1000000)
    my_list = list(range(1000000))
    a = time.time_ns()
    for _ in range(10): my_arr2 = my_arr * 2
    b = time.time_ns()
    for _ in range(10): my_list2 = [x * 2 for x in my_list]
    c = time.time_ns()
    print(b - a, 'ns')
    print(c - b, 'ns')

    return None


def demo02():
    """
    NumPy的ndarray：一种多维数组对象
    :return:
    """
    data = np.random.randn(2, 3)
    print(data)
    print(data * 10)
    print(data + data)
    print(data.shape)
    print(data.dtype)
    return None


def demo03():
    """
    创建ndarray
    :return:
    """
    # 创建数组最简单的办法就是使用array函数。它接受一切序列型的对象（包括其他数组），
    # 然后产生一个新的含有传入数据的NumPy数组。以一个列表的转换为例
    data1 = [6, 7.5, 8, 0, 1]
    arr1 = np.array(data1)
    print(arr1)
    # 嵌套序列（比如由一组等长列表组成的列表）将会被转换为一个多维数组
    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2)
    print(arr2)
    # 因为data2是列表的列表，NumPy数组arr2的两个维度的shape
    # 是从data2引入的。可以用属性ndim和shape验证
    print(arr2.ndim)
    print(arr2.shape)
    # 除非特别说明（稍后将会详细介绍），np.array会
    # 尝试为新建的这个数组推断出一个较为合适的数据类型。
    # 数据类型保存在一个特殊的dtype对象中。比如说，在上面的两个例子中，我们有
    print(arr1.dtype)
    print(arr2.dtype)
    # 除np.array之外，还有一些函数也可以新建数组。
    # 比如，zeros和ones分别可以创建指定长度或形状的全0或全1数组。
    # empty可以创建一个没有任何具体值的数组。要用这些方法创建多维数组，
    # 只需传入一个表示形状的元组即可
    print(np.zeros(10))
    print(np.zeros((3, 6)))
    # 注意：认为np.empty会返回全0数组的想法是不安全的。
    # 很多情况下（如前所示），它返回的都是一些未初始化的垃圾值。
    print(np.empty((2, 3, 2)))
    # 注意：认为np.empty会返回全0数组的想法是不安全的。
    # 很多情况下（如前所示），它返回的都是一些未初始化的垃圾值。
    print(np.arange(15))
    return None


if __name__ == "__main__":
    # demo01()
    # demo02()
    demo03()