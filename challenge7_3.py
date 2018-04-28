# -*- coding:utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt

def climate_plot():
    # 直接读取 NASA 全球温度变化数据集
    df_temperature = pd.read_excel('GlobalTemperature.xlsx')

    # 传入世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx",sheetname='表名')

    # 1.查看数据文件结构
    # 2.读取数据并对缺失值处理
    # 3.对时间序列数据集进行处理并重新采样
    # 4.按规定选择数据
    # 5.按规定绘图

    # 务必在绘图前设置子图对象，并返回
    fig = plt.subplot()

    # 返回 fig 对象
    return fig



