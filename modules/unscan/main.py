import json
import requests
from termcolor import colored
from termcolor import cprint
import time
import os
from multiprocessing.pool import ThreadPool as Pool


def scan(target):
    #loading site urls into the tool
    sites=[]
    with open('modules/unscan/data.json',"r") as f:
        data = json.load(f)
        for url in data:
            key=data[url]
            site=(key['url'])
            sites.append(site)

#making the request to the profile/site.
    def get(site,target):
        url=site.format(target)
        resp=requests.get(url)
        code=resp.status_code
        #chcking if exists logic
        if code==200:
            symbol=colored(f"[+]","green")
            url=colored(url,"blue")
            print(symbol,url)
        else:
            pass

    # pool for asyncronous exectution        
    pool_size = 500
    pool = Pool(pool_size)
    start=time.time()
    for site in sites:
        pool.apply_async(get, (site,target))
    pool.close()
    pool.join()

    print(f"scanned {len(sites)} sites")

def main():
    while True:
        global target
        #getting target username
        target=input("Enter username to check: ")
        if target is None:
            continue
        else:
            print(" ")
            start=f"""
                -----------------------------------------------------------
                |                                                         |
                |               username scanner                          |
                |                                                         |
                |                                                         |
                |                                                         |
                |            target: {target}                             |
                -----------------------------------------------------------"""
            print(start)
            print(" ")
            scan(target)