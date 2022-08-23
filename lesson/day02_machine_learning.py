#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier


def knn_iris():
    """
    用KNN算法对鸢尾花进行分类
    :return:
    """
    # 1）获取数据
    iris = load_iris()
    # 2）划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
    # 3）特征工程：标准化
    transfer = StandardScaler()
    # x_train = transfer.fit_transform(x_train)
    transfer.fit(x_train)
    x_train = transfer.transform(x_train)
    x_test = transfer.transform(x_test)

    # 4）KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)
    # 5）模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)
    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    return None


def knn_iris_gscv():
    """
    用KNN算法对鸢尾花进行分类
    :return:
    """
    # 1）获取数据
    iris = load_iris()
    # 2）划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)
    # 3）特征工程：标准化
    transfer = StandardScaler()
    # x_train = transfer.fit_transform(x_train)
    transfer.fit(x_train)
    x_train = transfer.transform(x_train)
    x_test = transfer.transform(x_test)

    # 4）KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)

    # 加入网格搜索与交叉验证
    # 参数准备
    param_dict = {"n_neighbors": [1, 3, 5, 7, 9, 11]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)
    estimator.fit(x_train, y_train)
    # 5）模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)
    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器：\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果：\n", estimator.cv_results_)

    return None


def knn_facebook_demo():
    """
    facebook 案例分析
    :return:
    """
    # 1、获取数据
    data = pd.read_csv("D:/pyhtonProject/Machine_Learning/resources/FBlocation/train.csv")
    data.head()
    # 2、基本数据处理
    # 1）缩小数据范围
    data = data.query("x < 2.5 & x > 2 & y < 1.5 & y > 1.0")
    # 2) 处理时间戳
    time_value = pd.to_datetime(data["time"], unit="s")
    date = pd.DatetimeIndex(time_value)
    # print(time_value)
    # print(date)
    data["day"] = date.day
    data["weekday"] = date.weekday
    data["hour"] = date.hour
    # 3) 过滤签到次数少的地点
    place_count = data.groupby("place_id").count()["row_id"]
    place_count[place_count > 3].head()
    data_final = data[data["place_id"].isin(place_count[place_count > 3].index.values)]
    # 筛选特征值和目标值
    x = data_final[["x", "y", "accuracy", "day", "weekday", "hour"]]
    y = data_final["place_id"]
    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=6)
    # 3）特征工程：标准化
    transfer = StandardScaler()
    # x_train = transfer.fit_transform(x_train)
    transfer.fit(x_train)
    x_train = transfer.transform(x_train)
    x_test = transfer.transform(x_test)

    # 4）KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)

    # 加入网格搜索与交叉验证
    # 参数准备
    param_dict = {"n_neighbors": [3, 5, 7, 9]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=3)
    estimator.fit(x_train, y_train)
    # 5）模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)
    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器：\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果：\n", estimator.cv_results_)

    print("data_final: \n", data_final)
    print("x.head(): \n", x.head())
    print("y: \n", y)

    return None


def nb_news():
    """
    用朴素贝叶斯算法对新闻进行分类
    :return:
    """
    # 1) 获取数据
    news = fetch_20newsgroups(data_home="./", subset="all")
    # 2) 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target)
    # 3) 特征工程： 文本特征抽取-tfidf
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4) 朴素贝叶斯算法预估器流程
    estimator = MultinomialNB()
    estimator.fit(x_train, y_train)

    # 5) 模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)
    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    # # 最佳参数：best_params_
    # print("最佳参数：\n", estimator.best_params_)
    # # 最佳结果：best_score_
    # print("最佳结果：\n", estimator.best_score_)
    # # 最佳估计器：best_estimator_
    # print("最佳估计器：\n", estimator.best_estimator_)
    # # 交叉验证结果：cv_results_
    # print("交叉验证结果：\n", estimator.cv_results_)
    return None


def decision_iris():
    """
    用决策树对鸢尾花进行分类
    :return:
    """
    # 1）获取数据集
    iris = load_iris()
    # 2）划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
    # 3）决策树预估器
    estimator = DecisionTreeClassifier(criterion="entropy")
    estimator.fit(x_train, y_train)
    # 4）模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)
    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)
    # 可视化决策树
    export_graphviz(estimator, out_file="./iris_tree.dot", feature_names=iris.feature_names)
    print("done")
    return None


def decision_titanic():
    """
    titanic 案例
    :return:
    """
    # 1、获取数据
    path = "D:/pyhtonProject/Machine_Learning/resources/titanic/titanic.csv"
    data = pd.read_csv(path)
    titanic = data.copy()

    # 筛选特征值和目标值
    x = titanic[["pclass", "age", "sex", "survived"]]
    x.head()
    # 2、数据处理
    # 1）缺失值处理
    x["age"].dropna()
    xx = x[["pclass", "age", "sex"]]
    yy = x["survived"]
    xx.head()
    yy.head()
    # 2) 转换成字典
    xx = xx.to_dict(orient="records")
    # 3、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(xx, yy, random_state=22)
    # 4、字典特征抽取
    transfer = DictVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 5、决策树预估器
    estimator = DecisionTreeClassifier(criterion="entropy")
    estimator.fit(x_train, y_train)
    # 6、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)
    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)
    # 可视化决策树
    export_graphviz(estimator, out_file="./titanic_tree.dot", feature_names=transfer.get_feature_names())
    print("done")

    print(x)
    return None


def random_forest_demo():
    """
    随机森林
    :return:
    """
    # 1）获取数据
    iris = load_iris()
    # 2）划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
    # 3）特征工程：标准化
    transfer = StandardScaler()
    transfer.fit(x_train)
    x_train = transfer.transform(x_train)
    x_test = transfer.transform(x_test)

    # 4）随机森林算法预估器
    estimator = RandomForestClassifier()

    # 加入网格搜索与交叉验证
    # 参数准备
    param_dict = {"n_estimators": [120, 200, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=3)
    estimator.fit(x_train, y_train)
    # 5）模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n", y_predict)
    print("直接比对真实值和预测值:\n", y_test == y_predict)
    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器：\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果：\n", estimator.cv_results_)

    return None


if __name__ == "__main__":
    # 代码1：用KNN算法对鸢尾花进行分类
    # knn_iris()
    # 代码2：用KNN算法对鸢尾花进行分类
    # knn_iris_gscv()
    # 代码3：facebook 案例分析
    # knn_facebook_demo()
    # 代码4：用朴素贝叶斯算法对新闻进行分类
    # nb_news()
    # 代码5：用决策树对鸢尾花进行分类
    # decision_iris()
    # 代码6：titanic案例
    # decision_titanic()
    # 代码7：随机森林案例
    random_forest_demo()
