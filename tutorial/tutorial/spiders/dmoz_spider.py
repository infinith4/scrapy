# -*- coding: utf-8 -*-
import scrapy
import sqlalchemy as sa
import configparser
import sys,os
sys.path.append(os.curdir)
from db import *

#cfg = configparser.ConfigParser()
#cfg.read('settings.cfg')

#url = 'mysql+pymysql://{0}:{1}@{2}/infbot_db?charset=utf8'.format(cfg['mysql']['user'], cfg['mysql']['password'], cfg['mysql']['host'])
#print(url)
#ngine = sa.create_engine(url, echo=True)

#engine.execute('DROP TABLE dmoz')
#if not engine.dialect.has_table(engine, 'dmoz'):
#    engine.execute('CREATE TABLE dmoz (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, title VARCHAR(1000),link VARCHAR(1000),descr VARCHAR(1000),insertdate DATETIME)')
#if not engine.dialect.has_table(engine, 'dmoza'):
#    engine.execute('CREATE TABLE dmoza (id INT NOT NULL PRIMARY KEY, title VARCHAR(5000), link VARCHAR(5000))')

class DmozSpiderSpider(scrapy.Spider):
    name = "dmoz_spider"
    allowed_domains = ["dmoz.com"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    ]

    custom_settings = {
        "DOWNLOAD_DELAY": 0.5, #0.5秒ごとにクロール
    }

    def parse(self, response):
        i = 0
        for sel in response.xpath("//div[@class='title-and-desc']"):
            title = sel.xpath("a/div[@class='site-title']/text()").extract()
            link = sel.xpath('a/@href').extract()
            descr = sel.xpath("/div[@class='site-descr ']/text()").extract()
            print("================================")
            print (title, link, descr)
            # SQL文に「?」が使用できないので、代わりに「%s」を使用
            dmoz.insert().execute(title=title, link=link)
            #ins = "INSERT INTO dmoz (title,link) VALUES (%s, %s)"
            #engine.execute(ins, title, link)
            #i += 1;
            #ins = "INSERT INTO dmoz (id,title,link) VALUES (%s, %s, %s)"
            #engine.execute(ins, i,title, link)
            #i += 1;
            #rows = engine.execute('SELECT * FROM dmoza')
            #for row in rows:
            #    print(row)
