import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform


file_name = "C:/Users/99942/Desktop/meta 0628.xlsx"

df = pd.read_excel(file_name, sheet_name='Sheet6', header=0, index_col = 0)
# df=df-df.mean()

# ≈∑ œæ‡¿Î
ou = pdist(df, 'euclidean')
ou1 = squareform(ou)
# print(ou1)
print('\n')


# œ‡πÿæ‡¿Î
cor = pdist(df, 'correlation')
cor1 = squareform(cor)
# print(cor1)
print('\n')

# º–Ω«”‡œ“
cos = pdist(df, 'cosine')
cos1 = squareform(cos)
# print(cos1)

print('\n')

# ndarray  ‰≥ˆµΩexcel
data_df = pd.DataFrame(cos1)
writer = pd.ExcelWriter('test.xlsx')
data_df.to_excel(writer, 'page_1',float_format='%.5f')
writer.save()
