# -*- coding:utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt

def climate_plot():
    # ֱ�Ӷ�ȡ NASA ȫ���¶ȱ仯���ݼ�
    df_temperature = pd.read_excel('GlobalTemperature.xlsx')

    # ����������������仯���ݼ�
    df_climate = pd.read_excel("ClimateChange.xlsx",sheetname='����')
    
    df_co2 = df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT']
    df_met = df_climate[df_climate['Series code']=='EN.ATM.METH.KT.CE']
    df_nox = df_climate[df_climate['Series code']=='EN.ATM.NOXE.KT.CE']
    df_ghgo = df_climate[df_climate['Series code']=='EN.ATM.GHGO.KT.CE']
    df_ghgr = df_climate[df_climate['Series code']=='EN.CLC.GHGR.MT.CE']
    df_list = [df_co2,df_met,df_nox,df_ghgo,df_ghgr]

    for df in df_list:
        df_drop = df.drop([],axis=1)
    # 1.�鿴�����ļ��ṹ
    # 2.��ȡ���ݲ���ȱʧֵ����
    # 3.��ʱ���������ݼ����д������²���
    # 4.���涨ѡ������
    # 5.���涨��ͼ

    # ����ڻ�ͼǰ������ͼ���󣬲�����
    fig = plt.subplot()

    # ���� fig ����
    return fig



