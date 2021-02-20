#coding=utf-8
import time
from zfapi import Login
from zfapi import GetInfo

base_url = 'http://xxxxx/'
username = 'xxxx'
password = 'xxxx'
count = 0
while count<=3:
    try:
        lgn = Login(base_url = base_url)
        lgn.login(username,password)
        cookies = lgn.cookies 
        srpihot = GetInfo(base_url=base_url, cookies=cookies)
        print("====通知====")
        print(srpihot.get_notice())
        break
    except Exception as e:
        print('[Error]',e)
        time.sleep(3)
        count += 1