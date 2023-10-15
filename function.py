import scipy.stats as stats

def averge(data):
    sum=0
    for num in data:
        sum += num
    averge=sum/len(data)
    return averge

def residual(data,real_num): #data测量值 real_num真值
    '''残差（测量值-真值）'''
    data1=[]  #绝对误差
    for num in data:
        data1.append(num-real_num)
    return data1

def sigma(data):#输入残差值
    '''计算数据的sigma值 (输入残差值)'''
    sum = 0
    i=0
    for num in data:
        sum =num**2+ sum
        i += 1
    data2 = sum/(i-1)
    data2 = data2 ** 0.5
    print("sigma : " +str(data2))
    return data2 

def delete_num(data1,data2): #输入残值和sigma值
    '''剔除粗大误差 (使用3sigma原理   输入残差和sigma)'''
    deleted_num=[]
    for num in data1:
        if abs(num) > 3*data2: 
            deleted_num.append(num)
            data1.remove(num)  
            print("\n剔除的粗大误差是: \n"+
          "\t"+str(deleted_num)) 
    if len(deleted_num) > 0:
        print("\n含有的粗大误差数为： "+"\n\t"+str(len(deleted_num)))
    return data1

def t_value(v):
    '''生成一个t分布对象，参数为自由度v'''
    t_dist = stats.t(v)
    # 计算t分布的95%置信区间的上界，即t值
    t_val = t_dist.ppf(0.975)
    
    return t_val





