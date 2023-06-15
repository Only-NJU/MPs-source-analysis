import pandas as pd
import numpy as np


#µº»Îexcel
file_name = 'test-cor1.xlsx'
df = pd.read_excel(file_name, sheet_name='page_1', header=0, index_col = 0)

for index, row in df.iterrows():
    ls= row.to_list()
    idx = ls.index(max(ls))   
    # min(ls)
    print (idx)


