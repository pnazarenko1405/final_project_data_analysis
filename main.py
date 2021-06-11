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

files = ['2019-20-fullyr-data_sa_crime.csv', '2018-19-data_sa_crime.csv'] # выполняем весь этот код по созданию карты с маркерами для каждого файла
for file in files:

    locations = []

    entrypoint1 = "https://nominatim.openstreetmap.org/search"
    query1 = {'q': 'MORPHETT VALE australia', 'format': 'xml'}
    r1 = requests.get(entrypoint1, params=query1)
    soup = BeautifulSoup(r1.text, 'xml')

    with open(osp.join(os.environ['HOME'],'папка с файлами',file), newline='') as f:   # если будут ошибки из-за пути, то просто вставь полный путь к папке с файлами csv
        reader = csv.reader(f)
        for row in reader:
            place = row[1]+' '+row[2] #берем название города и почтовый индекс
            locations.append(place)

    locations.pop(0) # удаляем перую строку (название столбцов)
    new_dict = {i:locations.count(i) for i in tqdm(locations)} # собираем словарь {локация : кол-во нарушений}

    sorted_values = sorted(new_dict.values(), reverse=True) # сортируем от большего к меньшему значения словаря
    sorted_dict = {}

    for i in sorted_values: # собираем новый словарь с сортировкой по значению
        for k in new_dict.keys():
            if new_dict[k] == i:
                sorted_dict[k] = new_dict[k]
                break

    # делаем срез словаря через списки
    lst_slice_key = list(sorted_dict.keys())[:27] #берем первые 27 записей (ключи)
    lst_slice_val = list(sorted_dict.values())[:27] #берем первые 27 записей (значения)

    new_sorted_dict = dict(zip(lst_slice_key, lst_slice_val)) # собираем новый словрь-срез
    print(new_sorted_dict)

    lat_19_20=[]
    lon_19_20=[]
    lst_number = []
    lst_place = []

    # делаем запрос и заполняем словари нужными данными
    for name, number in tqdm(new_sorted_dict.items()):
        entrypoint2 = "https://nominatim.openstreetmap.org/search"
        query2 = {'q': str(name), 'format': 'xml'}
        r2 = requests.get(entrypoint2, params=query2)
        soup1 = BeautifulSoup(r2.text, 'xml')
        for place1 in soup1.find_all("place"):
            lst_place.append(place1['display_name'])
            lat_19_20.append(float(place1['lat']))
            lon_19_20.append(float(place1['lon']))
            lst_number.append(number)
            break

    coord_19_20=dict(zip(lat_19_20, lon_19_20))
    a = list(coord_19_20.keys())[0]
    b = coord_19_20[a] 

    def color_change(count): # менеяем цвет в зависимости от кол-ва преступлений в точке
        if(count < 800):
            return('green')
        elif(800 <= count <1100):
            return('orange')
        else:
            return('red')

    def radius_change(count): # менеяем радиус в зависимости от кол-ва преступлений в точке
        if(count < 800):
            rad = 7
            return rad
        elif(800 <= count <1100):
            rad = 14
            return rad
        else:
            rad = 21
            return rad

    map = folium.Map(location=[a,b], zoom_start = 8) # создаем карту с дефолтной локацией
    marker_cluster = folium.plugins.MarkerCluster().add_to(map) # создаем кластеризацию маркеров на карте

    for lat, lon, place, number in tqdm(zip(lat_19_20, lon_19_20, lst_place, lst_number)): # создаем маркеры на карте one by one
        place_splited = place.split(',')
        folium.CircleMarker(location=[lat,lon], radius=radius_change(int(number)), # location - координаты маркера, radius - берем из функции radius_change
        popup = f'Place: {place_splited[0]}, {place_splited[1]}, {place_splited[2]}\nCrimes: {str(number)}',  # popup - текст маркера
        fill_color=color_change(int(number)),  color="black", fill_opacity = 0.9).add_to(marker_cluster) # fill_color - берем из функции color_change

    map.save(f"map_{file[:-4]}.html") # сохраняем карту в html формате
    print(f'DONE with {file}')
    url = f"map_{file[:-4]}.html"
    webbrowser.open(url, new=2)  # запускаем карту в браузере (внимание - запускается не сервер какой-нибудь или сайт, а просто открывается файл. 
                                                                                        # браузер выступаем в роли проги, которая читает html)