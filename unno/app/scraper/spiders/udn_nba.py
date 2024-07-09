from typing import Generator

import requests
from news.constants import SourceWebsites
from news.models import News
from pyquery import PyQuery


class UdnNbaSpider:
    def __init__(self, channel_id: int = 2000, max_page: int = 10):
        self.channel_id = channel_id
        self.max_page = max_page
        self.url_template = "https://tw-nba.udn.com/api/more?channel_id={channel_id}&type=index&page={page}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        }

    def run(self):
        for page in range(1, self.max_page + 1, 1):
            url = self.get_url(page)
            response = self.get(url)

            for link in self.parse_link(response):
                page_response = self.get(link)
                data = self.parse(page_response)
                self.show(data)
                self.save(data)

    def get(self, url: str) -> str:
        response = requests.get(
            url,
            headers=self.headers,
        )

        if response.status_code == 200:
            return response.text
        else:
            print(response.text)
            return ""

    def get_url(self, page: int) -> str:
        return self.url_template.format(channel_id=self.channel_id, page=page)

    def parse_link(self, body: str) -> Generator[str, None, None]:
        if not body:
            return

        dom = PyQuery(body)

        for item in dom("dt a").items():
            yield item.attr("href")

    def parse(self, body: str) -> dict:
        if not body:
            return {}

        dom = PyQuery(body)

        return dict(
            uid=None,
            title=dom("h1.story_art_title").text(),
            img=dom("figure.photo-story img").attr("src"),
            content=dom("#story_body_content span p").remove("figure").text().strip(),
            source=SourceWebsites.UDN_NBA,
            source_url=dom('meta[property="og:url"]').attr("content"),
            post_time=dom('meta[name="pubdate"]').attr("content"),
        )

    def show(self, data: dict):
        print(data)

    def save(self, data: dict):
        News.objects.update_or_create(**data)
