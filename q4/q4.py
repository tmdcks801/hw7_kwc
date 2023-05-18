import numpy as np
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('gender2.csv',encoding="EUC-KR",index_col=0,header=0)
    df = df[['2022년_계_총인구수', '2022년_남_총인구수','2022년_여_총인구수']]

    df.rename(columns={'2022년_계_총인구수': 'Total','2022년_남_총인구수':'Male','2022년_여_총인구수':'Female'}, inplace=True)
    print(df)

