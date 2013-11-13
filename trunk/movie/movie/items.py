# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class MovieItem(Item):
    name_zh=Field()
    name_en=Field()
    name_alias=Field()
    director=Field()
    tv_host=Field()
    actor=Field()
    author=Field()
    dubber=Field()
    country=Field()
    cat=Field()
    first_run=Field()
    file_type=Field()
    lauange=Field()
    desc=Field()
    sources_link=Field()
    sources_name=Field()
    souces=Field()
    source_url=Field()
    cover_image=Field()
    cover_local_image_url=Field()
    #连续剧集数
    count=Field()
    #连续剧、电影、综艺
    movie_type=Field()
    
