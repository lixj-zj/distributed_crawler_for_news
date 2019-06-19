# -*- coding: utf-8 -*-

# Scrapy settings for main_node project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from main_node.com_config import user_agent

BOT_NAME = 'main_node'

SPIDER_MODULES = ['main_node.spiders']
NEWSPIDER_MODULE = 'main_node.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 '

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
# }
DEFAULT_REQUEST_HEADERS = user_agent.UserAgent().get_headers()

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'main_node.middlewares.MainNodeSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'main_node.middlewares.MainNodeDownloaderMiddleware': 543,
   #  'main_node.middlewares.MainNodeProxyMiddleware': 100,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'main_node.pipelines.MainNodePipeline': 300,
    'main_node.pipelines.mongodb.SingleMongodbPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'






# #scrapy-redis配置
# # 过滤器
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# # 调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# # 调度状态持久化
# SCHEDULER_PERSIST = True
# # 请求调度使用优先队列
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# # redis 使用的端口和地址
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
#
# ##增加全局并发数的一些配置:
# # 默认 Item 并发数：100
# CONCURRENT_ITEMS = 100
# # 默认 Request 并发数：16
# CONCURRENT_REQUESTS = 16
# # 默认每个域名的并发数：8
# CONCURRENT_REQUESTS_PER_DOMAIN = 8
# # 每个IP的最大并发数：0表示忽略
# CONCURRENT_REQUESTS_PER_IP = 0
#
# ##缓存，scrapy默认已经自带了缓存，配置如下
# # 打开缓存
# HTTPCACHE_ENABLED = True
# # 设置缓存过期时间（单位：秒）
# # HTTPCACHE_EXPIRATION_SECS = 0
# # 缓存路径(默认为：.scrapy/httpcache)
# HTTPCACHE_DIR = 'httpcache'
# # 忽略的状态码
# HTTPCACHE_IGNORE_HTTP_CODES = []
# # 缓存模式(文件缓存)
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'




# MONGODB_URI = 'mongodb://192.168.131.24:27017'
# MONGODB_DATABASE = 'demo'
# MONGODB_COLLECTION = 'scio'


# 日志文件         # (最好为爬虫名称，例如：qiushi.log)
# LOG_FILE = 'scrapy.log'
LOG_FILE = "logs/scrapy.log"

# 日志等级
LOG_LEVEL = 'INFO'

# 是否启用日志（创建日志后，不需开启，进行配置）
LOG_ENABLED = False  # （默认为True，启用日志）

# 日志编码
LOG_ENCODING = 'utf-8'

# 如果是True ，进程当中，所有标准输出（包括错误）将会被重定向到log中
# 例如：在爬虫代码中的 print（）
LOG_STDOUT = False  # (默认为False)
