
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

file_name = "C:/Users/99942/Desktop/meta 0628.xlsx"
# 特征
df = pd.read_excel(file_name, sheet_name='Sheet4', header = 0)
# 标签
df2 = pd.read_excel(file_name, sheet_name='Sheet5', usecols = [24])
'''
df_s = df-df.mean()
'''
Z_normalizer1 = preprocessing.StandardScaler()
df_s = Z_normalizer1.fit_transform(df)
'''
min_max_normalizer1 = preprocessing.MinMaxScaler()
df_s = min_max_normalizer1.fit_transform(df)
'''

# 标签类型转换
array = np.array(np.ravel(df2))
df2 = array.tolist()

lda = LinearDiscriminantAnalysis(n_components=2)

# reduced_x=pca.fit_transform(df_s)
lda.fit(df_s,df2)
reduced_x = lda.transform(df_s)
# print(df_s)
print(lda.score(df_s,df2))
print(lda.explained_variance_ratio_)



red_x,red_y=[],[]
blue_x,blue_y=[],[]
cyan_x,cyan_y=[],[]
black_x,black_y=[],[]
green_x,green_y=[],[]

red_xx,red_yx=[],[]
green_xx,green_yx=[],[]
blue_xx,blue_yx=[],[]

for i in range(len(reduced_x)):
    if df2[i] == [1]:
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])

    elif df2[i]== [2]:
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_x[i][1])

    elif df2[i]== [3]:
        cyan_x.append(reduced_x[i][0])
        cyan_y.append(reduced_x[i][1])

    elif df2[i]== [4]:
        black_x.append(reduced_x[i][0])
        black_y.append(reduced_x[i][1])

    elif df2[i]== [5]:
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])

    elif df2[i]== [6]:
       red_xx.append(reduced_x[i][0])
       red_yx.append(reduced_x[i][1])
   
    elif df2[i]== [7]:
        green_xx.append(reduced_x[i][0])
        green_yx.append(reduced_x[i][1])
        
    # elif df2[i]== [8]:
      #  blue_xx.append(reduced_x[i][0])
      #  blue_yx.append(reduced_x[i][1])

plt.scatter(red_x,red_y,c='r',marker='p')
plt.scatter(blue_x,blue_y,c='dodgerblue',marker='p')

plt.scatter(cyan_x,cyan_y,c='c',marker='p')
plt.scatter(black_x,black_y,c='k',marker='p')
plt.scatter(green_x,green_y,c='limegreen',marker='p')

plt.scatter(red_xx,red_yx,c='magenta',marker='p')
plt.scatter(green_xx,green_yx,c='goldenrod',marker='p')
# plt.scatter(blue_xx,blue_yx,c='b',marker='x')

# plt.legend(['CE','OUTL'])
plt.show()



