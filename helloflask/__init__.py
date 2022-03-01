from email import header
from flask import Flask,g,make_response,Response, request
from datetime import date, datetime

app = Flask(__name__)
#__name__ : 어플리케이션이름이 들어감
app.debug =True

@app.route('/res1')
def res1():
  custom_res = Response("Custom Response",200,{'test':'ttt'})
  return make_response(custom_res)

#1)다음 형태로 요청했을때 해당 key로 Cookie를 굽는 코드를 작성하시오.
#http://localhost:5000/wc?key=token&val=abc
@app.route('/wc')
def wc():
  key = request.args.get('key')
  val = request.args.get('val')
  res = Response("SET COOKIE")
  res.set_cookie(key,val)
  return make_response(res)

#2) 다음과 같이 요청했을때 해당 key의 Cookie Value를 출력하는 코드 작성하시오. 
#http://localhost:5000/rc?key=token

# def ymd(fmt):
#   def trans(date_str):
#     return datetime.strptime(date_str,fmt)
#   return trans


# @app.route('/dt')
# def dt():
#   datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
#   return '우리나라 시간 형식:' + str(datestr)

#WSGI 
@app.route('/test_wsgi')
def wsgi_test():
  def application(environ, start_response):
      body = 'The request method was %s' % environ['REQUEST_METHOD']
      headers = [('Content-Type', 'text/plain'),('Content-Length',str(len(body)))]
      start_response('200 OK',headers)
      return [body]
    
  return make_response(application)


#request 요청이 들어오기 전에 실행해줘 -> 어떤 요청이 들어와도 실행 됨
# @app.before_request
# def before_request():
#   print("before_request")
#   g.str = '한글'  

# @app.route("/gg")
# def helloworld2():
#   return "Hello World!" + getattr(g,'str','111')

@app.route("/")
def helloworld():
  return "Hello Flask World!"


