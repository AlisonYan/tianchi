#导入pandas方便数据读取和预处理。
import pandas as pd
import numpy as np
#使用imblearn.combine导入SOMTE+ENN方法对不平衡数据进行处理
from imblearn.combine import SMOTEENN

#分别对训练数据和测试数据从本地进行读取。
train=pd.read_csv('C:/Users/Administrator/Desktop/datasets/df_train.csv')
test=pd.read_csv('C:/Users/Administrator/Desktop/datasets/df_test.csv')

id_train=pd.read_csv('C:/Users/Administrator/Desktop/datasets/df_id_train.csv',names=['id','labels'])
id_test=pd.read_csv('C:/Users/Administrator/Desktop/datasets/df_id_test.csv',names=['id'])

fee_detail=pd.read_csv('C:/Users/Administrator/Desktop/datasets/fee_detail.csv')

#先分别输出训练与测试数据的基本信息。可以对数据规模、各个特征的数据类型以及是否有缺失等，有一个总体的了解。
print train.info()
print test.info()

print id_train.info()
print id_test.info()

print fee_detail.info()

#观察标记训练数据欺诈和非欺诈的比例
print id_train['labels'].value_counts()  #0    19000  , 1     1000



