from sys import displayhook
from PIL import Image
import requests
from terminaltables import AsciiTable
from tkinter import filedialog as fd
from PIL.ExifTags import TAGS
import ffmpeg
import shutil
import os
from termcolor import colored
import json
from pprint import pprint
from pytube import YouTube

image_formats=['jpg','jpeg','png','gif','bmp','jfif','tiff','tif','webp']
table_data = [
                ['', 'Options',''],
                ['', '1:File',''],
                ['', '2:Youtube',''],
                ]
table = AsciiTable(table_data)
print(table.table)
choice=int(input("select an option to begin: "))
if choice==1:
    filename=fd.askopenfilename()
    ext=filename.split('.')[1]
    if ext in image_formats:
        file = Image.open(filename)
        info_dict = {
        "Filename": file.filename,
        "Image Size": file.size,
        "Image Height": file.height,
        "Image Width": file.width,
        "Image Format": file.format,
        "Image Mode": file.mode,
        "Image is Animated": getattr(file, "is_animated", False),
        "Frames in Image": getattr(file, "n_frames", 1)
        }
        for label,value in info_dict.items():
            print(f"{label:25}: {value}")
            
        # extract EXIF data
        exifdata = file.getexif()

        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")
    else:
        #assuming its a video since its not in the image_formats list
        os.chdir("modules/EXIFViewer")
        newfile=f"temp.{ext}"
        shutil.copyfile(filename, newfile)
        data=ffmpeg.probe("temp.mp4")["streams"]
        symbol=colored("[*]","green")
        for data in data:
            avg_frame_rate=data['avg_frame_rate']
            bit_rate=data['bit_rate']
            bits_per_raw_sample=data['bits_per_raw_sample']
            chroma_location=data['chroma_location']
            closed_captions_file=data['closed_captions']
            codec_long_name=data['codec_long_name']
            codec_name={data['codec_name']}
            codec_tag=data['codec_tag']
            codec_tag_string={data['codec_tag_string']}
            codec_typo={data['codec_type']}
            coded_height={data['coded_height']}
            coded_width=data['coded_width']
            color_primaries=data['color_primaries']
            color_range=data['color_range']
            color_space=data['color_space']
            color_transfer={data['color_transfer']}
            display_aspect_ratio=data['display_aspect_ratio']
            duration=data['duration']
            print(symbol+f" Average Frame Rate: {avg_frame_rate}")
            print(symbol+f" Bit Rate: {bit_rate}")
            print(symbol+f" Bits Per Raw Sample: {bits_per_raw_sample}")
            print(symbol+f" Chroma Location: {chroma_location}")
            print(symbol+f" Closed Captions File: {closed_captions_file}")
            print(symbol+f" Codec Long Name: {codec_long_name}")
            print(symbol+f" Codec Name: {codec_name}")
            print(symbol+f" Codec Tag: {codec_tag}")
            print(symbol+f" Codec Tag String: {codec_tag_string}")
            print(symbol+f" Codec Type: {codec_typo}")
            print(symbol+f" Coded Height: {coded_height}")
            print(symbol+f" Coded Width: {coded_width}")
            print(symbol+f" Color Primaries: {color_primaries}")
            print(symbol+f" Color Range: {color_range}")
            print(symbol+f" Color Space: {color_space}")
            print(symbol+f" Color Transfer: {color_transfer}")
            print(symbol+f" Display Aspect Ratio: {display_aspect_ratio}")
            print(symbol+f" Duration: {duration}")
            break
        os.remove(newfile)
        os.chdir("..")

elif choice==2:
    with open('config/config.json','r+') as f:
        config = json.load(f)
        key=config['youtubeapikey']
    while True:
        youturl=input("enter the url of the video: ")
        if youturl.startswith("https://www.youtube.com/watch?v="):
            symbol="["+colored("*","green")+"]"
            id=youturl.split('=')[1]
            url=f"https://youtube.googleapis.com/youtube/v3/videos?key={key}&part=snippet,contentDetails,statistics&id={id}"
            response = requests.get(url)
            data=response.json()
            video_title=data['items'][0]['snippet']['title']
            channel_title=data['items'][0]['snippet']['channelTitle']
            channel_id=data['items'][0]['snippet']['channelId']
            channel_url=f"https://www.youtube.com/channel/{channel_id}"
            channel_thumbnail=data['items'][0]['snippet']['thumbnails']['default']['url']
            channel_published_at=data['items'][0]['snippet']['publishedAt']
            likecount=data['items'][0]['statistics']['likeCount']
            viewcount=data['items'][0]['statistics']['viewCount']
            print(f"{symbol} Video Title: {video_title}")
            print(f"{symbol} Channel Title: {channel_title}")
            print(f"{symbol} Channel URL: {channel_url}")
            print(f"{symbol} Channel Thumbnail: {channel_thumbnail}")
            print(f"{symbol} Channel Published At: {channel_published_at}")
            print(f"{symbol} Like Count: {likecount}")
            print(f"{symbol} View Count: {viewcount}")

        else:
            print("invalid url")
            continue
        break