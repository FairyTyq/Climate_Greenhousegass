# -*- coding:utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt

def climate_plot():
    # ֱ�Ӷ�ȡ NASA ȫ���¶ȱ仯���ݼ�
    df_temperature = pd.read_excel('GlobalTemperature.xlsx')

    # ����������������仯���ݼ�
    df_climate = pd.read_excel("ClimateChange.xlsx",sheetname='����')

    # 1.�鿴�����ļ��ṹ
    # 2.��ȡ���ݲ���ȱʧֵ����
    # 3.��ʱ���������ݼ����д������²���
    # 4.���涨ѡ������
    # 5.���涨��ͼ

    # ����ڻ�ͼǰ������ͼ���󣬲�����
    fig = plt.subplot()

    # ���� fig ����
    return fig



