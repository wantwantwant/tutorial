# 语音自动播报
import pyttsx3


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 100)
engine.say('王超坤是傻逼')
engine.runAndWait()



