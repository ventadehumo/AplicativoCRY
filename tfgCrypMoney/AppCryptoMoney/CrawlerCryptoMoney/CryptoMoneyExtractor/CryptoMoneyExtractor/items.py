# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CryptomoneyextractorItem(scrapy.Item):
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
