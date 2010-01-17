# (c) 2010 Joseph Adams
# Information see: http://github.com/Jcla/jcla-helloworld



from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class InputformHandler(webapp.RequestHandler):
  
  def get(self):
    self.response.out.write("""
    <form method='POST' action='/message'>
      <input type='text' name='msg' />
      <input type='submit' value='submit'  />
    </form>
    """)
class MainHandler(webapp.RequestHandler):

  def get(self, pattern):
    self.response.out.write('Hello world!')
  #  self.response.out.write(pattern)
    
  def post(self, pattern):
    m = self.request.get('msg')
    self.response.out.write('You posted the message %s' % (m))

def main():
  application = webapp.WSGIApplication([
  ('/inputform', InputformHandler), 
  ('/(.*)', MainHandler),
  ],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
