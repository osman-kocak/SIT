#!/user/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install nikto")
os.system("clear")
os.system("figlet Sytem Info Tool")

M = ("""
Port Tarama Programı

1) Port Tarama Islemleri
2) Acik tarama Islemleri (Nikto)
3) Wordpress Acik Tarama Islemleri
4) Guvenlik Duvari Testeri (Waffw00f)



""")

print(M)

islem = raw_input("Yapmak Istediginiz Islem Numarasini Giriniz:")

if(islem == "1"):
    ip = raw_input("Hedef IP Giriniz: ")
    os.system("clear")
    os.system("nmap -sS -sV  "+ ip)
    q=raw_input("----------- ANA MENUYE GITMEK ISTIYORSANIZ (Y) BASIN -----------: " )
    if(q == "Y"):
	os.system("clear")
	os.system("figlet Sytem Info Tool")
	print(M)

    
elif (islem == "2"):
    ip = raw_input("Hedef IP Giriniz: ")
    os.system("nikto -h " + ip)
    q=raw_input("----------- ANA MENUYE GITMEK ISTIYORSANIZ (Y) BASIN -----------: " )
    if(q == "Y"):
	os.system("clear")
	os.system("figlet Sytem Info Tool")
	print(M)

elif (islem == "3"):
    ip = raw_input("Hedef IP veya URL Giriniz: ")
    os.system("wpscan --url "+ ip +" --ignore-main-redirect  --enumerate u --enumerate vt --enumerate vp ")
    q=raw_input("----------- ANA MENUYE GITMEK ISTIYORSANIZ (Y) BASIN -----------: " )
    if(q == "Y"):
	os.system("clear")
	os.system("figlet Sytem Info Tool")
	print(M)
    
elif (islem == "4"):
    ip = raw_input("Hedef URL Giriniz (Ornek: www.ornek.com): ")
    os.system("wafw00f " + ip)
    q=raw_input("----------- ANA MENUYE GITMEK ISTIYORSANIZ (Y) BASIN -----------: " )
    if(q == "Y"):
	os.system("clear")
	os.system("figlet Sytem Info Tool")
	print(M)

else:
	print("Hatalı Seçim Yaptınız. Program Kapatılıyor......")