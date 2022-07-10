from terminaltables import AsciiTable
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import urllib
import webbrowser

def usa():
    plate=input("enter plate number: ")
    state=input("please enter the abbreviated 2 letter statecode: ")
    url = 'https://www.faxvin.com/license-plate-lookup/result?plate={}&state={}'.format(plate,state)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.find_all("div", {"class": "error"}):
        print(soup.prettify())
        print(colored("We couldn't find records for that plate. Please check and try again.","red"))
    elif soup.find_all("div", {"class": "details"}):
        try:
            table = soup.find('table', attrs={'class': 'tableinfo'})
            cells = table.findAll("td")
        except:
            print(colored("an error has occured.","red"))
        symbol=f"[{colored('+', 'green')}]"
        print("plate data found")
        vin = cells[0].b.text
        make = cells[1].b.text
        model = cells[2].b.text
        year = cells[3].b.text
        trim = cells[4].b.text
        style = cells[5].b.text
        engine = cells[6].b.text
        plant = cells[7].b.text
        age = cells[8].b.text
        print(f"{symbol} Vin: {vin}")
        print(f"{symbol} Make: {make}")
        print(f"{symbol} Model: {model}")
        print(f"{symbol} Year: {year}")
        print(f"{symbol} Trim: {trim}")
        print(f"{symbol} Style: {style}")
        print(f"{symbol} Engine: {engine}")
        print(f"{symbol} Plant: {plant}")
        print(f"{symbol} Age: {age}")

def uk():
    plate=input("enter numberplate: ")
    url="https://www.checkcardetails.co.uk/cardetails/{}".format(plate)
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.find_all("div", {"class": "no-reg-found"}):
        print(colored("We couldn't find records for that plate. Please check and try again.","red"))
    elif soup.find_all("div", {"id": "content"}):
        try:
            table = soup.find('table', attrs={'class': 'table'})
            cells = table.findAll("td")
        except Exception as e:
            print(e)
            print(colored("an error has occured.","red"))
        symbol=f"[{colored('+', 'green')}]"
        print("plate data found")
        endstr=""""""
        model_varient=cells[1].text
        model_description=cells[3].text
        primary_colour=cells[5].text
        fuel_type=cells[7].text
        engine=cells[9].text
        engine_litres=cells[11].text
        year_of_manufacture=cells[13].text
        euro_status=cells[15].text
        transmission=cells[17].text
        vehicle_age=cells[19].text
        registration_place=cells[21].text
        registration_date=cells[23].text
        keeper_start_date=cells[25].text
        last_v5c_issue_date=cells[27].text
        type_approval_date=cells[29].text
        wheel_plan=cells[31].text
        print(f"{symbol} Model Varient: {model_varient}")
        print(f"{symbol} Model Description: {model_description}")
        print(f"{symbol} Primary Colour: {primary_colour}")
        print(f"{symbol} Fuel Type: {fuel_type}")
        print(f"{symbol} Engine: {engine}")
        print(f"{symbol} Engine Litres: {engine_litres}")
        print(f"{symbol} Year of Manufacture: {year_of_manufacture}")
        print(f"{symbol} Euro Status: {euro_status}")
        print(f"{symbol} Transmission: {transmission}")
        print(f"{symbol} Vehicle Age: {vehicle_age}")
        print(f"{symbol} Registration Place: {registration_place}")
        print(f"{symbol} Registration Date: {registration_date}")
        print(f"{symbol} Keeper Start Date: {keeper_start_date}")
        print(f"{symbol} Last V5C Issue Date: {last_v5c_issue_date}")
        print(f"{symbol} Type Approval Date: {type_approval_date}")
        print(f"{symbol} Wheel Plan: {wheel_plan}")

def india():
    print("this is the best site for RTO lookups but since it uses a captcha best i can do is open the page for ya")
    webbrowser.open("https://vahaninfos.com/vehicle-details-by-number-plate")
    
