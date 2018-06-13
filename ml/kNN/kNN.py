# -*- coding: utf-8 -*- #

from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0],  [0, 0.1]]) # 注意 这里声明的是numpy.array数组
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    """
    inX: type [float, float] 预测样本
    dataSet: type numpy.array[[float, float]] 样本集
    """
    dataSetSize = dataSet.shape[0] # 获取样本量
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # 生成一个跟dataSet同类型的数组，第一维度长度为dataSetSize，第二维度1，每个item为一个二维节点
    # 并计算跟dataSet的差值，即目标点与样本集中的点的距离向量 delta = (x - y)

    sqDiffMat = diffMat ** 2 # 计算 delta**2
    sqDistances = sqDiffMat.sum(axis = 1) # 将axis=1的维度，进行sum合并 sum(delta**2)
    distances = sqDistances ** 0.5 # 将 sum(delta**2)**0.5

    sortedDistIndicies = distances.argsort() # 对距离从小到大排序，返回索引值

    classCount = {} # 用来存储前k个分类对应的数据量的

    for i in range(k): # 获取前k个分类
        voteIlabel = labels[sortedDistIndicies[i]] # 跟进第k个分类的样本索引值，获取对应的分类标签
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 # 对该分类标签进行加1计数

    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True) # 对分类统计的结果进行排序

    return sortedClassCount[0][0]

"""
#run
group, labels = createDataSet()
print group, labels
print classify0([0,0], group, labels, 3)
"""
