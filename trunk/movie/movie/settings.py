# Scrapy settings for movie project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
BOT_NAME = 'movie'

SPIDER_MODULES = ['movie.spiders']
NEWSPIDER_MODULE = 'movie.spiders'

ITEM_PIPELINES={
                'movie.pipelines.MoviePipeline':1,
                'movie.pipelines.MyImagesPipeline': 200,
                'movie.pipelines.MysqlStorePipeline':300,
            }

SAVE_DATA=True
DEBUG=False
DOWNLOAD_DELAY=3

JOBDIR='crawls/somespider-1'

MYSQL_DATABASE={
    'host':'localhost',
    'user':'root',
    'passwd':'123456',
    'db':'movie',
    'charset':'utf8',
    'use_unicode':True

}

IMAGES_EXPIRES=90
IMAGES_STORE='/Volumes/sdisk/workspace/movie_crawler/trunk/movie/data/image'
LOG_FILE='/Volumes/sdisk/workspace/movie_crawler/trunk/movie/log/log'
LOG_LEVEL='ERROR'

DEFAULT_REQUEST_HEADERS = { 'Referer': 'http://www.ffdy.cc/'}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36'
