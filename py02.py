import numpy as np
import matplotlib.pyplot as plt
import random
import time
with open('idkp1-10.txt') as f:
    allstr = f.readlines()

#读取组内数据
def func(s):
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

#绘制重量——价值的散点图
def draw_scatter(n,v,w):
    x=[]
    y=[]
    W=[]
    V=[]
    for i in range(n):
        x=int(w[i])
        W.append(x)
        y=int(v[i])
        v.append(y)
        plt.scatter(x,y)
    plt.title("W-V scatter plot")
    plt.xlabel("W")
    plt.ylabel("V")
    plt.show()

#对价值与重量的比值进行非递增排序
def datasorted(w,v):
    v_w=[]
    v1=v[2::3]
    w1=w[2::3]
    for i in range(len(v1)):
        s=int(v[i])/int(w[i])
        v_w.append(s)
    v_w.sort(reverse=True)
    print(v_w)
def pack(w,v,C):
    begin=time.time()

    n_list = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

    dp = [0 for _ in range(C + 1)]
    for i in range(1, len(w) + 1):  # 物品循环
        for j in reversed(range(1, C + 1)):  # 剩余体积循环
            for k in range(n_list[i-1]):  # 别的和0，1背包一样 就是这里枚举一下每个组内的值，在每个组内选出一个max值
                if j-w[i-1][k] >= 0:
                    dp[j] = max(dp[j], dp[j- w[i-1][k]] + v[i-1][k])
    print("最大价值：",dp[C])
    end=time.time()
    print("运行时间为：",end-begin)

#n,c,v,w=func('IDKP0')

if __name__=='__main__':
    print("请输入你需要哪一组数据的文件：")
    file=input()
    n,c,v,w=func(file)
    print(n,c,v,w)
    draw_scatter(n,v,w)
    datasorted(w,v)

    v1=[int(x)for x in v]
    w1=[int(y)for y in w]
    v2=[v1[i:i+3] for i in range(0, len(v1),3)]   #3个3个分为一组
    w2=[w1[i:i+3] for i in range(0, len(w1),3)]   #3个3个分为一组
    n1=len(v2)
    #print(n1)
    #print(v2,w2)
    #print(v1[1][1],type(v1[1][1]))
    C=int(c)
    pack(w2,v2,C)



