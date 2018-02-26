from scrapy.crawler import CrawlerProcess
from spiders import cryptocurrency_spider
#from spiders.SendMail import sendEmail
#from spiders.SendMail import ReadNewsData
#from spiders.SendMail import WriteHTML
#from spiders.SendMail import DeleteXMLs
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(cryptocurrency_spider.CRYPTOCURRENCY_Spider)
    #yield runner.crawl(muyseguridad_monitoring.NEWS_MONITORING_muyseguridad)
    #yield runner.crawl(cuadernosSeguridad_monitoring.NEWS_MONITORING_cuadernosSeguridad)
    reactor.stop()

crawl()
reactor.run()  # the script will block here until the last crawl call is finished

'''
News_list = ReadNewsData.viewFiles()
DictionaryOfNews = ReadNewsData.XML_To_HTML(News_list)
html_body = WriteHTML.Write_HTL_News_Data(DictionaryOfNews)
sendEmail.Send_email(html_body)
DeleteXMLs.delete_xml()
'''