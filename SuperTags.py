#! -*- coding:utf-8 -*-
from burp import IBurpExtender
from burp import IHttpListener
from burp import IHttpRequestResponse
from burp import IResponseInfo
import sys  
import re


reload(sys)  
sys.setdefaultencoding('utf8')

class BurpExtender(IBurpExtender,IHttpListener):
    
    def registerExtenderCallbacks(self,callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._pattern = r'<[i|b|a|s|f|l|p|m|e|o|d|v].*?>'
        self._callbacks.setExtensionName("SuperTags")

        print "Load SuperTags plugin success"
        print "Created by Hpdoger"
        print "Blog: Hpdoger.me"
        print "============================================="
        print ""

        self._callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if toolFlag == 4 or toolFlag == 8:
            if not messageIsRequest:
                # 获得请求体
                request = messageInfo.getRequest()
                analyzedRequest = self._helpers.analyzeRequest(request) # 用来获取请求头一类的对象
                analyzedRequest2 = self._helpers.analyzeRequest(messageInfo) # 用来获取url的对象   
                # reqHeaders = analyzedRequest.getHeaders()                
                reqParaList = analyzedRequest.getParameters()
                reqUrl = analyzedRequest2.getUrl()
                Allparams = {}

                for para in reqParaList:
                    if para.getType() != para.PARAM_COOKIE:
                        Allparams[para.getName()] = para.getValue()
                          
                # 获得响应体
                response = messageInfo.getResponse() # get response
                analyzedResponse = self._helpers.analyzeResponse(response)
                body = response[analyzedResponse.getBodyOffset():]
                response_body = body.tostring() # get response_body
                # print response_body

                tags = re.findall(self._pattern,response_body.encode('utf-8'))
                # print tags
                self.ChecktheSame(Allparams,tags,reqUrl)

                    


    def ChecktheSame(self,Allparams,tags,reqUrl):

        for param_key in Allparams:
            if Allparams[param_key]:
                for tag in tags:                                                    
                    if tag.find(Allparams[param_key]) != -1:
                        print "Found Available tag %s" % (tag)
                        print "Variable param is \"%s\" and the Vulnerable url is :   %s\n" % (param_key,reqUrl)
                    else:
                        continue
