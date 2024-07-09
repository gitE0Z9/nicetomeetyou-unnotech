from .spiders.udn_nba import UdnNbaSpider


def crawl_udn_nba_task(max_page: int = 10):
    spider = UdnNbaSpider(channel_id=2000, max_page=max_page)
    spider.run()
