import pandas as pd
import time

def delete(ProvinceName):
    # 读取csv文件
    day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    df = pd.read_csv('TikTokData_'+day+'_'+ProvinceName+'_.csv')

    # 删除第六列字符串前面的'https:'
    df.iloc[0:, 5] = df.iloc[0:, 5].str.replace('https:', '')

    # 保存修改后的csv文件
    df.to_csv('TikTokData_'+day+'_'+ProvinceName+'_.csv', index=False)
