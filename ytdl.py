#!/usr/bin/env python3.8
from pytube import YouTube
# # # download video

# get input from user
link = input("Enter the link: ")
yt = YouTube(link)

print("-----------------------------")
# print video info
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length,"seconds")
print("Description: ",yt.description)
print("Ratings: ",yt.rating)
#printing all the available streams
print("-----------------------------")

print(*yt.streams,sep ="\n")
print("-----------------------------")
print("list of streams are available please enter I tag of the stream that you like "+"\n"+
"or just click enter \nwe will find and download best quality video by default")

tag = input(" Enter the tag: ")

#choose stream
if tag == "" :
        ys = yt.streams.get_highest_resolution()
else :
        ys = yt.streams.get_by_itag(tag)


# download
ys.download('.')
print("\n \n downloaded")

print("-----------------------------")

