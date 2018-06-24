# -*- coding: utf-8 -*-

from math import log

def createDataSet():
    dataSet = [[1, 1, 'yes'], # 构建特征值
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no'],
            ]
    labels = ['no surfacing', 'flippers'] # 特征属性描述
    return dataSet, labels


def calcShannonEnt(dataSet):
    """
    function: 计算样本集的香农熵

    dataSet: type List[List[]]
    return : type float
    """

    numEntries = len(dataSet) # 计算总样本量，用于计算各类型样本出现概率的分母
    labelCounts = {} # 用于存储每种类型的样本量

    for featVec in dataSet:
        currentLabel = featVec[-1] # 获取样本的分类
        if currentLabel not in labelCounts.keys(): # 发现新类类型
            labelCounts[currentLabel] = 0 # 初始化新类型的样本量
        labelCounts[currentLabel] += 1 # 对该种类型的样本量加一

    shannonEnt = 0.0 # 初始化信息熵
    for key in labelCounts:
        probabillity = float(labelCounts[key]) / numEntries # 计算每个分类出现的概率
        shannonEnt -= probabillity * log(probabillity, 2) # 累计香农信息熵

    return shannonEnt


def splitDataSet(dataSet, axis, value):
    """
    function: 根据某个特征的某个值，分离出一个该特征值下面的子样本集，同时从样本集去除特征（方便外部迭代）
    dataSet: type List[List[]]
    axis: type int
    value: type int/string
    return: type List[List[]]
    """
    retDataSet = [] # 返回满足给定特征的样本
    for featVect in dataSet: # 遍历每个样本
        if featVect[axis] == value: # 判断样本的目标特征是否符合目标值
            reduceFeatVec = featVect[:axis]
            reduceFeatVec.extend(featVect[axis + 1:])
            retDataSet.append(reduceFeatVec) # 将该样本单独分离出来，剔除该属性值
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    """
    function:计算一个样本集中的最大信息增益的特征
    dataSet: type List[List[]]
    return: type int
    """
    numFeatures = len(dataSet[0]) - 1 # 计算总特征数量（-1是因为有一个item存储的是分类，不是特征）
    baseEntropy = calcShannonEnt(dataSet) # 计算整体样本的信息熵
    bestInfoGain = 0.0 # 初始化信息增益
    bestFeature = -1 # 初始化最优特征
    for i in range(numFeatures): # 对于每种特征
        featList = [example[i] for example in dataSet] # 抽取该特征的所有标称量
        uniqueVals = set(featList) # 对所有标称量进行去重，获得标称量的枚举
        newEntropy = 0.0 # 初始化划分样本后的信息熵
        for value in uniqueVals: # 对于该特征的每个标称值
            subDataSet = splitDataSet(dataSet, i, value) # 对第i个特征，标称值为value的样本，抽离出一个子样本集
            prob = len(subDataSet) / float(len(dataSet)) # 计算该样本集在整体样本中的出现概率
            newEntropy += prob * calcShannonEnt(subDataSet) # 累计该特征划分后的信息熵
        infoGain = baseEntropy - newEntropy # 计算该划分下的信息增益
        if (infoGain > bestInfoGain) : # 留下最大的信息增益特征
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    """
    input : array [] 剩余分类的列表
    """
    classCount = {} # 用于存储分类的个数
    for vote in classList:
        if vote not in classCount.keys(): # 如果没有过该分类
            classCount[vote] = 0 # 为此分类初始化为0
        classCount[vote] += 1 # 否则对此分类增加1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True) # 根据分类对应次数从大到小排序
    return sortedClassCount[0][0] # 返回最多的分类

def createTree(dataSet, labels):
    """
    function:跟进最优特征划分，将样本集划分成决策树
    dataSet: type List[List[]]
    labels: type List[string]
    """
    classList = [example[-1] for example in dataSet] # 提取所有的分类

    # 结束条件判断
    if classList.count(classList[0]) == len(classList): # 结束条件1：如果只有一种分类，即随机取一个分类，分类的数量刚好等于总数量
        return classList[0] # 返回该特征作为叶子
    if len(dataSet[0]) == 1: # 结束条件2：如果只剩下分类了，即所有特征都分离完了
        return majorityCnt(classList) # 选择一种出现最多次数的分类，作为叶子（不过这样应该会有一定的错误率）

    # 最优特征选取
    bestFeat = chooseBestFeatureToSplit(dataSet) # 选出最优特征
    bestFeatLabel = labels[bestFeat]

    # 构建结果
    myTree = {bestFeatLabel:{}} # 初始化决策树
    del(labels[bestFeat]) # 删除已选出的标签

    featValues = [example[bestFeat] for example in dataSet] # 选出最有特征在样本集中的特征值
    uniqueVals = set(featValues) # 去重，得到最优特征的特征值集合

    # 迭代构建
    for value in uniqueVals:
        subLabels = labels[:]  # 由于python的引用传参，会导致该变量在递归中被修改，因此复制一个副本进行传递
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels) # 对最有特征的每个值进行样本抽离，迭代计算决策树

    return myTree

"""
# run
data, labels = createDataSet()
tree = createTree(data, labels)
print tree
"""
