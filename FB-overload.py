#!/usr/bin/python
# coding: utf-8
# copyright: DulLah

import os
import sys
import requests
import cookielib
import mechanize
from bs4 import BeautifulSoup as BS
from http.cookiejar import LWPCookieJar as cookie

reload(sys)
sys.setdefaultencoding('utf8')
br=mechanize.Browser()
cj=cookielib.LWPCookieJar("cookies.log")
br.set_cookiejar(cj)
br.set_handle_gzip(True)
br.set_handle_redirect(True) 
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders=[('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
s=requests.Session()

url = "https://mbasic.facebook.com{}"
P="\033[0;97m"
H="\033[0;92m"
M="\033[0;91m"
B="\033[0;41m"
R="\033[0m"

def data(id,pw):
	br.open("https://mbasic.facebook.com")
	br._factory.is_html = True
	br.select_form(nr=0)
	br.form["email"] = id
	br.form["pass"] = pw
	br.submit()
	login = br.geturl()
	if "save-device" in str(login):
		cj.save()
		print "%s\n[!] %ssilahkan konekin ke VPN server spanyol \n    sebelum melanjutkan \n"%(M,P)
		raw_input("%s[*]%s enter untuk melanjutkan... "%(H,P))
		over(url.format("/profile/edit/info/nicknames"))
	elif "checkpoint" in str(login):
		print "%s[!] akun cekpoint:)"%(M)
	else: exit("%s[!] login gagal:)"%(M))

def over(link):
	print "%s[*]%s tunggu sebentar"%(H,P)
	data=[]
	s.cookies = cookie("cookies.log")
	s.cookies.load()
	font = open("font.txt","r").read()
	a = s.get(link)
	bs = BS(a.content,"html.parser")
	for i in bs("form"):
		if "post" in i["method"]:
			data.append(i["action"])
	for i in bs("input"):
		try:
			if "fb_dtsg" in i["name"]:
				data.append(i["value"])
			if "jazoest" in i["name"]:
				data.append(i["value"]) 
		except:pass
	b = s.post(url.format(data[0]),data = 
		{
			"fb_dtsg": data[1],
			"jazoest": data[2],
			"additional_types[705456762826020]": "nicknames",
			"dropdown": "nickname",
			"text": font,
			"checkbox": "checkbox",
			"save": "Simpan"
		})
	if b.status_code==200:
		print "%s[*]%s done .."%(H,P)
		exit("%s[*]%s silahkan cek profile anda"%(H,P))
	else:
		exit("%s[!] gagal coba lagi"%(M))
		
if __name__ == "__main__":
	os.system("clear")
	print """
     %s_______                    
    / __/ _ )  ___ _  _____ ____
   / _// _  | / _ \ |/ / -_) __/%s
  /_/ /____/  \___/___/\__/_/  
 ----------------------------------------%s
 %s Coded : DulLah                         %s%s
 ----------------------------------------
"""%(M,P,M,B,R,P)
	id=raw_input("%s[?]%s username: "%(H,P))
	pw=raw_input("%s[?]%s password: "%(H,P))
	data(id,pw)
