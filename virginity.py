from termcolor import colored
import time
import json
import os
def configure():
    with open('config/config.json','r+') as f:
        config = json.load(f)

    print(colored("creating loot directory","blue"))
    os.mkdir('loot')

    #serpaikey
    serpapikey=input(colored("Enter your serpapi key (leave blank to configure later): ","blue"))
    serpapikeycur=config['serpaikey']
    config['serpaikey']=serpapikey
    with open('config/config.json','w') as f:
        json.dump(config,f,indent=4,sort_keys=True)

    #youtube api key
    youtubeapikey=input(colored("Enter your youtube api key (leave blank to configure later): ","blue"))
    config['youtubeapikey']=youtubeapikey
    with open('config/config.json','w') as f:
        json.dump(config,f,indent=4,sort_keys=True)

    #imgurclientid
    imgurclientid=input(colored("Enter your imgur client id (leave blank to configure later): ","blue"))
    config['imgurclientid']=imgurclientid
    with open('config/config.json','w') as f:
        json.dump(config,f,indent=4,sort_keys=True)

    #imgursecret
    imgursecret=input(colored("Enter your imgur secret key (leave blank to configure later): ","blue"))
    config['imgursecret']=imgursecret
    with open('config/config.json','w') as f:
        json.dump(config,f,indent=4,sort_keys=True)

    #instagramusername
    instagramusername=input(colored("Enter your instagram username (leave blank to configure later): ","blue"))   
    config['instauser']=instagramusername
    with open('config/config.json','w') as f:
        json.dump(config,f,indent=4,sort_keys=True)
    
    #instagrampassword
    instagrampassword=input(colored("Enter your instagram password (leave blank to configure later): ","blue"))
    config['instapass']=instagrampassword
    with open('config/config.json','w') as f:
        json.dump(config,f,indent=4,sort_keys=True)

    #setting setup flag to true
    config['setup']=True
    with open('config/config.json','w') as f:
        json.dump(config,f,indent=4,sort_keys=True)
    
    print(colored("Configuration complete!","blue"))
    time.sleep(1)
    print(colored("Starting...","green"))
    time.sleep(1)
    import main
    main.main()

def main():
    with open('config/config.json','r+') as f:
        config = json.load(f)

    print(colored("                                          WARNING","red"))
    print(colored("""
    Due to externally downloaded tools such as harvester and osintgram needing access to api keys or credentials
    please only download the official version of this tool from my own github https://github.com/theunsocialengineer 
    and make sure this tool is only pulling the external tools from their respective githubs to prevent any kind of 
    damage to your accounts as cloned copies could be trying to access or steal those credentials.

    ""","blue"))

    time.sleep(3)
    print(f"{colored('                                        DISCLAIMER','green')}")
    print(f"""{colored('''
    This tool has been built in an educational capacity to teach people osint analysis techniques used by professionals 
    in the field of security and digital forensics. This tool has also been developed for practicing cyber security researchers, 
    law enforcement aagencies , and other professional agents for use in their respective fields. This tool is not intended to be 
    used for malicious purposes or for any other purpose other than the intended use and i do not accept any responsibility 
    for any damage caused by using this tool.
    ''','blue')}""")

    accept=input(colored("Do you accept the disclaimer? (y/n) ","red"))

    if accept == "y":
        configure()
        
    #extis the program if disclaimer is not accepted
    else:
        print(colored("Exiting...","red"))
        time.sleep(1)
        exit()

main()