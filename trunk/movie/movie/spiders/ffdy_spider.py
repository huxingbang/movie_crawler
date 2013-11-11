# -*- coding: utf-8 -*-

import re
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from movie.items import MovieItem
from util.string import list2str

class MoviePageSpider(BaseSpider):
    name="ffdy"
    allowed_domains=["ffdy.cc"]
    root_url="http://www.ffdy.cc"
    start_urls=[
        "http://www.ffdy.cc/movie/35483.html",
        "http://www.ffdy.cc/movie/35900.html",
        "http://www.ffdy.cc/teleplay/35689.html"
        #"http://www.ffdy.cc/type,genre/movie,action/",
        #"http://www.ffdy.cc/type/teleplay/",
        #"http://www.ffdy.cc/type/zy/",
    ]

    def parseMovieDetailPage(self, response):
        self.parseMovieDetailPage(response)
        '''
        sel=HtmlXPathSelector(response)
        
        movieUrls=sel.xpath("//div[@class='gkpic']/a/@href").extract()
        for url in movieUrls:
            url=self.root_url+url
            #print url
            yield Request(url=url, callback=self.parseMovieDetailPage)

        next_page_zh=u'下一页'
        next_url=sel.xpath("//div[@class='list-pager']/a[text()='%s']/@href"%next_page_zh).extract()
        next_url=self.start_urls[0]+''.join(next_url)
        #print next_url
        yield Request(url=next_url, callback=self.parse)
        '''        
            

    def parse(self, response):

        movieItem=MovieItem()

        sel=HtmlXPathSelector(response)
        
        #下载资源
        movieItem['sources_link'] = sel.xpath("//div[@class='resourcesmain']//input[@name='checkbox']/@value").extract()

        #资源名称
        movieItem['sources_name'] = sel.xpath("//div[@class='resourcesmain']//a/text()").extract()

        movieItem['name_zh'] = list2str(sel.xpath("//div[@id='film']/h1/text()").extract())

        movieItem['name_en'] = list2str(sel.xpath("//div[@id='film']/h1/em/text()").extract())

        info=sel.xpath("//div[@class='detail_intro']/table/tr")
        for s in info:
            td_title = list2str(s.xpath("td[1]//text()").extract())
            td_value = list2str(s.xpath("td[2]//text()").extract())
            
            if re.search(u"别名", td_title):
                movieItem['name_alias']=td_value
            elif re.search(u"导演", td_title):
                movieItem['director']=td_value
            elif re.search(u"主演", td_title):
                movieItem['actor']=td_value
            elif re.search(u"国家|地区", td_title):
                movieItem['country']=td_value
            elif re.search(u"类型", td_title):
                movieItem['cat']=td_value
            elif re.search(u"上映日期", td_title):
                movieItem['first_run']=td_value
            elif re.search(u"版本", td_title):
                movieItem['file_type']=td_value
            elif re.search(u"对白语言", td_title):
                movieItem['lauange']=td_value


        #描述
        movieItem['desc'] = list2str(sel.xpath("//p[@class='inner_content']/text()").extract())

        movieItem['source_url']=response.url

        #yield movieItem
        return movieItem

