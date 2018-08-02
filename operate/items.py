# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OperateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Textchunk = scrapy.Field()
    Recommended = scrapy.Field()
    Aircraft = scrapy.Field()
    TypeOfTraveller = scrapy.Field()
    CabinFlown = scrapy.Field()
    Route = scrapy.Field()
    DateFlown = scrapy.Field()
    SeatComfort = scrapy.Field()
    CabinStaffService = scrapy.Field()
    FoodAndBeverages = scrapy.Field()
    InflightEntertainment = scrapy.Field()
    GroundService = scrapy.Field()
    WifiAndConnectivity = scrapy.Field()
    ValueForMoney = scrapy.Field()