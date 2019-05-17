from dynamic_scraper.spiders.django_spider import DjangoSpider
from scrapit.models import *


class PigiaSpider(DjangoSpider):

    name = 'pigia_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(PigiaWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = PigiaPhone
        self.scraped_obj_item_class = PigiaPhoneItem
        super(PigiaSpider, self).__init__(self, *args, **kwargs)


class OlxSpider(DjangoSpider):

    name = 'olx_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(OlxWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = OlxPhone
        self.scraped_obj_item_class = OlxPhoneItem
        super(OlxSpider, self).__init__(self, *args, **kwargs)
