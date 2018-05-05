
from django.conf.urls import url
from views import index, style, criptomoney, updateDB

urlpatterns = [
    url(r'^index', index, name='index'),
    url(r'^style', style, name='style'),
    url(r'^elMeuEstil', style, name='elMeuEstil'),

    url(r'^criptomoney', criptomoney, name='criptomoney'),
    url(r'^crawler/updateDB', updateDB, name='updateDB'),
]