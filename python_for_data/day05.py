#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


def demo01():
    """
    Series
    :return:
    """
    obj = pd.Series([4, 7, -5, 3])
    print(obj)
    print(obj.values)
    print(obj.index)
    return None


def demo02():
    """
    整数索引
    :return:
    """
    ser = pd.Series(np.arange(3.))
    print(ser)
    # print(ser[-1]) // 会报错
    ser1 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
    print(ser1)
    print(ser1[-1])
    return None


def demo03():
    """
    DataFrame和Series之间的运算
    :return:
    """
    obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
    print(obj)
    return None


if __name__ == "__main__":
    # demo01()
    # demo02()
    demo03()
    # demo04()
    # demo05()
    # demo06()
    # demo07()
    # demo08()
    # demo09()
    # demo10()
    # demo11()
    # demo12()
