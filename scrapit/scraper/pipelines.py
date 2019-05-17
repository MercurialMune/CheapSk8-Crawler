import logging
from django.db.utils import IntegrityError
from scrapy.exceptions import DropItem


class DjangoWriterPipeline(object):

    def process_item(self, item, spider):
        if spider.conf['DO_ACTION']:
            try:
                item['phone_site'] = spider.ref_object

                item.save()
                spider.action_successful = True
                dds_id_str = str(item._dds_item_page) + '-' + str(item._dds_item_id)
                spider.struct_log("{cs}Item {id} saved to Django DB.{ce}".format(
                    id=dds_id_str,
                    cs=spider.bcolors['OK'],
                    ce=spider.bcolors['ENDC']))

            except IntegrityError as e:
                spider.log(str(e), logging.ERROR)
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")
        else:
            if not item.is_valid():
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")

        return item
