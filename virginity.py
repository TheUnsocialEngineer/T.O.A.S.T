import json

with open('config/config.json','r+') as f:
    config = json.load(f)
    setup=config.get('setup')