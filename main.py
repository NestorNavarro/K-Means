import pandas as pd
from random import choice
from Iris import Iris
from MessegeBox import MB
import math
import copy

error_list = list()
class K_Mean:

    def __init__(self, k_groups, iteration):
        self.k = k_groups
        self.iterator = iteration
        self.data = pd.read_csv(r"irisData.csv")
        self.irisList = list()
        self.centroidList = list()
        self.minValue = list()
        self.tempList = list()
        self.getDataSet()
        self.getRandomData()

    def getDataSet(self):
        for i in range(len(self.data)):
            iris = Iris()
            iris.sepal_length = self.data['sepal_length'][i]
            iris.sepal_with = self.data['sepal_with'][i]
            iris.petal_length = self.data['petal_length'][i]
            iris.petal_with = self.data['petal_with'][i]
            iris.target = self.data['Class'][i]
            self.irisList.append(iris)

    def getRandomData(self):
        for i in range(self.k):
            self.centroidList.append(choice(self.irisList))
            self.centroidList[i].tag = "C" + str(i + 1) + ""
        self.distanceManhattan()

    def distanceManhattan(self):
        for i in range(len(self.irisList)):
            for j in range(self.k):
                self.minValue.append([abs(self.irisList[i].sepal_length - self.centroidList[j].sepal_length) + abs(
                    self.irisList[i].sepal_with - self.centroidList[j].sepal_with) + abs(
                    self.irisList[i].petal_length - self.centroidList[j].petal_length) + abs(
                    self.irisList[i].petal_with - self.centroidList[j].petal_with), self.centroidList[j].tag])
            self.minValue.sort()
            self.irisList[i].distance = self.minValue[0][0]
            self.irisList[i].tag = self.minValue[0][1]
            self.minValue.clear()

    def calculate_mean(self):
        for i in range(self.k):
            meanSL = 0
            meanSW = 0
            meanPL = 0
            meanPW = 0
            x = 0
            for j in range(len(self.irisList)):
                if self.centroidList[i].tag == self.irisList[j].tag:
                    meanSL = meanSL + self.irisList[j].sepal_length
                    meanSW = meanSW + self.irisList[j].sepal_with
                    meanPL = meanPL + self.irisList[j].petal_length
                    meanPW = meanPW + self.irisList[j].petal_with
                    x += 1
            self.centroidList[i].sepal_length = meanSL / x
            self.centroidList[i].sepal_with = meanSW / x
            self.centroidList[i].petal_length = meanPL / x
            self.centroidList[i].petal_with = meanPW / x
        self.distanceManhattan()

    def validation(self):
        for i in range(len(self.tempList)):
            if self.tempList[i].sepal_length != self.centroidList[i].sepal_length:
                return True
            if self.tempList[i].sepal_with != self.centroidList[i].sepal_with:
                return True
            if self.tempList[i].petal_length != self.centroidList[i].petal_length:
                return True
            if self.tempList[i].petal_with != self.centroidList[i].petal_with:
                return True
        return False

    def copy_centroid(self):
        self.tempList = list()
        for i in range(self.k):
            temp = copy.copy(k.centroidList[i])
            k.tempList.append(temp)

    def calculate_error(self):
        sum_k = 0
        for i in range(self.k):
            sum_distance = 0
            for j in range(len(self.irisList)):
                if self.centroidList[i].tag == self.irisList[j].tag:
                    sum_distance = sum_distance + math.pow(self.irisList[j].distance, 2)
            sum_k = sum_k + sum_distance
        error_list.append([sum_k, self.irisList])


mb = MB()
if mb.flag:
    x = 0
    while x < int(mb.c.get()):
        k = K_Mean(int(mb.k.get()), int(mb.n.get()))
        k.copy_centroid()
        k.calculate_mean()
        i = 0
        while k.validation() | i < k.iterator:
            k.copy_centroid()
            k.calculate_mean()
            i += 1
        k.calculate_error()
        x += 1
    print("Error por corrida")
    for i in range(len(error_list)):
        print(error_list[i][0])
    error_list.sort()
    print("Mejor corrida " + str(error_list[0][0]))
    for i in range(len(k.irisList)):
        print(error_list[0][1][i].sepal_length, error_list[0][1][i].sepal_with,
              error_list[0][1][i].petal_length, error_list[0][1][i].petal_with, error_list[0][1][i].target,
              error_list[0][1][i].distance, error_list[0][1][i].tag)