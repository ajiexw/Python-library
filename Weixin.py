#!/bin/env python
#coding: utf-8
import os
import hashlib
import sae
import web
from lxml import etree

config={"TOKEN":'pyweinxintest',
	"WEIXIN": 'weixin'}
        
urls = (
    '/weixin', 'weixin'
)

app_root = os.path.dirname(__file__)

class weixin:        
    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr

        token = config['TOKEN']
        
        tmplist = [ token, timestamp, nonce ]
        tmplist.sort()
        tmplist.sort()
        tmpstr = ''.join( tmplist )
        hashstr = hashlib.sha1( tmpstr ).hexdigest()

        if hashstr == signature:
            return echostr
        
        print signature,timestamp,nonce
        print tmpstr,hashstr
        return 'Error' + echostr


    def POST(self):
        data = web.data()
        root = etree.fromstring( data )
        child = list( root )
        recv = {}
        for i in child:
            recv[i.tag] = i.text

        #print data
        #print recv
        
        #测试demo，接受什么就返回什么
        textTpl = """<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[%s]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            <FuncFlag>0</FuncFlag>
            </xml>"""
        echostr = textTpl % (recv['FromUserName'], recv['ToUserName'],recv['CreateTime'],recv['MsgType'],recv['Content'])
        return echostr

app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)
