import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#导入excel
file_name = 'C:/Users/99942/Desktop/meta 0628.xlsx'
df = pd.read_excel(file_name, sheet_name='Sheet4', header=0)

#Pearson相关性
prs = df.corr("pearson")


#绘图
# plt.figure(dpi=300)
plt.pcolor(prs, cmap = 'bwr',vmin=-1, vmax=1)

plt.yticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns, rotation=90)
plt.colorbar()
plt.show()




