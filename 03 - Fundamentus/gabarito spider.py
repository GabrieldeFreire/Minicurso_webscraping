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
        links_xpath = '//tbody//tr/td/a/@href'
        paper_xpath = response.xpath(links_xpath).getall()
        paper_list = [papel_.strip() for papel_ in paper_xpath]
        yield from response.follow_all(paper_list[:1], callback=self.get_paper_info)

    def get_paper_info(self, response):
        table_xpath = '//table'
        paper=response.url.split('=')[-1]
        table = response.xpath(table_xpath)[0]
        line_xpath = './/tr//text()'
        lines_info = table.xpath(line_xpath).getall()
        lines_info = [item for item in lines_info if item not in ['\n', '?']]
        line_info_dict = {}

        if len(lines_info) == 20:
            for index in range(0, len(lines_info), 2):
                line_info_dict[lines_info[index]] = lines_info[index+1]
            self.logger.info(f'Salvando papel: {paper}')
            yield line_info_dict
