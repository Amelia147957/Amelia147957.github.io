print("------Task1------")


def find_and_print(messages, current_station):
    # 建立站名
    station_dict = {"Songshan": 1,
                    "Nanjing Sanmin": 2,
                    "Taipei Arena": 3,
                    "Nanjing Fuxing": 4,
                    "Songjiang Nanjing": 5,
                    "Zhongshan": 6,
                    "Beimen": 7,
                    "Ximen": 8,
                    "Xiaonanmen": 9,
                    "Chiang Kai-Shek Memorial Hall": 10,
                    "Guting": 11,
                    "Taipower Building": 12,
                    "Gongguan": 13,
                    "Wanlong": 14,
                    "Jingmei": 15,
                    "Dapinglin": 16,
                    "Qizhang": 17,
                    "Xiaobitan": 17.5,
                    "Xindian City Hall": 18,
                    "Xindian": 19
                    }

    # 接下來要開始計算距離
    current_station_dis = station_dict[current_station]
    closest_friend = None
    closest_distance = 1000

    for friend, message in messages.items():
        friend_station_name = None
        # 找到匹配的站名
        for station_name in station_dict.keys():
            if station_name in message:
                friend_station_name = station_name
                break

        if friend_station_name:
            # 要額外計算分支的小碧潭站(要到七張站再轉乘到小碧潭站)
            if friend_station_name == "Xiaobitan" or current_station == "Xiaobitan":
                extra_distance = 0.5
                if friend_station_name == "Xiaobitan":
                    distance = abs(
                        station_dict["Qizhang"] - current_station_dis) + extra_distance
                else:
                    distance = abs(
                        station_dict[friend_station_name] - station_dict["Qizhang"]) + extra_distance
            # 一般的狀況
            else:
                friend_station_number = station_dict[friend_station_name]
                distance = abs(friend_station_number - current_station_dis)

            if distance < closest_distance:
                closest_distance = distance
                closest_friend = friend

    print(closest_friend)


# 相關好友訊息
messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
}


find_and_print(messages, "Wanlong")  # print Mary
find_and_print(messages, "Songshan")  # print Copper
find_and_print(messages, "Qizhang")  # print Leslie
find_and_print(messages, "Ximen")  # print Bob
find_and_print(messages, "Xindian City Hall")  # print Vivian


print("------Task2------")


def book(consultants, hour, duration, criteria):  # 顧問, 預約時間, 持續時間, 條件
    # 先建立時間表
    if "schedules" not in globals():
        globals()["schedules"] = {}

    # 給每個顧問建立時間表
    for consultant in consultants:
        if consultant['name'] not in globals()["schedules"]:
            globals()["schedules"][consultant['name']] = []

    # 先篩選出符合時間的顧問
    available_consultants = []
    for consultant in consultants:
        available = True
        for checking_hour in range(hour, hour + duration):
            if checking_hour in globals()["schedules"][consultant['name']]:
                available = False
                break
        if available:
            available_consultants.append(consultant)

    # 如果沒有符合時間的顧問
    if not available_consultants:
        print("No Service")
        return

    # 條件排序
    chose_consultant = None
    for consultant in available_consultants:
        if chose_consultant is None:
            chose_consultant = consultant

        else:
            # 如果條件是價格
            if criteria == "price":
                if consultant["price"] < chose_consultant["price"]:
                    chose_consultant = consultant
            # 如果條件是評分
            elif criteria == "rate":
                if consultant["rate"] > chose_consultant["rate"]:
                    chose_consultant = consultant

    # 預約時間
    for booking_hour in range(hour, hour + duration):
        globals()["schedules"][chose_consultant['name']].append(booking_hour)

    print(chose_consultant['name'])


consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}
]


book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John


print("------Task3------")


def func(*data):
    name_dict = {}
    for name in data:
        if len(name) == 2:  # 名字只有二個字
            mid_name = name[1]  # 取得第二個字
        elif len(name) == 3:  # 名字只有三個字
            mid_name = name[1]  # 取得第二個字
        elif len(name) == 4:  # 名字只有四個字
            mid_name = name[2]  # 取第三個字
        elif len(name) == 5:  # 名字只有五個字
            mid_name = name[2]  # 取第三個字
        else:
            continue

    # 將中間字加入字典
        if mid_name not in name_dict:
            name_dict[mid_name] = [name]
        else:
            name_dict[mid_name].append(name)

    # 用來判斷是否找到沒有重複的名字
    found_unique = False

    # 找出中間字沒有重複的名字
    for mid_name, name in name_dict.items():
        if len(name) == 1:
            print(name[0])  # 印出名字
            found_unique = True
            break

    if not found_unique:
        print("沒有")


func("彭大牆", "陳王明雅", "吳明")
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")
func("郭宣雅", "夏曼藍波安", "郭宣恆")


print("------Task4------")


def get_number(index):
    if index == 0:
        return 0
    sequence = 0
    for i in range(1, index + 1):
        if i % 3 == 0:
            sequence -= 1
        else:
            sequence += 4
    print(sequence)


get_number(1)
get_number(5)
get_number(10)
get_number(30)
