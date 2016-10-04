# Why?
I found a icon resource site which can help on PPT. But there are too many icons that can't be download manually. So I'd like to use a downloader tool to do the task. After googling a while, I see the best way to do this is to creat a bot using Scrapy.
# install scrapy
* Install python 2.7.12 on Windows 10
* Install python win32 API extension
* Install lxml wheel http://www.lfd.uci.edu/~gohlke/pythonlibs/
* Install Pillow
# test
run the interactive shell.
>scrapy shell http://icooon-mono.com/category/event-en/?lang=en
>response.xpath('//div[@id="topMaincolumn"]/ul/li/a/img/@src').extract()
# resource spider
1. follow the tutorial to create a project
2. create item in parse() to provide item with image_urls
3. define item class
4. enable pipeline inherits from ImagePipeline
5. create the pipeline to rename the images
