# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from Spider import cryptocurrency_spider
from.models import Criptomoneda

# Create your views here.

def index(request):
    return render_to_response('index.html')

def style(request):
    return render_to_response('style.css')

def elMeuEstil(request):
    return render_to_response('elMeuEstil.css')

def criptomoney(request):
    return render_to_response('criptomoney.html')

def updateDB(request):
    print "[*] Starting spider from Web Request"
    moneyList = cryptocurrency_spider.init_twisted_CryptoSpider()
    print "[*] Brute criptomoney data : " + moneyList

    current_DB_Criptomoney = Criptomoneda.objects.all()
    #instances_List = aws_instances_controller.AWS_instances_details()

    for DB_CryptoMoney in current_DB_Criptomoney:
        for CryptoMoney in moneyList:
            if str(DB_CryptoMoney.id_Criptomoneda) == CryptoMoney.get('id'):
                if str(DB_CryptoMoney.KeyName) != CryptoMoney.get('KeyName') or str(DB_CryptoMoney.GroupName) != CryptoMoney.get(
                        'GroupName') or str(DB_CryptoMoney.State) != CryptoMoney.get('State') or\
                                str(DB_CryptoMoney.PublicIpAddress) != CryptoMoney.get('PublicIpAddress'):
                    print "[+] Currency " + CryptoMoney.get("name") + " have changes, updating DB entry"
                    DB_CryptoMoney.PublicIpAddress = str(CryptoMoney.get('PublicIpAddress', '-'))
                    DB_CryptoMoney.State = str(CryptoMoney.get('State', '-'))
                    DB_CryptoMoney.KeyName = str(CryptoMoney.get('KeyName', '-'))
                    DB_CryptoMoney.GroupName = str(CryptoMoney.get('GroupName', '-'))
                    DB_CryptoMoney.save()
    instances = Criptomoneda.objects.all()
    context = {'instances': instances}
    return render(request, 'AWS_Instances.html', context)
    return render_to_response('criptomoney.html')