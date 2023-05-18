import numpy as np
import pandas as pd

if __name__ == '__main__':
    pro=[[1000,25],[280,120],[900,30]]
    df=pd.DataFrame(pro,index=["store1","store2","store3"],columns=["unit price","number"])

    print(df)

    df["total_price"]=df["unit price"]+df["number"]

    print()
    print(df)

    print()

    df_sort=df.sort_values(by="total_price",ascending=[False])
    print(df_sort.head(2))
