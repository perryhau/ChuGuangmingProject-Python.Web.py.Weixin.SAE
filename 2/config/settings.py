#!/usr/bin/env python
# coding: utf-8
import web
import sae.const
#数据库设定
db = web.database(dbn='mysql', user=sae.const.MYSQL_USER, pw=sae.const.MYSQL_PASS, host=sae.const.MYSQL_HOST, port=3307,
                  db=sae.const.MYSQL_DB)
#TOKEN 到微信公众平台自己设置
config = {"TOKEN": 'chu888chu888'}
#发送文本信息
textMessage = '''
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
            </xml>
            '''


