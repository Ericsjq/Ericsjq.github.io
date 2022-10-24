"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
#接口：http://192.168.31.234:8586/
class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 页面模板
    pa = open('h.html','r',encoding='gbk')
    

    Page = pa.read()
    pa.close()
    # 处理一个GET请求
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(json.dumps(self.Page).encode('ASCII'))#.encode('utf-8'))

if __name__ == '__main__':
    serverAddress = ('0.0.0.0', 8586)
    server = HTTPServer(serverAddress, RequestHandler)
    print('服务器启动。')
    server.serve_forever()
"""
"""
# api接口
# -*- coding: utf-8 -*-
# @time    : 2022/6/20
# @author  : Eric
# @function: get service of fastapi
# 公网IP：111.201.248.167  # 111.201.254.195
# 接口调用：http://192.168.31.234:5862/api_v5/apikey=6131&token=kf1&inp=你好
# 接口名称：http://192.168.31.234:5862/api_v5/apikey=【your_apikey】&token=【your_token】&inp=【your_news】
li = [6131,2022,2019]
li2= ['kf1','xn2','jn9']
from fastapi import FastAPI
#import ues_train as ai
import time
print(1)
app = FastAPI()
print(11)
@app.get('/api_v5/apikey={a}&token={t}&inp={b}')
def calculate(a: str=None, b: str=None, t:str=None):
    try:
        #c = a + b
        print(a,b,t)
        if int(str(a)) in li and li2[li.index(int(a))] == str(t):
            o = open('h.html')
            res = o#{"text":ai.aihf(str(b)),"time":time.time()}
            o.close()
        else:
            res = {"text":"token Error","time":time.time(),"Error":'token_not_found'}
        
    except:
        res = {"text":"Server Error","time":time.time(),"Error":'Internal Server Error'}
    return res

if __name__ == '__main__':
    import uvicorn
    print('服务器启动。')
    uvicorn.run(app=app,
                host="0.0.0.0",#"192.168.31.234",0.0.0.0
                port=5865,#8586,5862
                workers=1)
"""
import sea
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")
def c():
	#return render_template("inde.html")# 这个以后细讲
        with open('inde.html','r',encoding='utf-8') as f:
            n = f.read()
        return n

@app.route("/sea/<aa>/")
def d(aa):
        
        #return rouder_template("xxx.html")
        l = sea.find(aa,len_=50)
        s = ''
        for i in l:
            s += '|'.join(i) + '\n'
        return str(s)#"666"
        """
        with open('inde.html','r',encoding='utf-8') as f:
            n = f.read()
        return n
        """

app.run(host='0.0.0.0')
