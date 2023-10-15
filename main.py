from pyrsistent import mutant
import function as fun
import pandas as pd
import matplotlib.pyplot as plt

#从excel中读取数据
df = pd.read_excel('F:/github/python/机器人队视觉组/github/ROBOCON2024-TASK/新建 Microsoft Excel 工作表.xlsx') #excel位置
lst = df.values.tolist()
print(lst)
data = [x for sub_lst in lst for x in sub_lst]  #将excel第一列的数据读取为一个列表
print(" 数据如下： ") 
print(data)

#计算测量的平均值
#real_num=int(input("请输入真值： "))
real_num=fun.averge(data)      #可以选两种 1.以测量平均值作为真值  2.以测量值为真值
data_averge_orgin=real_num
data=fun.residual(data,real_num)

#剔除粗大误差
data1=fun.sigma(data)
data=fun.delete_num(data,data1)  # 不含粗大误差的数据
real_num=fun.averge(data)
data1=fun.sigma(data)
data=fun.delete_num(data,data1)
   
#判断系统误差
#画出数据图
squares = data
plt.plot(squares)
plt.show()  #可以通过观察判断是否存在系统误差

#求算术平均值得标准差
num1=str(fun.sigma(data)/len(data))
print("\n算术平均值的标准差: "+
      "\n\t"+
      num1)

#算术平均值的极限误差
v=len(data)-1
t=fun.t_value(v)
t=round(t,4)
num=t*float(num1)

#合成误差后的计算值

result=real_num+num+data_averge_orgin
print("\n最终的结果为："+str(result))