# -*- coding:utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt

def climate_plot():
    # 1.查看数据文件结构
    # 直接读取 NASA 全球温度变化数据集
    df_temperature = pd.read_excel('GlobalTemperature.xlsx')

    # 传入世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx",sheetname='Data')
    
    # 2.读取数据并对缺失值处理
    df_co2 = df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT']
    df_met = df_climate[df_climate['Series code']=='EN.ATM.METH.KT.CE']
    df_nox = df_climate[df_climate['Series code']=='EN.ATM.NOXE.KT.CE']
    df_ghgo = df_climate[df_climate['Series code']=='EN.ATM.GHGO.KT.CE']
    df_ghgr = df_climate[df_climate['Series code']=='EN.CLC.GHGR.MT.CE']
    
    df_ghg_concat = pd.concat([df_co2,df_met,df_nox,df_ghgo,df_ghgr],axis=0)
    df_ghg_drop = df_ghg_concat.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1).set_index('Country code').replace({'..':pd.np.NaN})
    
    df_ghg_fill = df_ghg_drop.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).dropna(how='all')

    df_ghg_fill.loc['total'] = df_ghg_fill.apply(lambda x:x.sum(),axis=0)
    # 矩阵转置
    df_ghg_zz = df_ghg_fill.loc['total'].T

    xmax = df_ghg_zz.max()
    xmin = df_ghg_zz.min()
    df_ghg_nor = df_ghg_zz.apply(lambda x:round((x-xmin)/(xmax-xmin),3))
    print(df_ghg_nor)
    #df_dic = {'df_dic':df_co2,'df_met':df_met,'df_nox':df_nox,'df_ghgo':df_ghgo,'df_ghgr':df_ghgr}
    # 归一化后的数据存入该字典
    #df_handled_list = []
    
#    for df_k,df_v in df_dic.items():
#        # 去掉不相关数据列
#        df_v_drop = df_v.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1).set_index('Country code').replace({'..':pd.np.NaN})
#        # 数据填充
#        df_v_fill = df_v_drop.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).dropna(how='all')
#
#        #数据归一化
#        df_v_nor = df_v_fill.apply(lambda x:round((x-x.min())/(x.max()-x.min()),3))
#        # 存入列表
#        df_handled_list.append(df_v_nor)
#    df_concat = pd.concat(df_handled_list,axis=0)
    #print(df_concat)
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

