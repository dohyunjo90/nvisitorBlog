#-*-coding:utf-8
import os,sys
import requests
import xml.etree.ElementTree as ET
import datetime
import telegram


def getNVisitor():
	naver_id = 'cdh_90'
	headers = {'User-Agent': 'Mozilla/5.0'}	
	res = requests.get("https://blog.naver.com/NVisitorgp4Ajax.nhn?blogId="+naver_id,headers=headers,timeout=5)	
	print("#########################################")
	print(res.text)
	print("#########################################")
	return ET.fromstring(res.text)	

def getToDay():
	return datetime.datetime.today().strftime("%Y%m%d")
def getNowTime():
	return datetime.datetime.today().strftime("%Y년%m월%d일 %H시%M분")

def sendMsg(telegram_token, msgText):
	bot 	= telegram.Bot(token = telegram_token)
	cat_id 	= '241889310'			
	bot.sendMessage(chat_id = cat_id, text=msgText)	


if __name__ == '__main__':
	telegram_token = '7748248585:AAGT2a5qzfF8U2eGsx_7jmJrk2koRmQuA2c'	
	try:
		visitor_xtree = getNVisitor()		
		for node in visitor_xtree.findall('visitorcnt'):
			if getToDay() == node.get('id'):
				msgText = ("%s %s명이 방문했어요!" %(getNowTime(), node.get('cnt')))
				print(msgText)
				sendMsg(telegram_token, msgText)
				break															
	except Exception as e:
		print("e:",e)
