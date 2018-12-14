# 免费的天气接口https://www.sojson.com/blog/305.html
import urllib.request
import json

url = 'http://t.weather.sojson.com/api/weather/city/101180101'
resp = urllib.request.urlopen(url)
if resp.code == 200:
    weather_json = resp.read().decode('utf-8')
    print(type(weather_json), weather_json)
    weather_data = json.loads(weather_json)
    data = weather_data['data']
    print('\n\n\n', data)

    today_humidity = data['shidu']
    today_pm25 = data['pm25']
    today_temperature = data['wendu']
    print(f'今日温度:{today_temperature}, 湿度：{today_humidity}')


    yesterday = data['yesterday']
    print(yesterday)
    forecast = data['forecast']
    print('\n\n', forecast)

"""
作业:
1.获取接口中昨天和未来四天数据
2.（选做）存入sqlite，结合web框架，数据放到表格中，做一个天气应用。如果有时间做css美化。
"""
