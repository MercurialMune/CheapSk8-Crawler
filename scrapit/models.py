from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem


class OlxWebsite(models.Model):
    name = models.TextField()
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class PigiaWebsite(models.Model):
    name = models.TextField()
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class PigiaPhone(models.Model):
    name = models.TextField()
    price = models.TextField()
    link = models.URLField()
    image = models.TextField(null=True)
    phone_site = models.ForeignKey(PigiaWebsite)
    url = models.URLField()
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class OlxPhone(models.Model):
    name = models.TextField()
    price = models.TextField()
    link = models.URLField()
    image = models.TextField(null=True)
    phone_site = models.ForeignKey(OlxWebsite)
    url = models.URLField()
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class PigiaPhoneItem(DjangoItem):
    django_model = PigiaPhone


class OlxPhoneItem(DjangoItem):
    django_model = OlxPhone




