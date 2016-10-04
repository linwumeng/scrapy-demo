# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os.path
from scrapy.pipelines.images import ImagesPipeline

class TutorialPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        print "e:/workspace/scrapy/event/" + image_paths[0]
        print "e:/workspace/scrapy/event/full/" + item['title'][0] + '.jpg'
        os.rename("e:/workspace/scrapy/event/" + image_paths[0], "e:/workspace/scrapy/event/full/" + item['title'][0] + '.jpg')
        # os.remove("e:/workspace/scrapy/business/" + image_paths[0])
        return item
