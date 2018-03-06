import logging

import pymysql
import redis
from scrapy.exceptions import DropItem

logger = logging.getLogger(__name__)


class CheckPipeline(object):
    def process_item(self, item, spider):
        if not item["undergraduate_num"] or not item["postgraduate_num"]:
            raise DropItem("Missing field is %s" % item)
        return item


class RedisPipeline(object):
    def __init__(self):
        self.r = redis.Redis(password=111111, db=1)
        # self.r=redis.StrictRedis(host=)

    def process_item(self, item, spider):
        self.r.sadd(spider.name, item["name"])
        logger.info("redis:add %s to %s" % (item["name"], spider.name))
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="root",
            charset="utf8",
            db="qianmu",
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        # zip(*)进行反解析
        cols, values = zip(*item.items())
        sql = "insert into `universities`(%s) VALUES (%s);" % (",".join(cols), (("%s," * len(cols))[:-1]))
        self.cursor.execute(sql, values)
        self.conn.commit()
        logger.info(self.cursor._last_executed)
        return item
