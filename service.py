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

#from tornado import ioloop
define("port", default=8001, help="run on the given port", type=int)

class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html",
                    title="test",
                    blog_name="cocal",                    
                    )
class HomeHandler(tornado.web.RequestHandler):
    titlelist = manager.titleManager()
    def get(self):
        self.render("homepage.html",
                    title="test",
                    articlesList = self.titlelist,
                    blog_name="cocal",                    
                    )
        
class GetPostsHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('postname')
        if name == None:
            self.write('err')
        else:
            content = manager.getPostHtml(name)
            self.render("post3.html",
                        content = content
                        )
            
            
class RefreshTitlesHandler(HomeHandler):
    pass

    
    
                
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/",HomeHandler),
                    (r"/tis",GetPostsHandler),
                    (r"/resh",RefreshTitlesHandler),
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
