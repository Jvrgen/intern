import datetime
import pandas as pd


# 读取数据
bank_data = pd.DataFrame(pd.read_excel('../1-7.xlsx'), dtype="int")
# print(bank_data.shape)

# 构建rfm模型特征
bank_data = bank_data.groupby(by = "id")

bank_data_last_time = bank_data["date"].max()
# print(bank_data_last_time)

F = bank_data.size()
M = bank_data["money"].sum()
# print(F)
# print(M)

R = datetime.datetime.now() - pd.to_datetime(bank_data_last_time, format='%Y%m%d')
R = R.astype("str").str.split().str[0]
R = R.astype("int")
# print(L)

Data_Feature = pd.concat([R, F, M], axis = 1)
print(Data_Feature.shape)

