# 语音自动播报
import pyttsx3


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 100)
engine.say('刘奶奶喝榴莲牛奶')
engine.runAndWait()



