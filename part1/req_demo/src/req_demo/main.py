import numpy as np
import pandas as pd

# NumPyを使ってランダムなデータを生成
np.random.seed(0)  # 再現性のため
data = np.random.randn(5, 3)  # 5行3列のランダムな数値データ

# NumPyの配列をPandasのDataFrameに変換
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# インデックスを設定
df.index = ['Row1', 'Row2', 'Row3', 'Row4', 'Row5']

# データの表示
print("データフレーム:")
print(df)

# 基本的な統計情報
print("\n基本統計:")
print(df.describe())

# 列Aの平均値
print("\n列Aの平均値:", df['A'].mean())

# 行Row2のデータ
print("\nRow2のデータ:")
print(df.loc['Row2'])

# 条件付きフィルタリング
print("\n列Bが0より大きい行:")
print(df[df['B'] > 0])