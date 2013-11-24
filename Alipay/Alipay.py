#coding=utf-8
import site_helper, web, page_helper
from tool import alipay

class Alipay:

    def GET(self):
        alipayTool=alipay()
        params={  
            '_input_charset':'utf-8',
            "body":"测试",
            'logistics_fee':'0',
            'logistics_payment':'SELLER_PAY',
            'logistics_type':'EXPRESS',
            "notify_url":"http://xxxx.com/return",
            "out_trade_no":"...",
            "partner":"...",
            "payment_type":"1",
            'price':'0.1',
            'quantity':'1',
            'receive_address':'无需收货地址',
            'receive_mobile':'...',
            'receive_name':'无需收货人',
            'receive_phone':'...',
            'receive_zip':'100000',
            "return_url":"http://xxx.com/return", 
            "seller_id":"...",
            "service":"trade_create_by_buyer",
            "show_url":"http://xxxxx.com/pay",
            "subject":"测试",
            "sign":"xxxxx",
            "sign_type":"MD5"
        }  
        payhtml=alipayTool.createPayForm(params) 
        return site_helper.page_nobase.Alipay(payhtml)
