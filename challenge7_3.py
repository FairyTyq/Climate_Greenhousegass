# -*- coding:utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt

def climate_plot():
    # 直接读取 NASA 全球温度变化数据集
    df_temperature = pd.read_excel('GlobalTemperature.xlsx')

    # 传入世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx",sheetname='Data')
    
    df_co2 = df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT']
    df_met = df_climate[df_climate['Series code']=='EN.ATM.METH.KT.CE']
    df_nox = df_climate[df_climate['Series code']=='EN.ATM.NOXE.KT.CE']
    df_ghgo = df_climate[df_climate['Series code']=='EN.ATM.GHGO.KT.CE']
    df_ghgr = df_climate[df_climate['Series code']=='EN.CLC.GHGR.MT.CE']
    
    #df_concat = pd.concat([df_co2,df_met,df_nox,df_ghgo,df_ghgr],axis=0)
    
    #print(df_concat)
    df_dic = {'df_dic':df_co2,'df_met':df_met,'df_nox':df_nox,'df_ghgo':df_ghgo,'df_ghgr':df_ghgr}
    # 归一化后的数据存入该字典
    df_handled_list = {}
    
    for df_k,df_v in df_dic.items():
        # 去掉不相关数据列
        df_v_drop = df_v.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1).set_index('Country code').replace({'..':pd.np.NaN})
        # 数据填充
        df_v_fill = df_v_drop.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).dropna(how='all')

        #数据归一化
        df_v_nor = df_v_fill.apply(lambda x:round((x-x.min())/(x.max()-x.min()),3))
        #print(df_v_nor.head())

        # 存入字典
        df_handled_list[df_k] = df_v_nor
    
    print(df_handled_list)
    
    # 1.查看数据文件结构
    # 2.读取数据并对缺失值处理
    # 3.对时间序列数据集进行处理并重新采样
    #print(df_temperature.head(20))
    #df_temperature['Date'] = pd.to_datetime(df_temperature['Date'])
    #df_temperature
    # 4.按规定选择数据
    # 5.按规定绘图

    # 务必在绘图前设置子图对象，并返回
    #fig = plt.subplot()

    # 返回 fig 对象
    #return fig

if __name__=='__main__':
    climate_plot()

