# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Compose, Identity

import re


class SpidersItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    sizes = scrapy.Field()
    site = scrapy.Field()
    _type = scrapy.Field()
    is_new = scrapy.Field()
    product_id = scrapy.Field()
    product_size_id = scrapy.Field()

class BigmodaItemLoader(ItemLoader):
    site_out = TakeFirst()
    url_out = TakeFirst()
    name_out = TakeFirst()
    price_in = TakeFirst()
    price_out = Compose(lambda x: x[0].strip().replace(',', '').split('.'), price_in)
    sizes_out = MapCompose(lambda x: x.strip())
    _type_out = TakeFirst()
    is_new_out = TakeFirst()
    product_id_out = TakeFirst()
    product_size_id_out = TakeFirst()


class NovitaItemLoader(ItemLoader):
    url_out = TakeFirst()
    name_in = TakeFirst()
    name_out = Compose(lambda x: re.search(r'(?<=№)(\d+/\d+)|(?<=№)(\d+)', str(x)).group(0), Identity())
    price_out = Compose(lambda x: x[0].strip().replace(',', '').split('.'), TakeFirst())
    sizes_out = Identity()
    site_out = TakeFirst()
    _type_out = TakeFirst()
    is_new_out =TakeFirst()


class PrimalineaItemLoader(ItemLoader):
    url_out = TakeFirst()
    name_out = TakeFirst()
    price_out = Compose(lambda x: re.search(r'(\d+)', x[0].strip().replace(' ', '')).group(0), Identity())
    sizes_out = Identity()
    site_out = TakeFirst()
    is_new_out = TakeFirst()
    _type_out = TakeFirst()


class AvigalItemLoader(ItemLoader):
    url_out = TakeFirst()
    name_out = TakeFirst()
    price_out = Compose(lambda x: re.search(r'(\d+)', x[0].strip().replace(' ', '')).group(0), Identity())
    sizes_out = Compose()
    site_out = TakeFirst()
    is_new_out = TakeFirst()
    _type_out = TakeFirst()

class WisellItemLoader(ItemLoader):
    url_out = TakeFirst()
    name_out = TakeFirst()
    price_out = Compose(lambda x: re.search(r'(\d+)', x[0].strip().replace(' ', '')).group(0), Identity())
    sizes_out = Identity()
    site_out = TakeFirst()
    is_new_out = TakeFirst()
    _type_out = TakeFirst()

