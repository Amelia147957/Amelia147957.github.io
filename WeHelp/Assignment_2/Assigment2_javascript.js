console.log("------Task1------");
function findAndPrint(messages, currentStation) {
    const stationDict = {
        "Songshan": 1,
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
    };

    const currentStationNumber = stationDict[currentStation];
    let closestFriend = null;
    let closestDistance = Infinity;

    for (let friend in messages) {
        let message = messages[friend];
        let friendStationName = null;
        for (let stationName in stationDict) {
            if (message.includes(stationName)) {
                friendStationName = stationName;
                break;
            }
        }

        if (friendStationName) {
            let distance;
            if (friendStationName === "Xiaobitan" || currentStation === "Xiaobitan") {
                const extraDistance = 0.5;
                if (friendStationName === "Xiaobitan") {
                    distance = Math.abs(stationDict["Qizhang"] - currentStationNumber) + extraDistance;
                } else {
                    distance = Math.abs(stationDict[friendStationName] - stationDict["Qizhang"]) + extraDistance;
                }
            } else {
                const friendStationNumber = stationDict[friendStationName];
                distance = Math.abs(friendStationNumber - currentStationNumber);
            }

            if (distance < closestDistance) {
                closestDistance = distance;
                closestFriend = friend;
            }
        }
    }

    console.log(closestFriend);
}

const messages = {
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Leslie": "I'm at home near Xiaobitan station.",
    "Vivian": "I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian


console.log("------Task2------");
let schedules = {};
function book(consultants, hour, duration, criteria) {
    consultants.forEach(consultant => {
        if (!schedules.hasOwnProperty(consultant.name)) {
            schedules[consultant.name] = [];
        }
    });

    let availableConsultants = consultants.filter(consultant => {
        for (let checkingHour = hour; checkingHour < hour + duration; checkingHour++) {
            if (schedules[consultant.name].includes(checkingHour)) {
                return false;
            }
        }
        return true;
    });

    if (availableConsultants.length === 0) {
        console.log("No Service");
        return;
    }

    let chosenConsultant = availableConsultants.reduce((chosen, consultant) => {
        if (!chosen) return consultant;
        if (criteria === "price" && consultant.price < chosen.price) return consultant;
        if (criteria === "rate" && consultant.rate > chosen.rate) return consultant;
        return chosen;
    }, null);

    for (let bookingHour = hour; bookingHour < hour + duration; bookingHour++) {
        schedules[chosenConsultant.name].push(bookingHour);
    }

    console.log(chosenConsultant.name);
}

const consultants = [
    { "name": "John", "rate": 4.5, "price": 1000 },
    { "name": "Bob", "rate": 3, "price": 1200 },
    { "name": "Jenny", "rate": 3.8, "price": 800 }
];

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John


console.log("------Task3------");
function func(...data) {
    const nameDict = {};
    for (const name of data) {
        let midName;
        switch (name.length) {
            case 2:
                midName = name[1];
                break;
            case 3:
                midName = name[1];
                break;
            case 4:
                midName = name[2];
                break;
            case 5:
                midName = name[2];
                break;
            default:
                continue;
        }

        if (!nameDict[midName]) {
            nameDict[midName] = [name];
        } else {
            nameDict[midName].push(name);
        }
    }

    let foundUnique = false;
    for (const [midName, names] of Object.entries(nameDict)) {
        if (names.length === 1) {
            console.log(names[0]);
            foundUnique = true;
            break;
        }
    }

    if (!foundUnique) {
        console.log("沒有");
    }
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安



console.log("------Task4------");
function getNumber(index) {
    if (index === 0) {
        return 0;
    }
    let sequence = 0;
    for (let i = 1; i <= index; i++) {
        if (i % 3 === 0) {
            sequence -= 1;
        } else {
            sequence += 4;
        }
    }
    console.log(sequence);
}

getNumber(1);
getNumber(5);
getNumber(10);
getNumber(30);

