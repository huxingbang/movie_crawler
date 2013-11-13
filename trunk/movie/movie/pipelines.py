# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import MySQLdb
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy import log
from util.string import list2str
import settings

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item.get('cover_image', ''):
            yield Request(item.get('cover_image', ''))

    def image_key(self, url):
        return "/".join(url.split("/")[3:])

    def item_completed(self, results, item, info):
        if results:
            item['cover_local_image_url']=results[0][1]['path']
        return item

class MoviePipeline(object):
    def process_item(self, item, spider):
        if settings.DEBUG:
            print '+---------------------------------------------------+'
            print u"图片:"+item.get('cover_image', '')
            print u"来源:"+item.get('source_url', '')
            print u"类型"+item.get('movie_type', '')
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
            print u'集数:'+item.get('count', '')
            print u'简介:'+item.get('desc', '')

            for o in item.get('souces', ''):
                print "%s:%s"%(o.get('title', ''), o.get('link', ''))
            print '+---------------------------------------------------+'
        return item

class MysqlStorePipeline(object):
    def __init__(self):
        log.start()
        self.conn = MySQLdb.connect(user=settings.MYSQL_DATABASE['user'], \
            passwd=settings.MYSQL_DATABASE['passwd'], \
            db=settings.MYSQL_DATABASE['db'], \
            host=settings.MYSQL_DATABASE['host'], \
            charset=settings.MYSQL_DATABASE['charset'], \
            use_unicode=settings.MYSQL_DATABASE['use_unicode'])
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        cover_image = MySQLdb.escape_string(item.get('cover_local_image_url', '').encode('utf-8'))
        alias_name=MySQLdb.escape_string(item.get('name_alias', '').encode('utf-8'))
        zh_name=MySQLdb.escape_string(item.get('name_zh', '').encode('utf-8'))
        en_name=MySQLdb.escape_string(item.get('name_en', '').encode('utf-8'))
        director=MySQLdb.escape_string(item.get('director', '').encode('utf-8'))
        tv_host=MySQLdb.escape_string(item.get('tv_host', '').encode('utf-8'))
        author=MySQLdb.escape_string(item.get('author', '').encode('utf-8'))
        dubber=MySQLdb.escape_string(item.get('dubber', '').encode('utf-8'))
        actor=MySQLdb.escape_string(item.get('actor', '').encode('utf-8'))
        country=MySQLdb.escape_string(item.get('country', '').encode('utf-8'))
        itype=MySQLdb.escape_string(item.get('cat', '').encode('utf-8'))
        movie_type=MySQLdb.escape_string(item.get('movie_type', '').encode('utf-8'))
        first_run=MySQLdb.escape_string(item.get('first_run', '').encode('utf-8'))
        vido_type=MySQLdb.escape_string(item.get('file_type', '').encode('utf-8'))
        lauange=MySQLdb.escape_string(item.get('lauange', '').encode('utf-8'))
        total_parts=MySQLdb.escape_string(item.get('count', '').encode('utf-8'))
        desc=MySQLdb.escape_string(item.get('desc', '').encode('utf-8'))
 
        sql="insert into movies (alias_name,zh_name, en_name, director, tv_host, author, dubber, actor, \
country, type, movie_type, first_run, vido_type, lauange, total_parts, `desc`, cover_image) VALUES \
('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '%s', '%s', '%s' )"%\
(alias_name, zh_name,en_name, director, tv_host, author, dubber, actor, country, itype, movie_type, first_run, vido_type, lauange, total_parts, desc, cover_image)

        if settings.SAVE_DATA:
            result=self.cursor.execute(sql)
            movie_id=self.conn.insert_id()
            self.conn.commit()

        print '======================='
        print movie_id
        print '======================='

        sql="insert into crawler (movie_id, source_url) VALUES (%d, '%s')"%(movie_id, item.get('source_url', '').encode('utf-8'))
        if settings.SAVE_DATA:
            self.cursor.execute(sql)
            self.conn.commit()


        sort=0
        for o in item.get('souces', ''):
            if o:
                url=MySQLdb.escape_string(o.get('link', '').encode('utf-8'))
                title=MySQLdb.escape_string(o.get('title', '').encode('utf-8'))
                sql="insert into sources (movie_id, sort, url, title) VALUES (%d, %d, '%s', '%s')" %(movie_id, sort, url, title)
                if settings.SAVE_DATA:
                    self.cursor.execute(sql)
                    self.conn.commit()
                sort+=1

        return item
