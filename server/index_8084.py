import tornado.ioloop
import tornado.web
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world 8084")
 
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/index.py", MainHandler),
])
 
if __name__ == "__main__":
    application.listen(8084)
    tornado.ioloop.IOLoop.instance().start()
