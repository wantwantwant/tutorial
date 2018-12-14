import sqlite3
connect = sqlite3.connect("weathersqlite.db")
cursor = connect.cursor()
# cursor.execute("""CREATE TABLE weather(
#                 date INT,
#                 sunrise INT,
#                 high VARCHAR,
#                 low VARCHAR,
#                 sunset INT,
#                 aqi INT,
#                 ymd INT,
#                 week VARCHAR,
#                 fx VARCHAR,
#                 fl VARCHAR,
#                 type VARCHAR,
#                 notice VARCHAR
# #            );""")

cursor.execute("""
      INSERT INTO weathers(date, sunrise, high, low, sunset, aqi, ymd, week, fx, fl, type, notice) VALUES ("06","07:17","高温 7.0℃","低温 -5.0℃","17:14",110.0,"2018-12-06","星期四", "东北风","<3级","多云", "阴晴之间，谨防紫外线侵扰");
""")
cursor.execute("""
      INSERT INTO weathers(date, sunrise, high, low, sunset, aqi, ymd, week, fx, fl, type, notice) VALUES ("07","07:18","高温 1.0℃","低温 -4.0℃","17:14",39.0,"2018-12-07","星期五", "南风","<3级","多云", "阴晴之间，谨防紫外线侵扰");
""")
cursor.execute("""
      INSERT INTO weathers(date, sunrise, high, low, sunset, aqi, ymd, week, fx, fl, type, notice) VALUES ( "08","07:19","高温 1.0℃", "低温 -5.0℃","17:14",77.0,"2018-12-08","星期六","东北风","3-4级","多云","阴晴之间，谨防紫外线侵扰");
""")
cursor.execute("""
      INSERT INTO weathers(date, sunrise, high, low, sunset, aqi, ymd, week, fx, fl, type, notice) VALUES ("09","07:20","高温 2.0℃","低温 -4.0℃","17:14", 71.0,"2018-12-09", "星期日","东南风", "<3级","多云", "阴晴之间，谨防紫外线侵扰");
""")
cursor.execute("""
      INSERT INTO weathers(date, sunrise, high, low, sunset, aqi, ymd, week, fx, fl, type, notice) VALUES ("10","07:21","高温 0.0℃","低温 -3.0℃","17:14",72.0,"2018-12-10","星期一","北风","<3级","雨夹雪","道路湿滑，步行开车要谨慎");
""")
cursor.close()
connect.commit()
connect.close()
