import webbrowser
from terminaltables import AsciiTable
import urllib
commandlist=['list','start','auto','update']

def list():
    with open('config/modules.txt','r') as modlist:
        table_data = [
            ['', 'Modules',''],
            ]
        modules=modlist.readlines()
        for module in modules:
            table_data.append(["",module.strip(),""])
        table = AsciiTable(table_data)
        print(table.table)


def start(module):
    print(f"\rstarting {module}")

def handle(commands):
    command=commands[0]
    if command in commandlist:
        if command=="list":
            list()
        elif command==('start'):
            module=commands[1]
            try:
                target=commands[2]
            except:
                pass
            print(f"starting {module}")
            if module=='unscan':
                import modules.unscan.main as unscan
                unscan.main()
            if module=='instastalk':
                import modules.InstaStalk.main as main
                main(username=target)
            if module=='eyespy':
                import modules.eyespy.main as main
                main
            if module=='phonelooker':
                import modules.phonelooker.main as main
                main
            if module=='only4dorks':
                import modules.only4dorks.main as main
                main
            if module=='pimeyes':
                webbrowser.open("https://www.pimeyes.com/")
            if module=='PlateUp':
                import modules.PlateUp.main as main
                main
    else:
        print(f"\rnot a command")