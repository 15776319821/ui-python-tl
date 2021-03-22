# -*- coding:utf-8 -*-

import io
import sys
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


#Serverurl='http://127.0.0.1:4723/wd/hub'



def desired():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    desired_caps=dict()
    #手机平台版本，大小写无所谓，对就行
    desired_caps['platformName']='Android'
    #要测试手机安卓版本（9.1.1可以写9.1 也可以写9都行）
    desired_caps['platformVersion']='9'
    #设备的名字，adb命令：adb devices查看，这个设备号安卓可以随便写，ios必须写对
    desired_caps['deviceName']='R4Y97PNBLRPVHEV4'
    #要测试的应用的包名
    desired_caps['appPackage']='com.cuteu.videochat'
    #要启动应用的那个界面，就输入对应页面的activity
    desired_caps['appActivity']='com.cuteu.video.chat.business.splash.SplashActivity'
    #加上下面两个配置项，才可以在app上输入中文
    desired_caps['unicodeKeyboard']=True
    desired_caps['resetKeyboard']=True
    #启动app时不要清楚原有的数据
    desired_caps['noReset']=True

    #连接appiun server，其中http的地址直接就是这个格式，没什么好说的
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(20)
    driver.find_element_by_id('com.cuteu.videochat:id/btnTabMine').click()
    driver.find_element_by_id('com.cuteu.videochat:id/imgSet').click()
    driver.find_element_by_xpath("//*[@text='关于我们']").click()

    time.sleep(3)
    q=driver.find_element_by_id('com.cuteu.videochat:id/toolbar_title')
    TouchAction(driver).tap(q, count=20).perform()
    driver.find_element_by_class_name('android.widget.ImageButton').click()

desired()