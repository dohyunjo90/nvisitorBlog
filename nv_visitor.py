#-*-coding:utf-8
import os, sys
import requests
import datetime
import telegram
from pytz import timezone

KST = datetime.datetime.now(timezone('Asia/Seoul'))

def getNowTime():
    return KST.strftime("%Y년%m월%d일 %H시%M분")

def sendMsg(telegram_token, msgText):
    bot = telegram.Bot(token=telegram_token)
    chat_id = '241889310'
    bot.sendMessage(chat_id=chat_id, text=msgText)

def check_url_status():
    url = "https://lab.hdc-dvp.com/main"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        return response.status_code
    except Exception as e:
        return None

if __name__ == '__main__':
    telegram_token = sys.argv[1]
    
    status_code = check_url_status()
    if status_code == 200:
        msgText = "{} 정상적으로 작동".format(getNowTime())
    else:
        msgText = "{} 에러".format(getNowTime())
    
    print(msgText)
    sendMsg(telegram_token, msgText)
