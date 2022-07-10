import instaloader
from instaloader import Post, Profile
import json
from termcolor import colored
from terminaltables import AsciiTable

L = instaloader.Instaloader()
with open('config/config.json','r+') as f:
    config = json.load(f)
    password=config.get('instapass')
    username=config.get('instauser')

print("Attempting to login...")
try:
  L.login(username,password)#
  print("Login successful!")
except Exception as e:
  print(colored(e,"red"))
  # if str(e).startswith("Login: Checkpoint required. Point your browser to"):
  #   split=str(e).split(" ")
  #   url=split[7]
  #   urllib.urlopen(url)
  exit()

options=['Download Posts','Download Stories','Get Followers','Get Following']

print("""                                                                                                                                                            
IIIIIIIIII                                          tttt                               SSSSSSSSSSSSSSS      tttt                            lllllll kkkkkkkk           
I::::::::I                                       ttt:::t                             SS:::::::::::::::S  ttt:::t                            l:::::l k::::::k           
I::::::::I                                       t:::::t                            S:::::SSSSSS::::::S  t:::::t                            l:::::l k::::::k           
II::::::II                                       t:::::t                            S:::::S     SSSSSSS  t:::::t                            l:::::l k::::::k           
  I::::Innnn  nnnnnnnn        ssssssssss   ttttttt:::::ttttttt      aaaaaaaaaaaaa   S:::::S        ttttttt:::::ttttttt      aaaaaaaaaaaaa    l::::l  k:::::k    kkkkkkk
  I::::In:::nn::::::::nn    ss::::::::::s  t:::::::::::::::::t      a::::::::::::a  S:::::S        t:::::::::::::::::t      a::::::::::::a   l::::l  k:::::k   k:::::k 
  I::::In::::::::::::::nn ss:::::::::::::s t:::::::::::::::::t      aaaaaaaaa:::::a  S::::SSSS     t:::::::::::::::::t      aaaaaaaaa:::::a  l::::l  k:::::k  k:::::k  
  I::::Inn:::::::::::::::ns::::::ssss:::::stttttt:::::::tttttt               a::::a   SS::::::SSSSStttttt:::::::tttttt               a::::a  l::::l  k:::::k k:::::k   
  I::::I  n:::::nnnn:::::n s:::::s  ssssss       t:::::t              aaaaaaa:::::a     SSS::::::::SS    t:::::t              aaaaaaa:::::a  l::::l  k::::::k:::::k    
  I::::I  n::::n    n::::n   s::::::s            t:::::t            aa::::::::::::a        SSSSSS::::S   t:::::t            aa::::::::::::a  l::::l  k:::::::::::k     
  I::::I  n::::n    n::::n      s::::::s         t:::::t           a::::aaaa::::::a             S:::::S  t:::::t           a::::aaaa::::::a  l::::l  k:::::::::::k     
  I::::I  n::::n    n::::nssssss   s:::::s       t:::::t    tttttta::::a    a:::::a             S:::::S  t:::::t    tttttta::::a    a:::::a  l::::l  k::::::k:::::k    
II::::::IIn::::n    n::::ns:::::ssss::::::s      t::::::tttt:::::ta::::a    a:::::a SSSSSSS     S:::::S  t::::::tttt:::::ta::::a    a:::::a l::::::lk::::::k k:::::k   
I::::::::In::::n    n::::ns::::::::::::::s       tt::::::::::::::ta:::::aaaa::::::a S::::::SSSSSS:::::S  tt::::::::::::::ta:::::aaaa::::::a l::::::lk::::::k  k:::::k  
I::::::::In::::n    n::::n s:::::::::::ss          tt:::::::::::tt a::::::::::aa:::aS:::::::::::::::SS     tt:::::::::::tt a::::::::::aa:::al::::::lk::::::k   k:::::k 
IIIIIIIIIInnnnnn    nnnnnn  sssssssssss              ttttttttttt    aaaaaaaaaa  aaaa SSSSSSSSSSSSSSS         ttttttttttt    aaaaaaaaaa  aaaallllllllkkkkkkkk    kkkkkkk                                                                                                                                                                                                                                          
""")


target=input("Enter the username of the target: ")
profile = Profile.from_username(L.context, target)

#creating options table
table_data = [
            ['', 'OPTIONS',''],
            ]
iterator=1
for option in options:
            table_data.append(["",f"{iterator}:"+option.strip(),""])
            iterator+=1
table = AsciiTable(table_data)
print(table.table)


option=input("choose an option to begin: ")
if option=="1":
  print("Downloading posts...")
  try:
    for post in profile.get_posts():
      L.download_post(post, target=profile.username)
    print(colored("Download complete!","green"))
  except Exception as e:
    print(colored("Download failed!","red"))
    print(e)

elif option=="2":
  print("Downloading stories...")
  try:
    userid= L.check_profile_id(target)
    for story in L.get_stories():
      # story is a Story object
      for item in story.get_items():
          # item is a StoryItem object
          L.download_stories(userids=[userid])
  except Exception as e:
    print(colored("Download failed!","red"))
    print(e)

elif option=="3":
  print("Getting followers...")
  try:
    for follower in profile.get_followers():
      print(follower.username)
      with open (f'loot/{profile.username}/followers.txt','a') as f:
        f.write(follower.username+'\n')
    print(colored("Process complete!","green"))
  except Exception as e:
    print(colored("Process failed!","red"))
    print(e)

elif option=="4":
  print("Getting following...")
  try:
    for following in profile.get_followees():
      print(following.username)
      with open (f'loot/{profile.username}/following.txt','a') as f:
        f.write(following.username+'\n')
      print(colored("Process complete!","green"))
  except Exception as e:
    print(colored("Process failed!","red"))
    print(e)