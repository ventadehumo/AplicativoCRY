
from scrapy import FormRequest
from scrapy import Request
from scrapy.spiders import CrawlSpider
import xml.etree.cElementTree as ET
from time import gmtime, strftime
import os
import sys

class RequestNode:
    def __init__(self,
                 url,
                 callback=None,
                 method='GET',
                 headers=None,
                 body=None,
                 formdata=None,
                 cookies=None,
                 meta=None,
                 encoding='utf-8',
                 priority=0,
                 dont_filter=False,
                 errback=None,
                 idx=None,
                 data=None):
        self.url = url
        self.callback = callback
        self.method = method
        self.headers = headers
        self.body = body
        self.cookies = cookies
        self.meta = meta
        self.encoding = encoding
        self.priority = priority
        self.dont_filter = dont_filter
        self.errback = errback
        self.data = data
        self.previousNode = None
        self.nextNode = None
        self.idx = idx
        self.formdata = formdata

class Engine_Module(CrawlSpider):
    def __init__(self):
        super(Engine_Module, self).__init__()

        self.numNodes = 0
        self.actualNode = None
        self.lastExecutionNode = None
        self.tailNode = None

    def insertLastSER(self, requestNode):
        if self.tailNode is not None and self.actualNode is not None:
            requestNode.previousNode = self.tailNode
            self.tailNode.nextNode = requestNode
            self.tailNode = requestNode
            self.numNodes += 1
        else:
            self.tailNode = requestNode
            self.actualNode = requestNode
            self.numNodes += 1

    def insertNextActualSER(self, requestNode):
        if self.actualNode is not None:
            tmpNodePrev = self.actualNode.previousNode
            self.actualNode.previousNode = requestNode
            requestNode.nextNode = self.actualNode
            if tmpNodePrev is not None:
                tmpNodePrev.nextNode = requestNode
                requestNode.previousNode = tmpNodePrev
            else:
                if self.lastExecutionNode is not None:
                    self.lastExecutionNode.nextNode = requestNode
                    requestNode.previousNode = self.lastExecutionNode

            self.actualNode = requestNode
            self.numNodes += 1
        else:
            if self.lastExecutionNode is not None:
                self.lastExecutionNode.nextNode = requestNode
                requestNode.previousNode = self.lastExecutionNode

            self.tailNode = requestNode
            self.actualNode = requestNode
            self.numNodes += 1

    def insertNextActualListNodesSER(self, listNodes):
        for node in reversed(listNodes):
            self.insertNextActualSER(requestNode=node)

    def insertNextLastListNodesSER(self, listNodes):
        for node in listNodes:
            self.insertLastSER(requestNode=node)

    def insertNextLastSameIdxSER(self, requestNode, idx):
        if idx is None:
            self.insertLastSER(requestNode=requestNode)
        else:
            req = self.actualNode
            compIndex = False
            while req is not None:
                if req.idx == idx:
                    compIndex = True
                if compIndex and req.idx != idx:
                    lastNode = req.previousNode
                    req.nextNode = req
                    req.previousNode = requestNode
                    lastNode.nextNode = requestNode
                    req = None
                    self.numNodes += 1
                else:
                    if req.nextNode is None:
                        self.insertLast(requestNode)
                        self.numNodes += 1
                    req = req.nextNode

    def getActualNodeToExecuteSER(self):
        return self.actualNode

    def executeNextSER(self):
        if self.actualNode is not None:
            self.numNodes -= 1
            nodeToExecute = self.actualNode
            self.lastExecutionNode = nodeToExecute
            self.actualNode = self.actualNode.nextNode
            if nodeToExecute.formdata is not None:
                yield FormRequest(
                    url=nodeToExecute.url,
                    encoding=nodeToExecute.encoding,
                    method=nodeToExecute.method,
                    headers=nodeToExecute.headers,
                    formdata=nodeToExecute.formdata,
                    cookies=nodeToExecute.cookies,
                    meta=nodeToExecute.meta,
                    dont_filter=nodeToExecute.dont_filter,
                    priority=nodeToExecute.priority,
                    callback=nodeToExecute.callback,
                    errback=nodeToExecute.errback
                )
            else:
                yield Request(
                    url=nodeToExecute.url,
                    encoding=nodeToExecute.encoding,
                    method=nodeToExecute.method,
                    headers=nodeToExecute.headers,
                    body=nodeToExecute.body,
                    cookies=nodeToExecute.cookies,
                    meta=nodeToExecute.meta,
                    dont_filter=nodeToExecute.dont_filter,
                    priority=nodeToExecute.priority,
                    callback=nodeToExecute.callback,
                    errback=nodeToExecute.errback
                )

    def executeNextWithAllSameIdxSER(self):
        if self.actualNode is not None:
            tmpIdx = self.actualNode.idx
            while tmpIdx is not None:
                self.numNodes -= 1
                nodeToExecute = self.actualNode
                self.lastExecutionNode = nodeToExecute
                self.actualNode = self.actualNode.nextNode
                if nodeToExecute.formdata is not None:
                    yield FormRequest(
                        url=nodeToExecute.url,
                        encoding=nodeToExecute.encoding,
                        method=nodeToExecute.method,
                        headers=nodeToExecute.headers,
                        formdata=nodeToExecute.formdata,
                        cookies=nodeToExecute.cookies,
                        meta=nodeToExecute.meta,
                        dont_filter=nodeToExecute.dont_filter,
                        priority=nodeToExecute.priority,
                        callback=nodeToExecute.callback,
                        errback=nodeToExecute.errback
                    )
                else:
                    yield Request(
                        url=nodeToExecute.url,
                        encoding=nodeToExecute.encoding,
                        method=nodeToExecute.method,
                        headers=nodeToExecute.headers,
                        body=nodeToExecute.body,
                        cookies=nodeToExecute.cookies,
                        meta=nodeToExecute.meta,
                        dont_filter=nodeToExecute.dont_filter,
                        priority=nodeToExecute.priority,
                        callback=nodeToExecute.callback,
                        errback=nodeToExecute.errback
                    )
                if self.actualNode is None or self.actualNode.idx != tmpIdx:
                    tmpIdx = None

    def getAllNextRequestSER(self):
        nodeList = []
        if self.actualNode is not None:
            node = self.actualNode
            while node is not None:
                nodeList.append([node.url])
                node = node.nextNode
            if node is not None:
                nodeList.append([node.url])
        return nodeList


    #########################################################
    #   Write Data Extract to XLM format (XLST)
    #########################################################

    def WriteNewsToXML(self, ListNews):
        NewsList = ET.Element("NewsList")
        DomainFrom = ET.SubElement(NewsList, "DomainFrom").text = ListNews.get('DomainFrom', None)

        # Creating xml name
        XML_Name = DomainFrom.split('.')
        XML_Name = XML_Name[1]

        dataTime = strftime("%Y-%m-%d %H-%M-%S", gmtime())
        dataTime = dataTime.replace(' ', '_')
        DataTime = ET.SubElement(NewsList, "DataTime").text = dataTime

        XML_Name = XML_Name + '_' + dataTime + '.xml'

        if sys.platform == 'win32':
            curdir = os.getcwd()
            xml_Path = curdir + "\\spiders\\News\\XML_Data\\" + XML_Name
        elif sys.platform == 'linux2':
            curdir = os.getcwd()
            xml_Path = curdir + "/spiders/News/XML_Data/" + XML_Name

        print "Writing news in path: " + xml_Path

        for new in ListNews.get('newsList', None):
            New = ET.SubElement(NewsList, "new")
            ET.SubElement(New, "tittle").text = new.get('tittle', None)
            ET.SubElement(New, "dataTime").text = new.get('dataTime', None)
            ET.SubElement(New, "url").text = new.get('url', None)

        tree = ET.ElementTree(NewsList)

        tree.write(xml_Path)