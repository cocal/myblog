# -*- coding: utf-8 -*-
'''
Created on 2014-6-14

@author: cocal
'''
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path

from tornado.options import define, options
#from tornado import ioloop
define("port", default=8001, help="run on the given port", type=int)

class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('test Done')
        self.render("test")
        print 'hehe'
            
class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        id=self.get_arguments('id')
        print('查询ID',id)
    
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/",SearchHandler),
                    (r"/de",DetailHandler),
                    ]
#        conn = pymongo.Connection("127.0.0.1",27017)
#        self.db = conn['mytestdb']
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            debug=True,
        )
        tornado.web.Application.__init__(self,handlers,**settings)

def testTimer():
    print('I am still running')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    #tornado.ioloop.PeriodicCallback(testTimer,3000).start() #实现每3s 循环任务
    tornado.ioloop.IOLoop.instance().start()     
