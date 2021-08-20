# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class BookScrapePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        return [Request(x, meta={'bookname': item.get('book_name')}) for x in item.get(self.images_urls_field, [])]
    
    def file_path(self, request, response=None, info=None):
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) method ar deprecated, '
            'please use file_path(request, response=None, info=None) instead',
            category=ScrapyDeprecationWarning, stacklevel=1)
        
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        
        file_name = request.meta['bookname'].replace(':', '')
        return 'full/%s.jpg' % (file_name)

