# -*- coding:utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import ticker

def climate_plot():
    # 1.查看数据文件结构

    # 传入世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx",sheetname='Data')
    
    # 2.读取数据并对缺失值处理
    df_co2 = df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT']
    df_met = df_climate[df_climate['Series code']=='EN.ATM.METH.KT.CE']
    df_nox = df_climate[df_climate['Series code']=='EN.ATM.NOXE.KT.CE']
    df_ghgo = df_climate[df_climate['Series code']=='EN.ATM.GHGO.KT.CE']
    df_ghgr = df_climate[df_climate['Series code']=='EN.CLC.GHGR.MT.CE']
    # 组合读取到的数据
    df_ghg_concat = pd.concat([df_co2,df_met,df_nox,df_ghgo,df_ghgr],axis=0)
    df_ghg_drop = df_ghg_concat.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1).set_index('Country code').replace({'..':pd.np.NaN})
    # 填充
    df_ghg_fill = df_ghg_drop.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).dropna(how='all')
    
    # 求和
    df_ghg_fill.loc['total'] = df_ghg_fill.apply(lambda x:x.sum(),axis=0)
    # 矩阵转置
    df_ghg_zz = df_ghg_fill.loc['total'].T

    
    # 直接读取 NASA 全球温度变化数据集
    df_temper = pd.read_excel('GlobalTemperature.xlsx')
    df_temper['Date'] = pd.to_datetime(df_temper['Date'])
    df_temper_date = df_temper.set_index('Date')
    # 选取1990-2011年间的温度变化数据
    df_temper_r = df_temper_date[['Land Average Temperature','Land And Ocean Average Temperature']]
    # 按照 A－年，Q－季度 重采样
    df_temper_ra = df_temper_r.resample('A').mean()
    df_temper_rq = df_temper_r.resample('Q').mean()
    
    # 选取1990～2010年的数据
    df_temper_ra_slice = df_temper_ra['1990-1-1':'2010-12-31']
    
    # 合并从两个数据集读取到的数据
    df_merge_temp = pd.concat([df_temper_ra_slice.reset_index(),df_ghg_zz.loc['1990':'2010'].reset_index()],axis=1)
    df_merge = df_merge_temp.drop(['Date'],axis=1).set_index('index')
    
    # 数据归一化
    df_nor = (df_merge-df_merge.min())/(df_merge.max()-df_merge.min())
    print(df_nor)
    

    # 绘图4*4
    fig,axes = plt.subplots(nrows=2,ncols=2)
    
    # 子图1
    ax1 = df_nor.plot(
            kind='line',
            figsize=(16,9),
            ax=axes[0,0],
            )
    
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Values')
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
    # 子图2
    ax2 = df_nor.plot(
            kind='bar',
            figsize=(16,9),
            ax=axes[0,1],
            )
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Values')
    # 子图3
    ax3 = df_temper_rq.plot(
            kind='area',
            figsize=(16,9),
            ax=axes[1,0],
            )
    ax3.set_xlabel('Quarters')
    ax3.set_ylabel('Temperature')
    # 子图4
    ax4 = df_temper_rq.plot(
            kind='kde',
            figsize=(16,9),
            ax=axes[1,1],
            )
    ax4.set_xlabel('Values')
    ax4.set_ylabel('Values')

    plt.show()

    # 3.对时间序列数据集进行处理并重新采样
    
    # 4.按规定选择数据
    # 5.按规定绘图

    # 务必在绘图前设置子图对象，并返回
    #fig = plt.subplot()

    # 返回 fig 对象
    return fig

if __name__=='__main__':
    climate_plot()

