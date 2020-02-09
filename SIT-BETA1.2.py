#!/user/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Sytem Info Tool")

print("""
Port Tarama Programı

1) Port Tarama Islemleri
2) Acik tarama Islemleri (Nikto)
3) Wordpress Acik Tarama Islemleri
4) Guvenlik Duvari Testeri (Waffw00f)


""")

islem = input("Yapmak Istediginiz Islem Numarasini Giriniz:")

if(islem == 1):
    ip = input("Hedef IP Giriniz: ")
    os.system("nmap -sS -sV " + ip)
elif (islem == 2):
    ip = input("Hedef IP Giriniz: ")
    os.system("nikto -h " + ip)
elif (islem == 3):
    ip = raw_input("Hedef IP veya URL Giriniz: ")
    os.system("wpscan --ignore-main-redirect  --enumerate u --enumerate vt --enumerate vp --url" + ip)
elif (islem == 4):
    ip = raw_input()"Hedef URL Giriniz (Ornek: www.ornek.com): ")
    os.system("wafw00f " + ip)
