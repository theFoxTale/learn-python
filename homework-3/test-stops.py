import csv
from datetime import datetime
from geopy.distance import geodesic

# задание №1
streets_and_busstops = {}
busstops_coordinates = []
with open('moscow-bus-stops.csv', 'r', encoding="cp1251") as bus_file:
    reader = csv.DictReader(bus_file, delimiter=";")
    for row in reader:
        # исключение заглушки
        if row['Street'] == 'проезд без названия':
            continue

        # для рассчёта расстояний в задании №3
        try:
            busstops_coordinates.append({
                "street"    : row['Street'],
                "longitude" : float(row["Longitude_WGS84"]),
                "latitude"  : float(row["Latitude_WGS84"])
            })
        except (TypeError, ValueError):
            pass

        #перебор и подсчёт
        if row['Street'] in streets_and_busstops:
            streets_and_busstops[row['Street']] += 1
        else:
            streets_and_busstops[row['Street']] = 1

#сортировка
sorted_streets_and_busstops = sorted(
    streets_and_busstops.items(), 
    key=lambda item: item[1], 
    reverse=True
)
print(f"Больше всего автобусных остановок({sorted_streets_and_busstops[0][1]}) в Москве на улице {sorted_streets_and_busstops[0][0]}")


# задание №2
print("")
dt_now = datetime.now()
station_with_repairs = []

metro_coordinates = []
metro_list = []
with open('moscow-metro-stops.csv', 'r', encoding="cp1251") as metro_file:
    reader = csv.DictReader(metro_file, delimiter=";")
    for row in reader:
        # зачем-то с "ё" и с "е" две разные станции
        row['NameOfStation'] = row['NameOfStation'].replace("ё", "е")

        # для рассчёта расстояний в задании №3
        try:
            if not row['NameOfStation'] in metro_list:
                metro_list.append(row['NameOfStation'])

                metro_station = {
                    "metro"     : row['NameOfStation'],
                    "longitude" : float(row["Longitude_WGS84"]),
                    "latitude"  : float(row["Latitude_WGS84"])
                }
                metro_coordinates.append(metro_station)
        except (TypeError, ValueError):
            pass

        # для ремонта эскалаторов
        if not row["RepairOfEscalators"]:
            continue

        # последний период ремонта из списка
        last_repair_period = row["RepairOfEscalators"].split(";")[-1]
        
        # дата окончания в ремонте
        end_date = datetime.strptime(last_repair_period.split("-")[-1], "%d.%m.%Y")
       
        # учитываем только то, что ремонтируется сейчас
        # (дата окончания ремонта больше текущей)
        if end_date > dt_now and not row["NameOfStation"] in station_with_repairs:
            station_with_repairs.append(row["NameOfStation"])

if len(station_with_repairs) == 0:
    print("Станции метро, на которых сейчас ремонтируются эскалаторы, не найдены.")
else:
    print(f"Список станций метро, на которых сейчас ведётся ремонт эскалатора: {', '.join(station_with_repairs)}.")

# задание №3
print("")
print("Подождите, я считаю...")
busstops_near_metro = {}
for busstop in busstops_coordinates:
    point_bus = (busstop["latitude"], busstop["longitude"])
    for metro in metro_coordinates:
        point_metro = (metro["latitude"], metro["longitude"])
        distance = geodesic(point_bus, point_metro).km
        if (distance <= 0.5):
            if metro['metro'] in busstops_near_metro:
                busstops_near_metro[metro['metro']] += 1
            else:
                busstops_near_metro[metro['metro']] = 1

#сортировка
sorted_busstops_near_metro = sorted(
    busstops_near_metro.items(), 
    key=lambda item: item[1], 
    reverse=True
)
print(f"Больше всего автобусных остановок({sorted_busstops_near_metro[0][1]}) в Москве у метро {sorted_busstops_near_metro[0][0]}")

