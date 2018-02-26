import scrapy
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import urllib
from scrapy.shell import inspect_response
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.http import HtmlResponse
import json
import enginemodule

class CriptoMoney_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id_Criptomoneda = scrapy.Field(serializer=str)
    name = scrapy.Field(serializer=str)
    symbol = scrapy.Field(serializer=str)
    rank = scrapy.Field(serializer=str)
    _24h_volume_usd = scrapy.Field(serializer=str)
    market_cap_usd = scrapy.Field(serializer=str)
    available_supply = scrapy.Field(serializer=str)
    total_supply = scrapy.Field(serializer=str)
    max_supply = scrapy.Field(serializer=str)
    percent_change_1h = scrapy.Field(serializer=str)
    percent_change_24h = scrapy.Field(serializer=str)
    last_updated = scrapy.Field(serializer=str)
    pass

class List_CryptMoney(scrapy.Item):
    list = scrapy.Field()

class CRYPTOCURRENCY_Spider(enginemodule.Engine_Module):
    name = 'cryptocurrency_spider'

    #########################################################
    #  Inicializacion
    #########################################################

    def __init__(self):

        super(CRYPTOCURRENCY_Spider, self).__init__()
        self.url = 'https://api.coinmarketcap.com/v1/ticker/'
        self.headers = {
         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
        #self.formdata={'login': '', 'password': ''}
        self.meta = None
        #self.meta = {'proxy': 'http://127.0.0.1:8081'}

        self.crypto_moneys = None

        self.WriteXML_Controller = True

        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def start_requests(self):
        self.logger.debug("Init Start request")
        yield Request(
            url=self.url,
            headers=self.headers,
            meta=self.meta,
            callback=self.globalposition,
            errback=self.errback_start_requests)


    #########################################################
    #   Posicion Global
    #########################################################

    def globalposition(self, response):
        try:
            self.logger.debug("Init globalposition")

            # Inicializacion Item
            item = CriptoMoney_Item()
            list_item = List_CryptMoney()

            # Inicializacion de variables

            fecha_scraper = None
            size_posicionGlobal = 0
            lista_leaks_posicionGlobal = []
            list_names_leaks = []

            # Fecha de scrapero

            # Extraccion depsicion global de monedas
            self.crypto_moneys = json.loads(response.body)
            criptomone_List = []


            for crpM in self.crypto_moneys:
                criptomone_List.append(crpM)

            list_item = criptomone_List

            self.logger.debug("End globalposition")
            return list_item

        except Exception, e:
            self.logger.error("Error in globalposition : ")
            self.logger.error(str(e))


    #########################################################
    #   Control de Errores
    #########################################################

    def errback_start_requests(self, failure):
        try:
            self.logger.debug("errback_start_requests , from start_requests")
        except Exception, e:
            self.logger.error("Hard error in errback_start_requests : s%" % str(e))


    #########################################################
    #   End Spider
    #########################################################

    def spider_closed(self):
        try:
            self.logger.debug("Init spider_closed")
            self.logger.debug("Writing Criptomoney ... ")

            '''
            # Escrivimos las noticias a XML
            if self.WriteXML_Controller:
                self.WriteNewsToXML(self.News)
                self.WriteXML_Controller = False
            '''
            return self.crypto_moneys
        except Exception, e:
            self.logger.error("Error in spider_closed")
            self.logger.error(e)