import webbrowser
from termcolor import colored

query1=input("Enter the query: ")
query2=input("Enter the query (leave blank to skip): ")
query3=input("Enter the query (leave blank to skip): ")
query4=input("Enter the query (leave blank to skip): ")
query5=input("Enter the query (leave blank to skip): ")

def query(q1="", q2="", q3="", q4="",q5=""):
    """
    This function takes 4 arguments and returns a string with the query.
    """
    baseurl="https://www.google.com/search?q="
    if q1 != "":
        query = baseurl+q1.replace(":","%3A")

    if q2 != "":
        query = query + "+" + q2.replace(":","%3A")
    
    if q3 != "":
        query = query + "+" + q3.replace(":","%3A")
    
    if q4 != "":
        query = query + "+" + q4.replace(":","%3A")
    
    if q5 != "":
        query = query + "+" + q5.replace(":","%3A")
    
    print(colored("{+}","blue")+colored("Opening Google search for: ", "green")+query)
    webbrowser.open(query)

query(query1, query2, query3, query4, query5)