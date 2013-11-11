# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from util.string import list2str
class MoviePipeline(object):
    def process_item(self, item, spider):
        print '+---------------------------------------------------+'
        print u"来源:"+item.get('source_url', '')
        print u"别名:"+item.get('name_alias', '')
        print u"中文名:"+item.get('name_zh', '')
        print u"英文名:"+item.get('name_en', '')
        print u"导演:"+item.get('director', '')
        print u"演员:"+item.get('actor', '')
        print u'国家:'+item.get('country', '')
        print u'类别:'+item.get('cat', '')
        print u'首映:'+item.get('first_run', '')
        print u'文件类型:'+item.get('file_type', '')
        print u'语言:'+item.get('lauange', '')
        print u'简介:'+item.get('desc', '')
        print item.get('sources_name', '')
        print item.get('sources_link', '')
        print '+---------------------------------------------------+'
        
        return item
