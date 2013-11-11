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
    actor=Field()
    country=Field()
    cat=Field()
    first_run=Field()
    file_type=Field()
    lauange=Field()
    desc=Field()
    sources_link=Field()
    sources_name=Field()
    source_url=Field()
    
