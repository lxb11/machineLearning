#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor, Ridge, LogisticRegression
from sklearn.metrics import mean_squared_error, classification_report, roc_auc_score
import joblib


def liner1():
    """
    正规方程的优化方法对波士顿房价进行预测
    :return:
    """
    # 1) 获取数据
    boston = load_boston()
    print("特征数量：\n", boston.data.shape)

    # 2) 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)

    # 3) 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4) 预估器
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)
    # 5) 得出模型
    print("正规方程-权重系数为：\n", estimator.coef_)
    print("正规方程-偏置为：\n", estimator.intercept_)

    # 6) 模型评估
    y_predict = estimator.predict(x_test)
    print("预测房价： \n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("正规方程-均方误差为：\n", error)

    return None


def liner2():
    """
    梯度下降的优化方法对波士顿房价进行预测
    :return:
    """
    # 1) 获取数据
    boston = load_boston()
    print("特征数量：\n", boston.data.shape)

    # 2) 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)

    # 3) 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4) 预估器
    estimator = SGDRegressor(learning_rate="constant", eta0=0.01, max_iter=10000)
    estimator.fit(x_train, y_train)
    # 5) 得出模型
    print("梯度下降-权重系数为：\n", estimator.coef_)
    print("梯度下降-偏置为：\n", estimator.intercept_)

    # 6) 模型评估
    y_predict = estimator.predict(x_test)
    print("预测房价： \n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("梯度下降-均方误差为：\n", error)

    return None


def liner3():
    """
    岭回归对波士顿房价进行预测
    :return:
    """
    # 1) 获取数据
    boston = load_boston()
    print("特征数量：\n", boston.data.shape)

    # 2) 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)

    # 3) 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4) 预估器
    estimator = Ridge(alpha=0.5, max_iter=10000)
    estimator.fit(x_train, y_train)
    # 5) 得出模型
    print("岭回归-权重系数为：\n", estimator.coef_)
    print("岭回归-偏置为：\n", estimator.intercept_)

    # 6) 模型评估
    y_predict = estimator.predict(x_test)
    print("预测房价： \n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("岭回归-均方误差为：\n", error)

    return None


def cancer_demo():
    """
    逻辑回归cancer_demo
    :return:
    """
    # 1、读取数据
    path = "D:/pyhtonProject/Machine_Learning/resources/cancer/breast-cancer-wisconsin.data"
    column_name = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                   'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                   'Normal Nucleoli', 'Mitoses', 'Class']
    data = pd.read_csv(path, names=column_name)
    data.head()
    # 2、缺失值处理
    # 1）替换 -> np.nan
    data = data.replace(to_replace="?", value=np.nan)
    # 2）删除缺失样本
    data.dropna(inplace=True)
    # 不存在缺失值
    print(data.isnull().any())

    # 3、划分数据集
    # 筛选特征值和目标值
    x = data.iloc[:, 1:-1]
    y = data["Class"]
    x.head()
    y.head()
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    x_train.head()
    # 4、标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 5、预估器流程
    # estimator = LogisticRegression()
    # estimator.fit(x_train, y_train)

    # 保存模型
    # joblib.dump(estimator, "./my_ridge.pkl")
    # 加载模型
    estimator = joblib.load("./my_ridge.pkl")

    # 逻辑回归的模型参数：回归系数和偏置
    print("逻辑回归-回归系数：\n", estimator.coef_)
    print("逻辑回归-偏置：\n", estimator.coef_)

    # 6) 模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)
    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    # 查看精确率、召回率、F1-score
    report = classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"])
    print("report: \n", report)
    # y_true： 每个样本的真实类别，必须为0（反例），1（正例）标记
    # 将y_test 转换成 0 1
    y_true = np.where(y_test > 3, 1, 0)
    score = roc_auc_score(y_true, y_predict)
    print("roc_auc_score: \n", score)
    return None


if __name__ == "__main__":
    # 代码1：正规方程的优化方法对波士顿房价进行预测
    # liner1()
    # 代码2： 梯度下降的优化方法对波士顿房价进行预测
    # liner2()
    # 代码3： 岭回归对波士顿房价进行预测
    # liner3()
    # 逻辑回归cancer_demo
    cancer_demo()
