import numpy as np
import matplotlib.pyplot as plt
import random

#读取文件
with open('idkp1-10.txt') as f:
    allstr = f.readlines()
#print(allstr)


def func(s):
    '''读取组内数据'''
    for i in range(len(allstr)):
        if s in allstr[i]:
            v1,v2 = allstr[i+1].split(',')
            n=v1.split('=')[-1]
            n=eval(n)
            c=v2.split()[-1][:-1]

            p = allstr[i+3].split(',')
            v=p[:-1]

            w = allstr[i+5].split(',')
            w=w[:-1]

            return n,c,v,w


def draw_scatter(n,v,w):
    '''绘制重量——价值的散点图'''
    x=[]
    y=[]
    W=[]
    V=[]
    for i in range(n):
        x=int(w[i])
        W.append(x)
        y=int(v[i])
        v.append(y)
        plt.scatter(x,y)            #绘制散点图
    plt.title("W-V scatter plot")   #设置标题
    plt.xlabel("W")                 #设置x轴标签为重量W
    plt.ylabel("V")                 #设置y轴标签为价值V
    plt.show()                      #显示图像


def datasorted(w,v):
    '''对价值与重量的比值进行非递增排序'''
    v_w=[]          #创建一个空列表，存储价值与重量的比值
    v1=v[2::3]      #价值列表里的第三项
    w1=w[2::3]      #重量列表里的第三项
    for i in range(len(v1)):
        s=int(v[i])/int(w[i])   #价值/重量
        v_w.append(s)           #将价值/重量的比值存入列表v_w
    v_w.sort(reverse=True)      #降序排序
    print(v_w)

def pack(n, c, w, v):

    # 初始化dp数组
    dp = [[0 for i in range(c + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):           #遍历所有的数组（第几组）
        for j in range(1, c + 1):       #遍历体积阈值，正向遍历（当前背包容量）
            dp[i][j] = max(dp[i-1][j],dp[i][j])       #在第i组，一件都不要，背包容量不减少还是原先的体积，它的最优解是前一组i-1组的最优解
            if j >= w[i-1] and dp[i][j] < dp[i-1][j-w[i-1]] + v[i-1]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-w[i-1]] + v[i-1])

    return




if __name__=='__main__':

    print("请输入你需要哪一组数据的文件：")
    file=input()
    n,c,v,w=func(file)      #调读取组内数据
    print("数组大小n:{0},\n背包最大容量c:{1},\n价值v:{2},\n重量w:{3}".format(n,c,v,w))

    pack(n, c, w, v)
    #draw_scatter(n,v,w)        #绘制重量——价值散点图
    #datasorted(w,v)         #价值/重量比值进行非递增排序
