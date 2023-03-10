from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']
birthday2 = os.environ['MYBIRTHDAY']
app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]
user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]
menses = os.environ['MENSES_DATE']

def get_weather():
    url = "https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=" + city
    res = requests.get(url).json()
    wet = res['data'][0]
    return wet['tem'], wet['tem1'], wet['tem2'], wet['phrase'], wet['humidity']

def get_count():
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


def get_birthday():
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days

def get_birthday2():
    next = datetime.strptime(str(date.today().year) + "-" + birthday2, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days

def get_menses():
    delta = today - datetime.strptime(menses, "%Y-%m-%d")
    return delta.days

def get_curmenses():
    return menses
def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)
wm = WeChatMessage(client)
cur, maxs, mins, weather, humidity = get_weather()
data = {"weather": {"value": weather, "color": get_random_color()},
        "cur": {"value": cur, "color": get_random_color()},
        "humidity": {"value": humidity, "color": get_random_color()},
        "menses": {"value": get_menses(), "color": get_random_color()},
        "premenses": {"value": get_curmenses(), "color": get_random_color()},
        "maxs": {"value": maxs, "color": get_random_color()},
        "mins": {"value": mins, "color": get_random_color()},
        "love_days": {"value": get_count(), "color": get_random_color()},
        "birthday_left": {"value": get_birthday(), "color": get_random_color()},
        "birthday_left2": {"value": get_birthday2(), "color": get_random_color()},
        "words": {"value": get_words(), "color": get_random_color()}
        }
everyone = user_id.split(",")
for i in everyone:
    res = wm.send_template(i, template_id, data)
    print(res)
    
    
    
# def get_weather():
#     url = "https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city=" + "周口"
#     res = requests.get(url).json()
#     wet = res['data'][0]
#     return wet['tem'], wet['tem1'], wet['tem2'], wet['phrase'], wet['humidity']
#     # return weather['weather'], math.floor(weather['temp'])

# def get_count():
#     delta = today - datetime.strptime(start_date, "%Y-%m-%d")
#     return delta.days


# def get_birthday():
#     next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
#     if next < datetime.now():
#         next = next.replace(year=next.year + 1)
#     return (next - today).days


# def get_words():
#     words = requests.get("https://api.shadiao.pro/chp")
#     if words.status_code != 200:
#         return get_words()
#     return words.json()['data']['text']


# def get_random_color():
#     return "#%06x" % random.randint(0, 0xFFFFFF)



# data = {"weather": {"value": weather, "color": get_random_color()},
#         "cur": {"value": cur, "color": get_random_color()},
#         "humidity": {"value": humidity, "color": get_random_color()},
#         "maxs": {"value": maxs, "color": get_random_color()},
#         "mins": {"value": mins, "color": get_random_color()},
#         "love_days": {"value": get_count(), "color": get_random_color()},
#         "birthday_left": {"value": get_birthday(), "color": get_random_color()},
#         "words": {"value": get_words(), "color": get_random_color()}
#         }
