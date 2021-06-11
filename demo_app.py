import sql as sql
import streamlit as st
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import json
import sys
import folium
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import webbrowser
import os.path as osp
import os
from folium.plugins import MarkerCluster
import numpy as np
from numpy import genfromtxt
import sqlite3





with st.echo(code_location='below'):

    df1 = pd.read_csv('2019-20-fullyr-data_sa_crime.csv')


    st.title("Различные данные по правонарушениям в Южной Австралии за 2018-2020гг.")
    xx = df1.copy()
    xx.drop(columns = ['Reported Date', 'Postcode - Incident', 'Offence Level 1 Description', 'Offence Level 2 Description', 'Offence Level 3 Description'])
    xx.sort_values(by='Suburb - Incident', ascending=False)
    groups = xx.groupby('Suburb - Incident', as_index=False).sum()
    group1 = groups.sort_values('Offence count', ascending=False).head(15)

    st.write('Статистика по пригородам с наибольшим количествам правонарушений за 2019-2020гг.')

    fig2, ax2 = plt.subplots(figsize=(40, 20))
    sns.barplot(data=group1, x='Suburb - Incident', y='Offence count', palette='magma')
    plt.xlabel('Suburb', size=20)
    plt.ylabel('Offence count in the suburb', size=20)
    plt.title('Total offence count of crimes in the suburbs (top 15) 2019/2020', size=36)
    st.pyplot(fig2)
    if st.button('Показать статистику по пригородам с наибольшим количествам правонарушений за 2019-2020гг. в виде таблицы'):
        st.dataframe(group1)

    xx1 = pd.read_csv('2019-20-fullyr-data_sa_crime.csv')
    xx1.drop(columns=['Reported Date', 'Postcode - Incident', 'Suburb - Incident', 'Offence Level 2 Description', 'Offence Level 3 Description'])
    xx1.sort_values(by='Offence Level 1 Description', ascending=False)
    groups1 = xx1.groupby('Offence Level 1 Description', as_index=False).sum()
    group12 = groups1.sort_values('Offence count', ascending=False)

    st.write('Статистика по количеству правонарушений по первой классификации за 2019-2020гг.')
    fig3, ax3 = plt.subplots(figsize=(40, 20))
    sns.barplot(data=group12, x='Offence Level 1 Description', y='Offence count', palette='magma')
    plt.xlabel('Type of crime (lev1)', size=20)
    plt.ylabel('Offence count', size=20)
    plt.title('Total offence count of different crimes (lev1) 2019/2020', size=36)
    st.pyplot(fig3)
    if st.button('Показать статистику по количеству правонарушений по первой классификации за 2019-2020гг. в виде таблицы'):
        st.dataframe(group12)

    xx2 = pd.read_csv('2019-20-fullyr-data_sa_crime.csv')
    xx2.drop(columns=['Reported Date', 'Postcode - Incident', 'Suburb - Incident', 'Offence Level 1 Description', 'Offence Level 3 Description'])
    xx2.sort_values(by='Offence Level 2 Description', ascending=False)
    groups1_2 = xx2.groupby('Offence Level 2 Description', as_index=False).sum()
    group123 = groups1_2.sort_values('Offence count', ascending=False)

    st.write('Статистика по количеству правонарушений по второй классификации за 2019-2020гг.')
    fig4, ax4 = plt.subplots(figsize=(40, 20))
    sns.barplot(data=group123, x='Offence Level 2 Description', y='Offence count', palette='magma')
    plt.xlabel('Type of crime (lev2)', size=20)
    plt.ylabel('Offence count', size=20)
    plt.title('Total offence count of different crimes (lev2) 2019/2020', size=36)
    st.pyplot(fig4)
    if st.button('Показать статистику по количеству правонарушений по второй классификации за 2019-2020гг. в виде таблицы'):
        st.dataframe(group123)

    xx3 = pd.read_csv('2019-20-fullyr-data_sa_crime.csv')
    xx3.drop(columns=['Reported Date', 'Postcode - Incident', 'Suburb - Incident', 'Offence Level 1 Description', 'Offence Level 2 Description'])
    xx3.sort_values(by='Offence Level 3 Description', ascending=False)
    groups1_2_3 = xx3.groupby('Offence Level 3 Description', as_index=False).sum()
    group1234 = groups1_2_3.sort_values('Offence count', ascending=False)

    st.write('Статистика по количеству правонарушений по третьей классификации за 2019-2020гг.')
    fig5, ax5 = plt.subplots(figsize=(60, 20))
    sns.barplot(data=group1234, x='Offence Level 3 Description', y='Offence count', palette='magma')
    plt.xlabel('Type of crime (lev3)', size=20)
    plt.ylabel('Offence count', size=20)
    plt.title('Total offence count of different crimes (lev3)', size=36)
    st.pyplot(fig5)
    if st.button('Показать cтатистику по количеству правонарушений по третьей классификации за 2019-2020гг. в виде таблицы'):
        st.dataframe(group1234)

    xx4 = pd.read_csv('2019-20-fullyr-data_sa_crime.csv')
    xx4.drop(columns=['Postcode - Incident', 'Suburb - Incident', 'Offence Level 1 Description', 'Offence Level 2 Description', 'Offence Level 3 Description'])
    xx4.sort_values(by='Reported Date')
    groups1_2_3_4 = xx4.groupby('Reported Date', as_index=False).sum()
    group12345 = groups1_2_3_4.sort_values('Offence count', ascending=False)

    st.write('Статистика по количеству правонарушений по датам за 2019-2020гг.')
    fig6, ax6 = plt.subplots(figsize=(60, 20))
    sns.lineplot(data=group12345, x='Reported Date', y='Offence count', color='red')
    plt.xlabel('Date', size=20)
    plt.ylabel('Offence count', size=20)
    plt.title('Total offence count by date 01.07.19-30.06.20', size=36)
    st.pyplot(fig6)
    if st.button('Показать статистику по количеству правонарушений по датам за 2019-2020гг. в виде таблицы'):
        st.dataframe(group12345)


    x_18_19=pd.read_csv ('2018-19-data_sa_crime.csv')
    x_18_19.drop(columns=['Reported Date', 'Postcode - Incident', 'Offence Level 1 Description', 'Offence Level 2 Description', 'Offence Level 3 Description'])
    x_18_19.sort_values(by='Suburb - Incident', ascending=False)

    groups_18_19 = x_18_19.groupby('Suburb - Incident', as_index=False).sum()
    group_18_19_1 = groups_18_19.sort_values('Offence count', ascending=False).head(15)

    st.write('Статистика по пригородам с наибольшим количествам правонарушений за 2018-2019гг.')
    fig7, ax7 = plt.subplots(figsize=(40, 20))
    sns.barplot(data=group_18_19_1, x='Suburb - Incident', y='Offence count', palette='magma')
    plt.xlabel('Suburb', size=20)
    plt.ylabel('Offence count in the suburb', size=20)
    plt.title('Total offence count of crimes in the suburbs (top 15) 2018/2019', size=36)
    st.pyplot(fig7)
    if st.button('Показать статистику по пригородам с наибольшим количествам правонарушений за 2018-2019гг. в виде таблицы'):
        st.dataframe(group_18_19_1)
    #
    # x_18_19_2 = pd.read_csv('2018-19-data_sa_crime.csv')
    # x_18_19_2.drop(columns=['Reported Date', 'Postcode - Incident', 'Suburb - Incident', 'Offence Level 2 Description', 'Offence Level 3 Description'])
    # x_18_19_2.sort_values(by='Offence Level 1 Description', ascending=False)
    # groups_18_19_2 = x_18_19_2.groupby('Offence Level 1 Description', as_index=False).sum()
    # group_18_19_2 = groups_18_19_2.sort_values('Offence count', ascending=False)
    #
    # st.write('Статистика по количеству правонарушений по первой классификации за 2018-2019гг.')
    # fig8, ax8 = plt.subplots(figsize=(40, 20))
    # sns.barplot(data=group_18_19_2, x='Offence Level 1 Description', y='Offence count', palette='magma')
    # plt.xlabel('Type of crime (lev1)', size=20)
    # plt.ylabel('Offence count', size=20)
    # plt.title('Total offence count of different crimes (lev1) 2018/2019', size=36)
    # st.pyplot(fig8)
    # if st.button('Показать статистику по количеству правонарушений по первой классификации за 2018-2019гг. в виде таблицы'):
    #     st.dataframe(group_18_19_2)
    #
    # x_18_19_4 = pd.read_csv('2018-19-data_sa_crime.csv')
    # x_18_19_4.drop(columns=['Reported Date', 'Postcode - Incident', 'Suburb - Incident', 'Offence Level 1 Description', 'Offence Level 3 Description'])
    # x_18_19_4.sort_values(by='Offence Level 2 Description', ascending=False)
    # groups_18_19_4 = x_18_19_4.groupby('Offence Level 2 Description', as_index=False).sum()
    # group_18_19_4 = groups_18_19_4.sort_values('Offence count', ascending=False)
    #
    # st.write('Статистика по количеству правонарушений по второй классификации за 2018-2019гг.')
    # fig10, ax10 = plt.subplots(figsize=(40, 20))
    # sns.barplot(data=group_18_19_4, x='Offence Level 2 Description', y='Offence count', palette='magma')
    # plt.xlabel('Type of crime (lev2)', size=20)
    # plt.ylabel('Offence count', size=20)
    # plt.title('Total offence count of different crimes (lev2) 2018/2019', size=36)
    # st.pyplot(fig10)
    # if st.button('Показать статистику по количеству правонврушений по второй классификации за 2018-2019гг. в виде таблицы'):
    #     st.dataframe(group_18_19_4)
    #
    # x_18_19_3 = pd.read_csv('2018-19-data_sa_crime.csv')
    # x_18_19_3.drop(columns=['Reported Date', 'Postcode - Incident', 'Suburb - Incident', 'Offence Level 1 Description', 'Offence Level 2 Description'])
    # x_18_19_3.sort_values(by='Offence Level 3 Description', ascending=False)
    # groups_18_19_3 = x_18_19_3.groupby('Offence Level 3 Description', as_index=False).sum()
    # group_18_19_3 = groups_18_19_3.sort_values('Offence count', ascending=False)
    #
    # st.write('Статистика по количеству правонарушений по третьей классификации за 2018-2019гг.')
    # fig9, ax9 = plt.subplots(figsize=(60, 20))
    # sns.barplot(data=group_18_19_3, x='Offence Level 3 Description', y='Offence count', palette='magma')
    # plt.xlabel('Type of crime (lev3)', size=20)
    # plt.ylabel('Offence count', size=20)
    # plt.title('Total offence count of different crimes (lev3) 2018/2019', size=36)
    # st.pyplot(fig9)
    # if st.button('Показать статистику по количеству правонарушений по третьей классификации за 2018-2019гг. в виде таблицы'):
    #     st.dataframe(group_18_19_3)


    din=pd.read_csv("Offenders, principal offence of public order offences.csv")
    #din_data = genfromtxt('Offenders, principal offence of public order offences.csv', delimiter=',')
    print(din)
    #din.columns=["Years", 'Offenders']
    #print(din)
    st.write('Статистика по количеству правонарушителей 2009-2019гг.')
    fig10, ax10 = plt.subplots(figsize=(40, 20))
    sns.lineplot(data=din, x="Years", y='Offenders', color='red')
    plt.xlabel('Year', size=40)
    plt.ylabel('Offenders', size=40)
    plt.title('Offenders dinamics', size=50)
    st.pyplot(fig10)

    if st.button('Показать статистику по количеству правонарушителей 2009-2019гг. в виде таблицы'):
        st.dataframe(din)

    years = np.array([2019, 2020])
    st.write("(Придётся немного подождать, программа обрабатывает примерно 95тыс. результатов для каждого года)")

    files = ['2019-20-fullyr-data_sa_crime.csv',
             '2018-19-data_sa_crime.csv']  # выполняем весь этот код по созданию карты с маркерами для каждого файла
    for file in files:


        locations = []

        entrypoint1 = "https://nominatim.openstreetmap.org/search"
        query1 = {'q': 'MORPHETT VALE australia', 'format': 'xml'}
        r1 = requests.get(entrypoint1, params=query1)
        soup = BeautifulSoup(r1.text, 'xml')


        st.write("Визуализация количества правонарушений по пригородам на карте " + str(years[0]) + "-" + str(years[1]) + "гг.")
        years = years-1
        print(years)

        #
        # with open(osp.join(os.environ['HOME'], 'Downloads/first_project 2', file), newline='') as f:  # если будут ошибки из-за пути, то просто вставь полный путь к папке с файлами csv
        #     reader = csv.reader(f)
        #     for row in reader:
        #         place = row[1] + ' ' + row[2]  # берем название города и почтовый индекс
        #         locations.append(place)
        #
        #
        # locations.pop(0)  # удаляем перую строку (название столбцов)
        # new_dict = {i: locations.count(i) for i in tqdm(locations)}  # собираем словарь {локация : кол-во нарушений}
        #
        # sorted_values = sorted(new_dict.values(), reverse=True)  # сортируем от большего к меньшему значения словаря
        # sorted_dict = {}
        #
        # for i in sorted_values:  # собираем новый словарь с сортировкой по значению
        #     for k in new_dict.keys():
        #         if new_dict[k] == i:
        #             sorted_dict[k] = new_dict[k]
        #             break
        #
        # # делаем срез словаря через списки
        # lst_slice_key = list(sorted_dict.keys())[:27]  # берем первые 27 записей (ключи)
        # lst_slice_val = list(sorted_dict.values())[:27]  # берем первые 27 записей (значения)
        #
        # new_sorted_dict = dict(zip(lst_slice_key, lst_slice_val))  # собираем новый словрь-срез
        # print(new_sorted_dict)
        #
        # lat_19_20 = []
        # lon_19_20 = []
        # lst_number = []
        # lst_place = []
        #
        # # делаем запрос и заполняем словари нужными данными
        # for name, number in tqdm(new_sorted_dict.items()):
        #     entrypoint2 = "https://nominatim.openstreetmap.org/search"
        #     query2 = {'q': str(name), 'format': 'xml'}
        #     r2 = requests.get(entrypoint2, params=query2)
        #     soup1 = BeautifulSoup(r2.text, 'xml')
        #     for place1 in soup1.find_all("place"):
        #         lst_place.append(place1['display_name'])
        #         lat_19_20.append(float(place1['lat']))
        #         lon_19_20.append(float(place1['lon']))
        #         lst_number.append(number)
        #         break
        #
        # coord_19_20 = dict(zip(lat_19_20, lon_19_20))
        # a = list(coord_19_20.keys())[0]
        # b = coord_19_20[a]
        #
        #
        # def color_change(count):  # менеяем цвет в зависимости от кол-ва преступлений в точке
        #     if (count < 800):
        #         return ('green')
        #     elif (800 <= count < 1100):
        #         return ('orange')
        #     else:
        #         return ('red')
        #
        #
        # def radius_change(count):  # менеяем радиус в зависимости от кол-ва преступлений в точке
        #     if (count < 800):
        #         rad = 7
        #         return rad
        #     elif (800 <= count < 1100):
        #         rad = 14
        #         return rad
        #     else:
        #         rad = 21
        #         return rad
        #
        #
        # map = folium.Map(location=[a, b], zoom_start=8)  # создаем карту с дефолтной локацией
        # marker_cluster = folium.plugins.MarkerCluster().add_to(map)  # создаем кластеризацию маркеров на карте
        #
        # for lat, lon, place, number in tqdm(zip(lat_19_20, lon_19_20, lst_place, lst_number)):  # создаем маркеры на карте one by one
        #     place_splited = place.split(',')
        #     folium.CircleMarker(location=[lat, lon], radius=radius_change(int(number)),
        #                         # location - координаты маркера, radius - берем из функции radius_change
        #                         popup=f'Place: {place_splited[0]}, {place_splited[1]}, {place_splited[2]}\nCrimes: {str(number)}',
        #                         # popup - текст маркера
        #                         fill_color=color_change(int(number)), color="black", fill_opacity=0.9).add_to(
        #         marker_cluster)  # fill_color - берем из функции color_change
        #
        # map.save(f"map_{file[:-4]}.html")  # сохраняем карту в html формате
        # print(f'DONE with {file}')
        # url = f"map_{file[:-4]}.html"
        #
        #
        #
        # folium_static(map)




















































