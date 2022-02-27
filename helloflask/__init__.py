from flask import Flask,g,make_response,Response

app = Flask(__name__)
#__name__ : 어플리케이션이름이 들어감
app.debug =True

@app.route('/res1')
def res1():
  custom_res = Response("Custom Response",200,{'test':'ttt'})
  return make_response(custom_res)

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