def main():
    print((("""
@@#P5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555P#@@
@P:                                                                                                                                                :P@
@?            ?PPPPPPPPPP57.   JPPP^                .YPPP~       JPPPPPPPPPPPPP:  JPPPPPPPPPPPPP:        JPPP^     JPPP^  JPPPPPPPPPP57.            ?@
@?            P@@@@@@@@@@@@B:  G@@@~                !@@@@G       G@@@@@@@@@@@@@^  B@@@@@@@@@@@@@^        G@@@~     G@@@~  G@@@@@@@@@@@@B.           ?@
@?            P@@@7:^^^^5G&@~  YBGG^               .P#GGGG^      :^^^^5BGG!^^^^.  YBB&!^^^^^^^^^.        G@&B^     P@@@~  5@@@!^^^^^PBBG:           ?@
@? .....  ..  P@@@~     !PY&!  5&BJ: ....  ....... ^YG&&&#? .....     P&##^     . P#GY.         .  ..... GGYG^ ..  P@@@~  7B@@^     5&#G: ..  ....  ?@
@? ...... ... P@@@5?JJ7~G@P5~..G@&J:..... .........PYPGG&&&~........ .P&&#^.. ....B@@#~!J7~7?^... .......YJB@~.... P@@@^ .YY#@YJ7~7?#&@#: ... ..... ?@
@? .......... P@@@@@@@55&#B!...G@&J:..............!@@#?:PP5?..........YGGG^.......B@@@YP@#JGB! ..........?J&@~.....G@@P:..P5J#@@BJGBGPJ!........... ?@
@? .::::::::. P@@@Y7?!^~~^:....G@&J^.:::...::::::.GGP&!:G@BJ^.:::::...G@@@~.....:.B@@P~!?7^7?^.....:::::.PYP@!.::. 5@BJ^..5B5YJ?!^7??!:...:...:::::.!@
@? :::::::::..JGGG^....::::::..G@&Y^...:.........!@&P555PG5GP::::::..:G@@@~:::....5GPP^... ...:::..::::::G&P5^.....G&YG!::G@&Y:.......::..:::.......?@
@J::::::::::::P&&&!::::::::::::G@@&J!!!!!!!!!^:::G@@@BBGG#@@@!::::::::G@@@!:::::::G&@@?!!!!!!!7!^::::::::G@@@J!!!!7#@&@!::G@@@~:::::::::::::::::::::J@
@J:^^^^^^^^^^:G@@@7:^^^^^^^^^^:G@@@@@@@@@@@@@7::7@@@G^^^^7@@@G::^^^^^:B@@@!:^^^^::B@@@@@@@@@@@@@!:^^^^^^:7&@@@@@@@@@@@G^::B@@@!:^^^^^^^^^^^^^^^^^^^:J@
@J:^^^^^^^^^^^JPPP!^^^^^^^^^^^^JP55PPPPPPPPPP~^^?P5P!:^^^^YPP5^^^^^^^^JPP5~^^^^^^^YP55PPPPPPPPP5~^^^^^^^^:~?5PPPPPP5Y7^^^^JPP5~^^^^^^^^^^^^^^^^^^^^:J@
@G~^^^^^^^^^^^::::^^^^^^^^^^^^^::::::::::::::^^^:::::^^^^^::::^^^^^^^^::::^^^^^^^^::::::::::::::^^^^^^^^^^^:::::::::::^^^^::::^^^^^^^^^^^^^^^^^^^^^~G@
@@#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP#@@

""")))
    countries={
        1:"USA",
        2:"UK",
        3:"India",
    }

    table_data = [
                ['', 'Country',''],
                ['', '1:USA',''],
                ['', '2:UK',''],
                ['', '3:India',''],
                ]
    table = AsciiTable(table_data)
    print(table.table)
    country=int(input("choose country of car: "))
    print (f"You have chosen {countries[country]}")
    if country==1:
        usa()
    elif country==2:
        uk()
    elif country==3:
        india()

main()