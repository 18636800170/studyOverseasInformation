# -*- coding: utf-8 -*-

# Scrapy settings for qianmu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qianmu'

SPIDER_MODULES = ['qianmu.spiders']
NEWSPIDER_MODULE = 'qianmu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Cookie': "JSESSIONID=00C27E797D8A3864065ABAB75F2FB057; Hm_lvt_f409979f9c1034edcba2b24ea2b0a835=1515293049; Hm_lpvt_f409979f9c1034edcba2b24ea2b0a835=1515293049",
    'Host': "qianmu.iguye.com",
    # 'Referer': "https://www.baidu.com/link?url=jKi6jfI7Ax4ltr7obaFp6-2jZQYSVUb3OyP0MwbFFBy&wd=&eqid=f41abe2d0000864b000000025a518973",
    'Upgrade-Insecure-Requests': "1",
    # 'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'qianmu.middlewares.QianmuSpiderMiddleware': 543,
# }


HTTPPROXY_ENABLED = True
PROXIES = [
    # 'http://118.89.190.86:8888',
    # 'http://123.206.133.179:8888',
    # 'http://140.143.191.23:8888',
    'http://ms0108:ms0108@182.84.98.201:888',
    'http://ms0108:ms0108@117.41.187.112:888',
    'http://ms0108:ms0108@210.16.189.75:888',
    'http://ms0108:ms0108@1.82.230.108:888',
    'http://ms0108:ms0108@117.41.184.182:888',
    'http://ms0108:ms0108@222.73.48.188:888',
    'http://ms0108:ms0108@103.21.142.201:888',
]
PROXY_MAX_FAILED = 1

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'qianmu.middlewares.useragent.RandomUseragentMiddleware': 543,
    # 'qianmu.middlewares.proxy.RandomProxyMiddleware': 749,
    "scrapy.downloadermiddlewares.useragents.UserAgentMiddleware": None,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# 后面的数字是优先级,从小到大
ITEM_PIPELINES = {
    #  对数据进行初级处理
    # 'qianmu.pipelines.CheckPipeline': 300,
    #  mysql数据库处理
    # 'qianmu.pipelines.MysqlPipeline': 301,
    #  redis数据库处理
    # 'qianmu.pipelines.RedisPipeline': 301,
    # 开启redis分布式处理
    "scrapy_redis.pipelines.RedisPipeline":300,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 性能优化
# 线程池数量
# REACTOR_THREADPOOL_MAXSIZE=20
# 降低日志级别
# LOG_LEVEL="INFO"
# 禁用重试
# RETRY_ENABLED=False
# 禁用重定向
# REDIRECT_ENABLED=False
# 减少超时等待
# DOWNLOAD_TIMEOUT=20


# redis使用
SCHEDULER="scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS="scrapy_redis.dupefilter.RFPDupeFilter"
# REDIS_URL="redis://user:pass@hostname:6379"
SCHEDULER_PERSIST=True



