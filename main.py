from itertools import count

import vk_api, json, vkbottle
from vk_api.longpoll import VkLongPoll, VkEventType
import sqlite3
from sqlite3 import Error

vk_session = vk_api.VkApi(token="32cd9f1d75ad02bbca67ababf0d8e77850236b166d36f9f619988956569a7859a1ea022dfdb6ee8c68ba0")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


def adder(x):
    file = open("txt.txt", "a", encoding="utf-8")


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but("Привет", "positive"), get_but("Пока", "positive")],
        [get_but("лайк", "positive"), get_but("дизлайк", "negative")],
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode("utf-8")
keyboard = str(keyboard.decode("utf-8"))


def sender(id, text):
    vk.messages.send(user_id=id, message=text, random_id=0, keyboard=keyboard)


def send_stick(id, number):
    vk.messages.send(user_id=id, sticker_id=number, random_id=0)


def send_photo(id, url):
    vk.messages.send(user_id=id, attachment=url, random_id=0)

def check (x):
    file = open('data.txt', 'a', encoding='utf-8')
    if x in file.read():
        return 1
    else:
        return 0
    file.close()

def adder (x):
    file = open('data.txt', 'a', encoding='utf-8')
    file.write(f'{x}\n')
    file.close()

def give (reputation, data_line_count):
    i = 0
    msg = ""
    friends_count = 0
    if data_line_count//4 > 2:
        for i in range(data_line_count // 4 - 2):
            m = 0
            while reputation[0][m + 1] != '\0':
                if reputation[0][m] < reputation[0][m + 1]:
                    tmp1 = reputation[0][m]
                    tmp2 = reputation[1][m]
                    reputation[0][m] = reputation[0][m + 1]
                    reputation[1][m] = reputation[1][m + 1]
                    reputation[0][m + 1] = tmp1
                    reputation[1][m + 1] = tmp2
                    m = m+1
                if reputation[0][m + 1] != '\0':
                    break
    i = i+1
    c = str(reputation[1][0])
    text = "Мы проанализировали ваши лайки и подобрали вам человека\nvk.com/id"
    text = text + c
    sender(id, text)
    sender(id, "Для того, чтобы найти ещё людей,\n напиши 'ещё'")
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                if friends_count >= i and event.text == "ещё":
                    sender(id, "Извините, у нас больше нет id,\nНапишите через некоторое время искать,\nвдруг кто-то появится")
                    break
                elif event.text == "ещё" and friends_count < i:
                    friends_count = friends_count + 1
                    c = str(reputation[1][friends_count])
                    text = "Мы проанализировали ваши лайки и подобрали вам человека\nvk.com/id"
                    text = text + c
                    sender(id, text)
                    sender(id, "Для того, чтобы найти ещё людей,\n напиши 'ещё'")
                else:
                    sender(id, "Извините, я вас не понимаю")







def search (x, a):
    with open("data.txt", "r")as file:
        contents = file.readlines()
        j = (len(contents))
        n = 0
        m = 0
        c = []
        i = 0
        b = ""
        z = 0
        allsum = []
        for n in range(2):
            internal_allsum = []
            for m in range (j//4):
                internal_allsum.append(0)
            allsum.append(internal_allsum)
        kof1 = 200
        kof2 = 100
        kof3 = 50
        count = 0
        uncount = 0
        sum = 0
        unsum = 0
        id2 = 0
        q = 1.2
        h = 0

        for i in range(j//4):
            id2 = int(contents[i * 4])
            if id != id2:
                g = 0
                y = 0
                b = contents[3 + i * 4]
                while (b[y + 2] != '\0'):
                    if (b[y + 1] == "-"):
                        c.insert(g, -1)
                        y = y + 4
                    else:
                        c.insert(g, int(b[y + 1]))
                        y = y + 3
                    if (y + 2 > len(b)):
                        break
                    g = g + 1
                for z in range(10):
                    if a[z] == c[z]:
                        count = count + 1
                    else:
                        uncount = uncount + 1
                if count == 0 and uncount != 0:
                    unsum = (kof3 * (q ** uncount)) / (q - 1)
                elif count != 0 and uncount == 0:
                    sum = (kof2 * (q ** count)) / (q - 1)
                elif count != 0 and uncount != 0:
                    sum = (kof2 * (q ** count)) / (q - 1)
                    unsum = (kof3 * (q ** uncount)) / (q - 1)
                c = []
                b = ""
                allsum[0][i] = int(sum - unsum)
                allsum[1][i] = contents[i * 4]
                count = 0
                uncount = 0

        if allsum[0][0] == 0:
            sender(id, "Пока в базе данных нет других пользователей.\n Можете через некоторое время\n написать боту 'искать'")
        else:
            give(allsum, j)



city = 0
old = 0
f = 0
g = 0
i = 0
a = []
tmp = []
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.text == "пока":
                old = 0
                city = 0
                f = 0
                g = 0
                a.clear()
                sender(id, "Для того, чтобы заполнить анкету вновь, напиши боту 'привет'")
            msg = event.text.lower()
            id = event.user_id

            if f == 1 and g == 0:
                if event.text.isdigit() and 0 < int(event.text) < 70:
                    old = int(event.text)
                    adder(id)
                    adder(old)
                    sender(id, "2. город, в котором ты проживаешь")
                    g = 1
                else:
                    sender(id, "Повторите попытку")
            else:
                if f == 1 and g == 1:
                    if not event.text.isdigit():
                        city = event.text

                        adder(city)
                        sender(id,
                               "Теперь я предоставлю тебе несколько мемов,\nкоторые ты должен оценить кнопками: 'лайк' или 'дизлайк'\n\nПервый мем")

                        f = 0
                    else:
                        sender(id, "Повторите попытку")

                if f == 0 and g == 1:
                    i = i + 1
                    if event.text == "лайк":
                        a.insert(i-2, 1)
                    elif event.text == "дизлайк":
                        a.insert(i-2, -1)
                    elif i != 1:
                        sender(id, "Повторите попытку")
                        i = i - 1
                    if (i == 1):

                        send_photo(id, "photo-113066361_457614910%2Falbum-113066361_00%2Frev")

                    elif (i == 2):
                        sender(id, "Второй мем")
                        send_photo(id, "photo-159146575_457647418%2Falbum-159146575_00%2Frev")
                    elif (i == 3):
                        sender(id, "Третий мем")
                        send_photo(id, "photo-57846937_460015877%2Falbum-57846937_00%2Frev")
                    elif (i == 4):
                        sender(id, "Четвёртый мем")
                        send_photo(id, "photo-76628628_457542289%2Falbum-76628628_00%2Frev")
                    elif (i == 5):
                        sender(id, "Пятый мем")
                        send_photo(id, "photo-199643014_457239222%2Falbum-199643014_00%2Frev")
                    elif (i == 6):
                        sender(id, "Шестой мем")
                        send_photo(id, "photo-67580761_458196231%2Falbum-67580761_00%2Frev")
                    elif (i == 7):
                        sender(id, "Седьмой мем")
                        send_photo(id, "photo-45745333_460449558%2Falbum-45745333_00%2Frev")
                    elif (i == 8):
                        sender(id, "Восьмой мем")
                        send_photo(id, "photo-60708045_457427410%2Falbum-60708045_00%2Frev")
                    elif (i == 9):
                        sender(id, "Девятый мем")
                        send_photo(id, "photo-30770434_457456072%2Falbum-30770434_00%2Frev")
                    elif (i == 10):
                        sender(id, "Десятый мем")
                        send_photo(id, "photo-57846937_460014874%2Falbum-57846937_00%2Frev")
                    elif (i ==11):
                        sender(id, "Вы полностью прошли анкетирование")
                        adder(a)
                        sender(id, a)
                        f = 0
                        g = 0
                        i = 0
                        search(id, a)
                        tmp.append(a)
                        a = []

                elif msg == "привет":
                    sender(id, "и тебе привет")
                    sender(id, "Заполни анкету:")
                    sender(id, "Чтобы очистить анкету напиши 'пока' ")
                    sender(id, "1. твой возраст")
                    f = 1
                    g = 0


                elif msg == "искать" and tmp[9] != 0:
                    a.append(tmp)
                    search(id, tmp)
                else:
                    sender(id, "Я вас не понимаю, возможно,\nнадо написать привет для прохождения анкетирования")

