import scrapy
import re
import time

# executar: scrapy runspider spider.py -o output.csv
class fundamentus(scrapy.Spider):
        
    name = 'fundamentus_NF'

    custom_settings = {
        'DOWNLOAD_TIMEOUT': 100,
        'HTTPCACHE_ENABLED': 1,
        'LOGSTATS_INTERVAL': 1,
        'LOG_LEVEL': 'DEBUG',
        # 'DOWNLOAD_DELAY': 0,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }

    def start_requests(self):
        self.logger.info('Iniciando spyder')
        self.count = 0
        yield scrapy.Request(
        url = 'http://fundamentus.com.br/detalhes.php?papel=',
            callback = self.get_all_papers
        )

    def get_all_papers(self, response):
        pass

    def get_paper_info(self, response):
        pass
