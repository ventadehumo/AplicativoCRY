# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response


# Create your views here.

def index(request):
    return render_to_response('index.html')


def style(request):
    return render_to_response('style.css')

def criptomoney(request):
    return render_to_response('criptomoney.html')

def updateDB(request):
    print "GAAAAAAAAAAAAAAAAS"
    return render_to_response('criptomoney.html')