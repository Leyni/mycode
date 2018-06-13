# -*- coding: utf-8 -*- #

from numpy import *
import operator

def loadSimpData():
    datMat = matrix([
        [1., 2.1],
        [2., 1.1],
        [1.3, 1.],
        [1., 1.],
        [2., 1.]
        ])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLabels

def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    """
    function: 指定一种分类器条件（某特征、某阈值、某种大小关系下），对样本进行分类
        dataMatrix : input 样本集
        dimen : input 分类维度
        threshVal : input 分类阈值
        threshIneq : input 分类不等式条件

        return : 分类结果的矩阵 m*1
    """

    retArray = ones((shape(dataMatrix)[0], 1)) # 构建一个m*1的全1矩阵
    if threshIneq == 'lt': # 判断不等式条件
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0 # 对小于阈值的样本标记为-1
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0 # 对大于阈值的样本标记为-1
    return retArray

def buildStump(dataArr, classLabels, D):
    """
    function: 构建错误率最小的单层决策树
    dataArr: 样本集，数组
    classLabels: 样本标注
    D: 样本错误率权重 1*m
    """
    dataMatrix = mat(dataArr) # 样本矩阵化m*n
    labelMat = mat(classLabels).T # 标记矩阵化m*1

    m, n = shape(dataMatrix) # 获取样本量和特征量
    numSteps = 10.0 # 阈值的划分数量
    bestStump = {} # 记录最佳单层决策树
    bestClasEst = mat(zeros((m,1))) #
    minError = inf # 最小错误率

    for i in range(n): # 对于每个特征进行尝试
        rangeMin = dataMatrix[:, i].min() # 获取该特征的最小值
        rangeMax = dataMatrix[:, i].max() # 获取该特征的最大值
        stepSize = (rangeMax - rangeMin) / numSteps # 计算该特征的步长
        for j in range(-1, int(numSteps) + 1): # 对于每个阈值进行尝试
            for inequal in ['lt', 'gt']: # 对于每种不等式条件，即划分方式
                threshVal = (rangeMin + float(j) * stepSize) # 计算阈值
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal) # 分类结果
                errArr = mat(ones((m, 1))) # 记录错误分类结果的矩阵 m*1
                errArr[predictedVals == labelMat] = 0 # 根据尝试的分类结果标记错误结果
                weightedError = D.T * errArr / m # 计算加权错误率 (m*1).T * (m*1)
                print "split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % \
                        (i, threshVal, inequal, weightedError)

                if weightedError < minError : # 如果该尝试的错误率更小
                    minError = weightedError # 记录当前尝试的错误率
                    bestClasEst = predictedVals.copy()  # 记录当前的分类结果
                    bestStump['dim'] = i # 记录当前划分的特征
                    bestStump['thresh'] = threshVal # 记录阈值
                    bestStump['ineq'] = inequal # 记录划分条件

    return bestStump, minError, bestClasEst

def adaBoostTrainDS(dataArr, classsLabels, numIt = 40):
    """
    function : adaBoost训练
    dataArr: input 样本集
    classLabels: input 样本标注
    numIt: input 迭代次数
    """
    weakClassArr = [] # 用于存储弱分类器结果
    m = shape(dataArr)[0] # 样本数量
    D = mat(ones((m, 1)) / m) # 初始化样本的错误率权重 m*1
    aggClassEst = mat(zeros((m, 1))) # 用于记录所有分类器的累计分类值 m*1
    for i in range(numIt): # 不断迭代训练
        bestStump, error, classEst = buildStump(dataArr, classLabels, D) # 训练出一个单层决策树
        print "D:", D.T

        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16))) # 计算分类器的权重
        bestStump['alpha'] = alpha # 记录分类器的权重
        weakClassArr.append(bestStump) # 追加训练出的分类器

        expon = multiply(-1 * alpha * mat(classLabels).T, classEst) # 对应元素相乘，计算指数，由于classEst和classLabel标注的是+/-1，因此相同结果为1，不同为-1
        D = multiply(D, exp(expon)) # 迭代样本错误率权重，公式为 D * e ** -alpha，
        D = D/D.sum()
        print "classEst: ", classEst.T

        aggClassEst += alpha * classEst # 累加该分类结果*权重的值，记录的是所有分类器对目前样本预测的概率累计值
        print "aggClassEst: ", aggClassEst.T
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1))) # 对比累计预测与样本标注的一致性（是否统一符号方向）
        errorRate = aggErrors.sum() / m # 累计预测后的错误率
        print "total error: ", errorRate, "\n"

        if errorRate == 0.0 : break # 如果累计错误率为0，退出迭代

    return weakClassArr



#run
datMat, classLabels = loadSimpData()
classifierArray = adaBoostTrainDS(datMat, classLabels, 9)
print datMat, classLabels
print classifierArray
