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
import manager

import msgNote
#from tornado import ioloop
define("port", default=8001, help="run on the given port", type=int)

class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html",
                    title="test",
                    blog_name="cocal",                    
                    )
class HomeHandler(tornado.web.RequestHandler):
#     titlelist = manager.titleManager()
    def get(self):
        self.render("homepage.html",
                    title="cocal's blog",
                    articlesList = manager.titleManager(),
                    blog_name="cocal",                    
                    )
        
class GetPostsHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('postname')
        if name == None:
            self.write('err')
        else:
            content = manager.getPostHtml(name)
            self.render("post4.html",
                        content = content
                        )
class initAPost(tornado.web.RequestHandler):
    def get(self):
        filename = self.get_argument('cr_name',None)
        filename = manager.initAPost(filename)
        manager.initTitleManager()
        content = manager.getPostHtml(filename+'.md')
        self.render("post3.html",
                     content = content
                        )
            
class RefreshTitlesHandler(tornado.web.RequestHandler):
    def get(self):
        manager.initTitleManager()
        self.render("homepage.html",
                    title="test",
                    articlesList = manager.titleManager(),
                    blog_name="cocal",                    
                    )
    
class testNewPage(tornado.web.RequestHandler): 
    def get(self):
        self.render('newtheme\index.html')   
class getMsg(tornado.web.RedirectHandler):
    def get(self):
        pass
    
class getMsgHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/msg" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
#         self.set_header("Content-Type", "text/plain")
        self.write('{% extends "msgNote.html" %}'
                   "You wrote " + self.get_argument("message"))    
                    
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/",HomeHandler),
                    (r"/tis",GetPostsHandler),
                    (r"/resh",RefreshTitlesHandler),
                    (r"/cre",initAPost),
                    (r"/t",testNewPage),
                    (r"/msg",getMsgHandle),
                    ]
        settings = dict(
            static_path = os.path.join(os.path.dirname(__file__), "static"),
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
