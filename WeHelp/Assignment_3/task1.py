import urllib.request as req
import json
import csv
import re

url_1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url_2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}


# 捷運站對應區域
mrt_to_district = {}

# 捷運站對應景點
mrt_to_spot = {}


# 第二個網頁
request_2 = req.Request(url_2, headers=headers)
with req.urlopen(request_2) as response:
    data_2 = response.read().decode("utf-8-sig")
    json_data_2 = json.loads(data_2)


results_2 = json_data_2["data"]


for M in results_2:
    MRT_station = M["MRT"]
    area = M["address"]
    # 每個站有序列號
    SERIAL_NO = M["SERIAL_NO"]
    # 透過正規表達式，取出區域
    match = re.search(r"\s(\w+區)", area)
    if match:
        district = match.group(1)
        mrt_to_district[SERIAL_NO] = (MRT_station, district)
        mrt_to_spot[MRT_station] = []


# 第一個網頁
request = req.Request(url_1, headers=headers)
with req.urlopen(request) as response:
    data = response.read().decode("utf-8-sig")
    json_data = json.loads(data)


results = json_data['data']['results']

# 將資料寫入 csv 檔案
with open('spot.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    for item in results:
        SpotTitle = item['stitle']
        longitude = item['longitude']
        latitude = item['latitude']
        first_image_url = item['filelist'].split(
            'https://')[1]  # 取第一張圖片網址
        first_image_url = 'https://' + first_image_url
        # 捷運站序列號
        SERIAL_NO = item['SERIAL_NO']

        # 透過序列號，找出捷運站進而找出區域
        if SERIAL_NO in mrt_to_district:
            MRT, district = mrt_to_district[SERIAL_NO]

            # 將景點加入捷運站對應景點
            mrt_to_spot[MRT].append(SpotTitle)
        else:
            MRT = "未知"
            district = "未知"

        writer.writerow([SpotTitle, district, longitude, latitude,
                        first_image_url])


# 寫入捷運站與景點對應到 mrt.csv
with open('mrt.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    for MRT, spots in mrt_to_spot.items():
        writer.writerow([MRT, ", ".join(spots)])
