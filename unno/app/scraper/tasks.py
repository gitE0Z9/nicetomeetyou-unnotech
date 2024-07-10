from .spiders.udn_nba import UdnNbaSpider


def crawl_udn_nba(max_page: int = 10):
    spider = UdnNbaSpider(channel_id=2000, max_page=max_page)
    created_count = spider.run()

    return created_count
