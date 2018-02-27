
from django.conf.urls import url
from views import index, style, criptomoney, updateDB

urlpatterns = [
    url(r'^index', index, name='index'),
    url(r'^style', style, name='style'),
    url(r'^crawler$', criptomoney, name='criptomoney'),
    url(r'^crawler/updateDB', updateDB, name='updateDB'),
]